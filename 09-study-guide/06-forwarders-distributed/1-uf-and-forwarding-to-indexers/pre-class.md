---
type: pre-class
theme: 06-forwarders-distributed
topic: 1-uf-and-forwarding-to-indexers
covers: "Lectures 31–33"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/06-forwarders-distributed]
---

# Pre-class — Universal Forwarder: Installation, Inputs, and Forwarding to an Indexer

> Read before the videos (covers lectures 31–33). ~4–5 min. These demos are fast-moving and mix OS-level steps with Splunk config. Walk in knowing the model so you can follow the reasoning, not just the keystrokes.

## Why this matters
The Universal Forwarder is how data gets into Splunk in every real deployment. Every indexer cluster, every SIEM, every distributed architecture starts with UFs running on endpoints. Understanding what the UF is (and what it deliberately is not), how to wire it to an indexer, and where the common failure points are is prerequisite knowledge for everything else in platform administration.

## The mental model (hold these)

1. **The UF is a separate, stripped-down binary — not full Splunk in "light mode."** It installs to `/opt/splunkforwarder` (separate from `/opt/splunk`). No web UI. No search. No parsing pipeline. It collects and ships data only.
2. **Run the UF as a non-root `splunk` OS user.** Create the user first. Set `chown -R splunk:splunk /opt/splunkforwarder`. The process must be able to read your log files — if they're owned by root, you'll get silent failures.
3. **Two config files do the work: `inputs.conf` (what to collect) and `outputs.conf` (where to send it).** Put these inside a custom app under `etc/apps/`, not in `system/local`. The app pattern keeps things manageable and Deployment-Server-ready.
4. **The UF sends "cooked" data — metadata attached, not parsed.** `host`, `source`, `sourcetype`, and `index` are attached at the UF. But timestamp recognition, line-merging, and field extraction happen at the indexer. This is why `props.conf`/`transforms.conf` live on the indexer, not the UF.
5. **The indexer must be explicitly configured to receive.** Receiving is off by default. Enable it with `[splunktcp://9997]` in `inputs.conf` on the indexer, or via Web/CLI. Port 9997 is the conventional port — not hardcoded.
6. **The fishbucket prevents re-reads.** The UF tracks its position in each file (CRC + byte offset). If events are lost (e.g., target index didn't exist), just restarting won't re-read the files. You must clear the fishbucket.

## Key terms (quick definitions)

- **Universal Forwarder** — lightweight data-collection agent; no UI, no parsing; installs to `/opt/splunkforwarder`.
- **`splunk` OS user** — non-root account that owns and runs the UF; must have read access to log files.
- **boot-start** — systemd unit registration so the UF survives reboots (`splunk enable boot-start -systemd-managed 1`).
- **cooked data** — UF output: metadata attached but not fully parsed; indexer does the parsing.
- **`[monitor://<path>]`** — `inputs.conf` stanza that tells the UF to watch a file or directory.
- **`disabled = 0`** — enables a stanza (`1` = disabled). Common point of confusion: zero means "not disabled" = active.
- **fishbucket** — database at `var/lib/splunk/fishbucket/` tracking per-file CRC + seek position.
- **`[tcpout]` / `[tcpout:<group>]`** — `outputs.conf` stanzas; global settings + named target group with server list.
- **`[splunktcp://9997]`** — `inputs.conf` stanza on the indexer; opens receiver for Splunk forwarder protocol traffic.
- **Port 9997** — conventional Splunk receive port; agreed on both the UF (`outputs.conf`) and indexer (`inputs.conf`) sides.

## Watch for this in the video

- The OS steps (creating the `splunk` user, `chown -R`) are done quickly but are load-bearing — a wrong ownership breaks data collection silently.
- The `disabled = 0` logic is called out explicitly: zero means enabled, one means disabled. This is backwards from what you might expect.
- The `inputs.conf` is placed inside a custom app under `etc/apps/` — note why that pattern is preferred.
- When the demo shows the fishbucket being cleared to force a re-read, pay attention to *why*: because the fishbucket had already advanced the seek position past events that were lost.
- The indexer receives an error about a "disabled or deleted index" before the index is created — this is the real-world behavior when an index is missing.

## Questions to hold in mind while watching

1. What prevents the UF from re-reading a file it has already processed, even after a restart?
2. Why does `props.conf` belong on the indexer and not the UF?
3. If `outputs.conf` lists multiple indexer IPs, what happens automatically?
4. What is the significance of `[splunktcp://9997]` vs `[tcp://9997]` on the indexer?

## How this connects forward

- **Windows UF (next topic):** Same UF mechanics, different OS install method (MSI) and different input types (WinEventLog, perfmon).
- **Deployment Server:** The manual `inputs.conf`/`outputs.conf` edits you see here are what the DS automates at scale — same files, pushed as apps.
- **Indexer clustering:** In a cluster, forwarders load-balance across multiple indexer peers. The `outputs.conf` multi-server group pattern introduced here is the same mechanism.
- **Technology add-ons:** The `sourcetype` you set in `inputs.conf` is the hook that ties into `props.conf` on the indexer for parsing. You'll see this explicitly in the data-onboarding topic.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| Install a *nix universal forwarder | https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Installanixuniversalforwarder |
| Enable boot-start (Linux, systemd) | https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Installleastprivileged |
| Configure forwarding with outputs.conf | https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Configureforwardingwithoutputs.conf |
| Configure the UF using configuration files | https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Configuretheuniversalforwarder |
| Enable a receiver (indexer side) | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Enableareceiver |
| Types of forwarders | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Typesofforwarders |
| Troubleshoot forwarder/receiver connection | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Receiverconnection |
