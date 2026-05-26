---
type: pre-class
theme: 02-install-bestpractices
topic: installation-linux-and-windows
covers: "Lectures 9–16"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/02-install-bestpractices]
---

# Pre-class — Installation & Post-Install Setup (Linux & Windows)

> Read before the lectures (covers lectures 9–16). ~4–5 min. The videos are hands-on labs; this primer gives you the *why* behind each step and the current best-practice version of it, so you're not just copying commands.

## Why this matters
Getting Splunk running is easy. Getting a *healthy* Splunk — non-root, boots cleanly, THP off, ulimits raised — is what separates a box that survives load from one that crawls or crashes. THP and ulimit are **mandatory**, not optional tuning.

## The mental model (hold these)
1. **Install = same package, role decided later.** Linux uses a `.tgz` you unpack to `/opt/splunk` (`$SPLUNK_HOME`) and **`chown` to the `splunk` user**; Windows uses an `.msi` wizard. (The Universal Forwarder is a separate package.)
2. **Run it safely:** as a **non-root `splunk` user**, **started on boot via systemd** (`enable boot-start -systemd-managed 1 -user splunk`).
3. **Two mandatory Linux best practices:** **disable THP** (both `enabled` *and* `defrag` = `never`) and **raise ulimits** (`nofile 64000`, `nproc 16000`, `fsize unlimited`). THP alone can cost ≥30% performance.
4. **Persistence matters:** `echo never` to a THP file resets on reboot — persist via tuned/systemd (modern) or init.d (legacy). With systemd, ulimits go in the **unit file**, not just `limits.conf`.
5. **Verify with the Monitoring Console health check** — it flags hardware, ulimit, and THP problems.

## Key terms (quick definitions)
- **`$SPLUNK_HOME`** — `/opt/splunk` (Linux), `C:\Program Files\Splunk` (Windows).
- **`splunk` CLI** — `$SPLUNK_HOME/bin/splunk` → `start`/`stop`/`restart`/`status`/`version`.
- **`user-seed.conf`** — pre-seeds the admin password before first start (for automation).
- **`enable boot-start -systemd-managed 1`** — makes Splunk a systemd service that starts on boot.
- **THP (Transparent Huge Pages)** — Linux memory feature you must turn off for Splunk.
- **ulimit** — per-process resource ceilings; raise open files / processes / file size.
- **MSI / service account** — Windows install; the key choice is which account Splunk runs as (Local System vs. dedicated/domain).

## Watch for this in the video
- Note the **non-root user** + **`chown splunk:splunk /opt`** — forgetting this is the #1 install failure.
- The course disables THP via an **init.d script** — that's the legacy way. On a modern systemd distro, prefer a **tuned profile** or systemd one-shot. The *goal* (both `enabled` and `defrag` = `never`, persistent) is what matters.
- The ulimit edit shown targets `limits.conf`; remember that a **systemd-managed** Splunk reads limits from its **unit file** instead.
- On the health check, the "physical memory below recommendation" warning is the **12 GB reference hardware** baseline.
- Windows install: the only real decision is the **service account** — Local System (simple, over-privileged) vs. a dedicated/domain account (least privilege, needed for remote logs).

## Questions to hold in mind while watching
1. Why `chown` the install to the `splunk` user, and what breaks if I don't?
2. Why must I disable **both** THP `enabled` and `defrag`, and why isn't `echo never` enough?
3. If Splunk is systemd-managed, where do my ulimit values actually need to go?
4. On Windows, which service account would I pick and why?

## How this connects forward
- **Apps & configuration files** explains the `etc/system` and `etc/apps` directories you see under `$SPLUNK_HOME`.
- **Indexes & buckets** uses `var/lib/splunk` (where data lands) and the disk planning from the prerequisites topic.
- The **deployment server** and **forwarders** topics build on this base install across many machines.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Install on Linux | https://docs.splunk.com/Documentation/Splunk/latest/Installation/InstallonLinux |
| Install on Windows | https://docs.splunk.com/Documentation/Splunk/latest/Installation/InstallonWindows |
| Run Splunk as a systemd service / boot-start | https://docs.splunk.com/Documentation/Splunk/latest/Admin/RunSplunkassystemdservice |
| Transparent huge pages and Splunk performance | https://docs.splunk.com/Documentation/Splunk/latest/ReleaseNotes/SplunkandTHP |
| ulimit errors / recommended values | https://docs.splunk.com/Documentation/Splunk/latest/Troubleshooting/ulimitErrors |
| Configure Linux systems running systemd (limits) | https://docs.splunk.com/Documentation/Splunk/latest/Workloads/Configuresystemd |
| Monitoring Console / health check | https://docs.splunk.com/Documentation/Splunk/latest/DMC/DMCoverview |
