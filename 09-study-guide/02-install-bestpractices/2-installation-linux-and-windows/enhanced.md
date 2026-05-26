---
type: enhanced
theme: 02-install-bestpractices
topic: installation-linux-and-windows
covers: "Lectures 9–16"
tags: [study-guide/enhanced, theme/02-install-bestpractices]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Installation & Post-Install Setup — Linux & Windows

> Deep reference on actually installing Splunk Enterprise on Linux and Windows, then performing the mandatory OS-level best practices (THP, ulimit), configuring boot-start with systemd, and running a post-install health check. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

This is the hands-on core of getting a healthy Splunk instance running. The work splits into:

1. **Install** — put Splunk on disk and start it (Linux tarball; Windows MSI).
2. **Run it safely** — as a non-root service that starts on boot (systemd).
3. **Tune the OS** — the two non-negotiable Linux best practices: **disable Transparent Huge Pages (THP)** and **raise ulimits**.
4. **Verify** — confirm health via the Monitoring Console health check.

Skipping steps 3–4 is the single most common cause of a Splunk box that "works" but performs badly or crashes under load. Treat THP and ulimit as mandatory, not optional.

---

## 1. The install model (recap)

Every full component installs from the **same Splunk Enterprise package**; configuration determines its role. The **Universal Forwarder is the one separate, lightweight package**. So "install Splunk" is the same act whether the box will become an indexer, search head, or heavy forwarder — the differences come later, in configuration.

`$SPLUNK_HOME` is the install root — `/opt/splunk` on Linux by convention, `C:\Program Files\Splunk` on Windows by default. The `splunk` CLI lives in `$SPLUNK_HOME/bin`.

---

## 2. Installing on Linux (tarball)

The portable, production-standard path. Steps:

1. **Get the package.** From your Splunk account, copy the `wget` command for the Linux `.tgz` (install `wget` first if needed: `sudo apt update && sudo apt install wget`).
   ```
   wget -O splunk-<ver>-Linux-x86_64.tgz "https://download.splunk.com/.../splunk-<ver>-Linux-x86_64.tgz"
   ```
2. **Create the non-root service account:** `sudo adduser splunk`.
3. **Unpack into `/opt`** so the tree lands at `/opt/splunk` (= `$SPLUNK_HOME`):
   ```
   sudo tar -xzvf splunk-<ver>-Linux-x86_64.tgz -C /opt
   ```
4. **Change ownership** to the service account so Splunk can write data/logs:
   ```
   sudo chown -R splunk:splunk /opt/splunk
   ```
5. **First start as the splunk user**, accepting the license:
   ```
   sudo -u splunk /opt/splunk/bin/splunk start --accept-license
   ```
   On first run Splunk prompts you to create the **admin** account (username + password). Web comes up on **:8000**.
6. **Manage it** with the CLI: `splunk status`, `splunk stop`, `splunk restart`, `splunk version`.

> **Why `-C /opt` + `chown`:** if you unpack as root and forget to hand ownership to the `splunk` user, Splunk can't write to its own directories and start-up fails or behaves erratically. This is the most common beginner stumble.

---

## 3. Automating the first-run admin (`user-seed.conf`)

Interactive first-run prompts don't scale and break automation. To pre-seed the admin credential, place a **`user-seed.conf`** in `$SPLUNK_HOME/etc/system/local/` *before* first start:

```
[user_info]
USERNAME = admin
PASSWORD = <strong-password>
```

Splunk consumes it on first start to create the admin user non-interactively. Use this for repeatable/scripted builds (and later, infrastructure-as-code). You can also start non-interactively with `--accept-license --answer-yes --no-prompt`.

---

## 4. Running as non-root & boot-start with systemd

You want Splunk to **start automatically on boot** and run **as the `splunk` user under systemd** (the modern, recommended manager — it handles restarts, resource limits, and logging).

```
sudo /opt/splunk/bin/splunk stop                       # stop first
sudo /opt/splunk/bin/splunk enable boot-start \
     -systemd-managed 1 -user splunk -group splunk
```

What this does and why it matters:

- Generates a **`Splunkd.service`** systemd unit (in `/etc/systemd/system/`) so the OS manages the process. `-user`/`-group` are optional but **recommended** — they make systemd run Splunk as the non-root account.
- The unit file is where systemd-enforced **ulimits** live (see §6) — `LimitNOFILE`, `LimitNPROC`, etc.
- **polkit rules** (Splunk 8.1.1+, via `create-polkit-rules`) let the non-root `splunk` user run `start`/`stop`/`restart` under systemd **without sudo**, avoiding sudoers edits.
- Requires Splunk 7.2.2+.

After this, manage Splunk via `systemctl start/stop/status Splunkd` (or the `splunk` CLI, which delegates to systemd).

---

## 5. Best practice: disable Transparent Huge Pages (THP)

**What THP is:** a Linux kernel feature that automatically coalesces standard memory pages into large "huge" pages to reduce TLB overhead. Good for some workloads — **bad for Splunk**.

**Why disable it for Splunk:** THP is too aggressive at coalescing pages for the many **short-lived processes** Splunk spawns (searches), it **prevents the jemalloc allocator from releasing memory** back to the OS, and it can cause **I/O regressions** from swapping huge pages. Splunk has measured a **minimum ~30% degradation in indexing and search performance** (and a similar latency increase) when THP is active. This is a large, well-documented hit — hence "mandatory."

**Critical nuance:** you must disable **both** `enabled` **and** `defrag` (direct memory compaction). Leaving *either* on still severely degrades performance.

**Verify current state:**
```
cat /sys/kernel/mm/transparent_hugepage/enabled   # want: [never]
cat /sys/kernel/mm/transparent_hugepage/defrag     # want: [never]
```
Echoing `never` into those files works but is **not persistent** across reboot.

**Make it persistent — modern vs. legacy:**
- **Modern (recommended):** use a **`tuned`** profile (`tuned-adm`) that sets `transparent_hugepages=never`, or a small **systemd one-shot unit** that writes `never` at boot. These fit current systemd-based distros cleanly.
- **Legacy:** an **init.d script** (e.g., `/etc/init.d/disable-thp` registered with `update-rc.d`) that echoes `never` to both paths at boot. This is what older courses show; it still works on init.d systems but is the old pattern.

---

## 6. Best practice: increase ulimits

**What ulimits are:** per-user/process resource ceilings a *nix shell imposes. Splunk runs many threads, opens many files (buckets, tsidx, network sockets), and spawns many search processes — so the **OS defaults are too low** and Splunk will log warnings or fail under load (you'll see ulimit warnings in `splunkd.log`).

**Recommended values (current Splunk guidance):**

| Limit | Recommended | What it governs |
|---|---|---|
| **open files** (`nofile`) | **64000** (hard) | file descriptors — buckets, sockets |
| **max user processes** (`nproc`) | **16000** (hard) | threads/processes Splunk can spawn |
| **max file size** (`fsize`) | **unlimited** (`-1`) | size of files Splunk can create |
| data/`core`/etc. | unlimited | misc segment limits |

**Where to set them:**
- **systemd-managed (preferred):** set in the `Splunkd.service` unit (or a drop-in). Splunk's recommended systemd values: `LimitNOFILE=65536`, `LimitNPROC=16000`, `LimitDATA=8589934592` (8 GB), `LimitFSIZE=infinity`, `TasksMax=8192`. With systemd, **the unit file's limits apply** — editing `limits.conf` alone won't affect a systemd-managed service.
- **Non-systemd / shell:** `/etc/security/limits.conf` (or a file in `limits.d/`) with `soft`/`hard` entries, e.g. `* hard nofile 64000`.

**Verify:** `ulimit -a` as the splunk user (or check the running service's limits); the Monitoring Console health check also reports them.

---

## 7. Installing on Windows

The Windows path uses the **`.msi`** installer (GUI wizard or silent install):

1. Download the MSI; double-click to launch the **installation wizard**.
2. Accept the license; choose install path (default `C:\Program Files\Splunk`).
3. **Choose the service account Splunk runs as** — the key Windows decision:
   - **Local System** — simplest; broad local privileges. Acceptable for a single host but over-privileged.
   - **Domain / dedicated low-privilege account** — recommended when Splunk must read remote logs, Windows Event Logs across the domain, or network shares. Grant it only the rights it needs (e.g., "Log on as a service," read access to target logs).
4. Set the **admin** username/password; optionally create a Start-menu shortcut.
5. Finish; Splunk installs and runs as a **Windows service** (`splunkd`), Web on **:8000** (`http://localhost:8000`).

**Silent/automated install** is available via `msiexec` with parameters (e.g., `AGREETOLICENSE=Yes`, `SPLUNKUSERNAME`, `SPLUNKPASSWORD`, install dir) for scripted deployment.

> THP/ulimit are **Linux** concerns — they don't apply on Windows. On Windows the equivalents are the **service account privileges** and standard Windows performance/AV-exclusion considerations (exclude Splunk's data dirs from antivirus scanning).

---

## 8. First login & essential server settings

After install, in **Settings → Server settings → General settings**, set the basics:

- **Server name** and **default host name** — meaningful identifiers (these become the `host` on the instance's own data).
- **Management port (8089)** and **Web port (8000)** — confirm/change.
- **Run Splunk Web** and **enable HTTPS/SSL** for the web UI (best practice — note Splunk uses a **self-signed cert** by default, so browsers warn until you install a CA-signed cert).
- **"Pause indexing if free disk space falls below N MB"** — the **minimum free disk** guard. If your lab disk is small, Splunk shows a yellow warning; you can lower the threshold to clear it, but understand it's protecting you from filling the disk. Changing it requires a restart (Settings → Server controls → Restart).

---

## 9. Post-install health check (Monitoring Console)

Verify the box is healthy and adhering to best practices via **Settings → Monitoring Console**:

1. Set the MC mode to **Standalone** (this instance only) in **General Setup**, confirm the server roles (e.g., license manager / search head / indexer for a single instance), and apply.
2. Run **Health Check** — a comprehensive set of checks for the instance.

What it flags (and ties back to this topic):
- **Hardware vs. reference** — e.g., "physical memory below the 12 GB reference" if under-spec.
- **Server limits (ulimit)** — pass if you raised `nofile`/`nproc`; shows current vs. recommended.
- **Transparent Huge Pages** — pass if both `enabled` and `defrag` are `never`.

A clean health check means Splunk is installed, hardened, and ready for further deployment.

---

## 10. The Splunk CLI & directory layout (orientation)

**Essential CLI** (`$SPLUNK_HOME/bin/splunk`): `start` / `stop` / `restart` / `status`, `version`, `enable boot-start`, `show`/`set` config, `btool` (inspect effective config — covered in the conf-files topic), `help`.

**Directory layout under `$SPLUNK_HOME`:**
- `bin/` — the `splunk` binary and CLI.
- `etc/` — **all configuration**: `etc/system/` (default + local), `etc/apps/` (apps), `etc/users/` (per-user). (Layering is its own topic.)
- `var/lib/splunk/` — **the indexes** (your data/buckets).
- `var/log/splunk/` — Splunk's own logs (`splunkd.log`, etc.) — first stop for troubleshooting.

---

## 11. Terminology & version notes

- **systemd is the current standard** for boot-start (`enable boot-start -systemd-managed 1`). Older material uses **init.d** scripts (and disables THP via an init.d script). On modern distros, prefer systemd / `tuned`.
- With **systemd-managed** Splunk, **ulimits belong in the unit file** (`LimitNOFILE`, etc.), not only in `limits.conf` — a common gotcha when limits "don't take."
- **polkit rules** (8.1.1+) are the modern way to let the non-root splunk user control the service without sudo.
- First-run automation via **`user-seed.conf`** and `--no-prompt` flags is current best practice for repeatable installs.

---

## 12. Common misconceptions

- **"Disabling THP once (echo never) is enough."** That's not persistent — it resets on reboot. Use tuned/systemd/init.d to persist, and disable **both** `enabled` and `defrag`.
- **"limits.conf controls my systemd service."** No — for a systemd-managed Splunk, the **unit file** limits apply.
- **"Run Splunk as root for convenience."** Use the non-root `splunk` account; root creates security and permission problems and complicates systemd.
- **"THP/ulimit are optional tuning."** They're mandatory on Linux — THP alone can cost ≥30% performance.
- **"Windows is the same as Linux."** Different installer (MSI), no THP/ulimit, and the big decision is the **service account** privileges.
- **"Forgot to `chown` — but it started, so it's fine."** Ownership problems cause subtle write failures; always hand the tree to the `splunk` user.

---

## 13. Mastery checklist — what you should be able to explain

- The Linux tarball install sequence: unpack to `/opt/splunk`, `chown` to the service account, first start `--accept-license`, create admin.
- **`user-seed.conf`** for non-interactive admin creation.
- **`splunk enable boot-start -systemd-managed 1 -user splunk`** and why systemd/non-root.
- **THP**: disable both `enabled` and `defrag`; the performance rationale; verify via `/sys/kernel/mm/transparent_hugepage/*`.
- **ulimit**: recommended `nofile 64000`, `nproc 16000`, `fsize unlimited`; with systemd they go in the unit file.
- Windows MSI install and the **service-account** choice (Local System vs. dedicated/domain).
- The **Monitoring Console health check** and what it validates (hardware, ulimit, THP).
- Default ports and Splunk Web HTTPS/self-signed cert.

---

## 14. Key terms (flashcard seeds)

- **`$SPLUNK_HOME`** — install root (`/opt/splunk` Linux, `C:\Program Files\Splunk` Windows).
- **`splunk` CLI** — `$SPLUNK_HOME/bin/splunk` (start/stop/restart/status/version/enable boot-start).
- **`--accept-license`** — non-interactive license acceptance on first start.
- **`user-seed.conf`** — pre-seeds the admin credential before first start.
- **`enable boot-start -systemd-managed 1`** — register Splunk as a systemd service that starts on boot.
- **`Splunkd.service`** — the generated systemd unit (holds enforced ulimits).
- **polkit rules** — let the non-root splunk user control the service without sudo (8.1.1+).
- **Transparent Huge Pages (THP)** — kernel feature that must be disabled (both `enabled` and `defrag`) for Splunk.
- **jemalloc** — Splunk's memory allocator, which THP interferes with.
- **ulimit** — per-process resource limits; raise `nofile`→64000, `nproc`→16000, `fsize`→unlimited.
- **`/etc/security/limits.conf`** — shell-level ulimit config (not used by a systemd-managed service).
- **MSI / `msiexec`** — Windows installer / silent-install tool.
- **Service account (Windows)** — Local System vs. dedicated/domain account Splunk runs as.
- **Minimum free disk** — threshold below which Splunk pauses indexing.
- **Monitoring Console health check** — validates hardware, ulimit, THP, etc.

---

## 15. Questions to drill (quiz seeds)

1. Give the ordered Linux tarball install steps from download to first login. Why the `chown`?
2. What does `user-seed.conf` do, where does it go, and why use it?
3. Write the command to make Splunk start on boot under systemd as the `splunk` user. Why stop Splunk first?
4. Why must THP be disabled for Splunk, and what's the measured performance impact? Which two settings must both be `never`?
5. Why isn't `echo never > .../enabled` sufficient on its own?
6. List the recommended ulimit values. Where do they belong when Splunk is systemd-managed, and why not just `limits.conf`?
7. On Windows, what's the key decision during install, and what are the options/trade-offs?
8. Which OS best practices (THP, ulimit) do *not* apply to Windows, and what's the Windows-equivalent concern?
9. Name three things the Monitoring Console health check validates from this topic.
10. What does the "pause indexing if free disk below N" setting protect against, and what do you do after changing it?
