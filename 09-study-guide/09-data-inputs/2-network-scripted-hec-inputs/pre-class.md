---
type: pre-class
theme: 09-data-inputs
topic: 2-network-scripted-hec-inputs
covers: "Lectures 51–53"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/09-data-inputs]
---

# Pre-class — Data Inputs: Network, Scripted, and HTTP Event Collector

> Read before the videos (covers lectures 51–53). ~4–5 min. Three distinct input mechanisms with very different operational models — walk in knowing the shape of each so the demos are confirmatory rather than introductory.

## Why this matters
Not everything you want to index lives in a file you can tail. Network devices send syslog to a port. Operating system state lives in command output. Cloud-native applications can't run agents. These three input types — network, scripted, and HEC — cover those gaps. More practically: in a security engineering context, syslog from firewalls and scripted collection from APIs are bread-and-butter data sources. HEC is increasingly how modern applications integrate with Splunk. Misconfiguring any of them means data gaps you might not notice until an incident.

## The mental model (hold these)
1. **Network inputs listen on a port.** `[udp://<port>]` and `[tcp://<port>]` in `inputs.conf` are passive listeners. `connection_host` controls where the `host` field comes from: `ip` (sender's IP — usually right), `dns` (reverse lookup — fragile), `none` (static — almost always wrong for network data). Choose `ip` by default.
2. **Direct syslog on an indexer is an anti-pattern.** UDP drops packets when overwhelmed; the indexer has better things to do than handle raw socket I/O. Put a Heavy Forwarder (or SC4S) in front to absorb bursts, buffer to disk, and forward reliably. `persistentQueueSize` on the HF's input is what protects you during indexer unavailability.
3. **Scripted inputs run a command and index its stdout.** The `[script://<path>]` stanza; `interval` (seconds or cron) controls frequency. Scripts live in the app's `bin/` directory and must be executable. They run as the Splunk process user — not root. Stdout = events; stderr = splunkd.log only.
4. **Modular inputs are what scripted inputs grew up to be.** Same idea, but packaged, GUI-configurable, per-stanza execution. For technology add-ons, use modular inputs. For quick one-off scripts, scripted inputs are fine.
5. **HEC is a token-authenticated HTTP endpoint on port 8088.** No agent required. Bearer token in `Authorization: Splunk <token>` header on every request. Two endpoints: `/services/collector/event` (JSON, with metadata override per event) and `/services/collector/raw` (plain text). Token controls which indexes data can reach via `allowedIndexes`.
6. **HEC is disabled by default; enabling takes two steps:** turn on global settings (`[http]` stanza, `disabled = 0`), then create a token (`[http://<name>]` stanza). Everything lives in the `splunk_httpinput` app's `local/inputs.conf`.

## Key terms (quick definitions)
- **`[udp://<port>]` / `[tcp://<port>]`** — network port listeners in `inputs.conf`.
- **`connection_host`** — `ip` / `dns` / `none`; controls `host` field derivation from the sender.
- **`queueSize`** — in-memory input buffer (default 500 KB); `persistentQueueSize` is the disk overflow.
- **`[script://<path>]`** — scripted input; indexes stdout of a scheduled executable.
- **`interval`** — seconds or cron expression for script run frequency.
- **Modular input** — packaged modern alternative to scripted inputs; GUI-configurable, per-stanza.
- **HEC** — HTTP Event Collector; agentless, token-authenticated, port 8088.
- **`Authorization: Splunk <token>`** — required HTTP header on every HEC request.
- **`/services/collector/event`** — structured JSON endpoint; per-event metadata override.
- **`/services/collector/raw`** — raw text endpoint; uses token defaults.
- **`allowedIndexes`** — per-token list of permitted destination indexes.
- **Indexer acknowledgement** — `ackEnabled = true`; returns ackID; client polls `/services/collector/ack` to confirm indexing.

## Watch for this in the video
- The network input demo configures a port listener on the Universal Forwarder (not the indexer) — note this architectural choice and why it matters.
- `connection_host = ip` versus `dns` — the demo uses ip; watch what host field appears on the indexed events.
- `queueSize` is explained in the context of a firewall sending bursts — connect it to the persistent queue concept for "what happens when the indexer is unreachable."
- The scripted input demo copies scripts from the Splunk Add-on for Unix and Linux into the app's `bin/` directory — this is the canonical pattern.
- HEC demo flow: enable global settings → create token → copy token value → send with curl → search index. Follow each step; the btool output confirms what was actually written to `inputs.conf`.
- The invalid-token test in the HEC demo shows exactly what HEC returns when the token doesn't match — internalize that response.

## Questions to hold in mind while watching
1. Why is the network input configured on a forwarder here rather than directly on the indexer?
2. What would happen to UDP syslog events during the 30 seconds it takes to restart the forwarder after a config change?
3. For the scripted input: if the script writes to stderr instead of stdout, where does that output go?
4. You have 20 applications that all need to send events via HEC. Should they share a token? Why or why not?

## How this connects forward
- **Data onboarding** (`props.conf` / `transforms.conf`) processes events *after* they arrive via any of these inputs — the sourcetype you assign here is the first thing `props.conf` looks up.
- **Distributed architecture** — HF pools handling syslog or HEC are a core part of the ingest tier in any serious deployment; the network input here is that HF's configuration.
- **Security content** — if you're building detection on firewall or proxy logs, understanding where and how they arrive (UDP 514 → HF → indexer) directly affects how you interpret `host`, `source`, and latency characteristics in your events.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| Get data from TCP and UDP ports | https://docs.splunk.com/Documentation/Splunk/latest/Data/Monitornetworkports |
| How Splunk handles syslog data over UDP | https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/HowSplunkEnterprisehandlessyslogdata |
| Get data from scripted inputs | https://docs.splunk.com/Documentation/Splunk/latest/Data/Getdatafromscriptedinputs |
| Setting up a scripted input | https://docs.splunk.com/Documentation/Splunk/latest/AdvancedDev/ScriptSetup |
| Set up and use HTTP Event Collector in Splunk Web | https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector |
| Set up HEC with configuration files | https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/UseHECusingconffiles |
| About HEC Indexer Acknowledgement | https://docs.splunk.com/Documentation/Splunk/latest/Data/AboutHECIDXAck |
| Scale HEC with distributed deployments | https://docs.splunk.com/Documentation/Splunk/latest/Data/ScaleHTTPEventCollector |
| Use persistent queues to prevent data loss | https://docs.splunk.com/Documentation/Splunk/latest/Data/Usepersistentqueues |
| inputs.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf |
