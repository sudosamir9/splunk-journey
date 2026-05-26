---
type: enhanced
theme: 09-data-inputs
topic: 1-monitoring-inputs-files-directories
covers: "Lectures 46–50"
tags: [study-guide/enhanced, theme/09-data-inputs]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Data Inputs: Monitoring Files and Directories

> Deep reference on the full spectrum of Splunk input types, with particular depth on the `monitor` input: how `inputs.conf` [monitor://] stanzas work, directory vs single-file monitoring, recursive subdirectory traversal, path wildcards (`...` vs `*`), dynamic host derivation with `host_regex` and `host_segment`, allowlist/denylist filtering, and the fishbucket mechanism that prevents duplicate indexing. Also covers `batch` and `oneshot` one-time input modes. Every concept is grounded in real `inputs.conf` stanzas. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Every event Splunk indexes arrives through a **data input**. Inputs are defined in `inputs.conf` and executed on whatever component runs the input — a Universal Forwarder (UF), a Heavy Forwarder (HF), or directly on an indexer. The input is responsible for the first three things Splunk must know about any data: **where to get it, what to call it (sourcetype, index), and how to track read position** so data is never indexed twice.

The `monitor` input — which tails files and directories continuously — is the most widely used input type in enterprise deployments. Understanding it in depth, including its file-tracking internals, is essential before building or troubleshooting any data pipeline.

---

## 1. Input type overview

Splunk supports several families of data input:

| Input family | inputs.conf stanza | Delivery model | Primary use cases |
|---|---|---|---|
| File/directory monitor | `[monitor://<path>]` | Continuous, non-destructive | Application logs, OS logs, growing log files |
| Batch (archive loader) | `[batch://<path>]` | One-shot, destructive (deletes after read) | Historical archives, one-time bulk import |
| Network — TCP | `[tcp://<port>]` | Continuous, port listener | Syslog over TCP, custom protocol data |
| Network — UDP | `[udp://<port>]` | Continuous, port listener | Syslog (UDP 514), SNMP traps, simple telemetry |
| Scripted | `[script://<cmd>]` | Scheduled (interval or cron), stdout | API polling, OS metrics, custom collection |
| Modular | `[<scheme>://<name>]` | Scheduled or event-driven, packaged | Packaged technology integrations (add-ons) |
| HTTP Event Collector | `[http]` / `[http://<token>]` | Push over HTTP/HTTPS, agentless | App logging, cloud-native, IoT, forwarder-free |
| Windows-specific | `[WinEventLog://...]`, `[perfmon://...]`, etc. | Continuous | Windows event logs, performance counters, AD |

The `monitor`, network, scripted, and HEC inputs are the most important for a platform administrator to understand from first principles. Modular inputs are the architect's choice for packaged technology add-ons.

---

## 2. The `monitor` input in depth

### 2.1 Basic stanza syntax

```ini
[monitor:///var/log/messages]
index       = os
sourcetype  = linux_messages_syslog
disabled    = false
```

The stanza header `[monitor://<path>]` can point to:
- A **single file**: `[monitor:///var/log/auth.log]`
- A **directory**: `[monitor:///var/log/]` — monitors everything directly inside it
- A **path with wildcards**: `[monitor:///var/log/apache/.../access.log]` — see §4 for wildcard rules

Splunk tails the file or directory continuously. New bytes appended to a monitored file are picked up and forwarded. This is the "live tail" model — identical to `tail -f` in behavior.

### 2.2 Core attributes

| Attribute | Type | Default | Meaning |
|---|---|---|---|
| `index` | string | `main` | Destination index for events from this input |
| `sourcetype` | string | auto-detected | Sourcetype assigned to events |
| `host` | string | hostname of the machine | Static host field for events from this input |
| `disabled` | bool (0/1) | `false` | Set to `true` / `1` to disable without removing the stanza |
| `followTail` | bool (0/1) | `0` | `1` = start reading from the current end of file (like `tail -f` on a fresh file); `0` = read from the beginning on first encounter |
| `recursive` | bool | `true` | `true` = also monitor subdirectories found inside a monitored directory |
| `crcSalt` | string | none | Salt added to CRC fingerprint calculation (see §6) |
| `initCrcLength` | int (bytes) | `256` | Number of bytes used for the initial CRC fingerprint |

### 2.3 Monitoring a directory versus a single file

When the `monitor://` path points to a **directory**, the monitor input discovers all files within that directory. With `recursive = true` (the default), it descends into subdirectories as well. With `recursive = false`, it watches only the immediate directory level.

```ini
# Monitor everything under /var/log recursively (default behaviour)
[monitor:///var/log]
index      = os
sourcetype = linux_syslog

# Monitor only /var/log directly, no subdirectories
[monitor:///var/log]
index     = os
recursive = false
```

When the path points to a **single file**, `recursive` has no effect. Only that exact file is tailed.

### 2.4 `followTail`

`followTail = 1` instructs the monitor processor to seek to the **end** of the file before starting to read. This is useful for very large existing files that you do not want to fully re-index on initial deployment. Once monitoring begins, all subsequently appended data is captured.

`followTail = 0` (default) means the monitor reads the file from the **beginning** the first time it encounters it. After the initial ingest, only new data appended after that point is forwarded.

> Do not set `followTail = 1` on a production deployment without intent. It permanently skips historical data. If you later clear the fishbucket (see §6), the file will be read again from the beginning — the `followTail` setting only applies the first time Splunk opens a file, not on re-discovery after fishbucket clear.

---

## 3. Assigning metadata from the path

By default the `host` field is set to the hostname of the machine running the input. When you are collecting logs from **multiple servers' files** gathered onto a single machine (e.g., a central log aggregator), the host field would be wrong — all events would show the aggregator's hostname, not the originating server. Two attributes solve this.

### 3.1 `host_segment`

Sets the host to the **Nth path segment** (counting from 1, splitting on `/` or `\`).

```ini
[monitor:///data/servers/.../access.log]
index        = web
host_segment = 3
```

Path example: `/data/servers/web01/access.log`
- Segment 1: `data`
- Segment 2: `servers`
- Segment 3: `web01`  ← this becomes the host

`host_segment` is an integer, deterministic, and requires no regex knowledge. The limitation: if path depth varies across files (different servers sitting at different nesting levels), a fixed integer will not be correct for all of them.

### 3.2 `host_regex`

Uses a **regular expression with a capturing group** to extract the host value from the full path. The first capturing group in the regex becomes the host.

```ini
[monitor:///data/servers/.../access.log]
index      = web
host_regex = /servers/(web\d+)/
```

Path `/data/servers/web03/logs/access.log` → captured group `web03` → `host = web03`.

`host_regex` is more flexible than `host_segment` when paths vary in depth, because regex anchors to a pattern rather than a fixed position.

> `host_regex` and `host_segment` are **mutually exclusive** within a single stanza. You cannot specify both. If both are present, the behavior is undefined.

---

## 4. Path wildcards

Splunk's monitor input supports two wildcard characters in path specifications. These are **not** standard glob or regex — they are specific to `inputs.conf` path matching.

### 4.1 `*` — single-segment wildcard

Matches **any characters within a single path segment** (i.e., between two `/` or `\` separators). It does not cross directory boundaries.

```
/var/log/*/messages
```
Matches:
- `/var/log/app1/messages`
- `/var/log/app2/messages`

Does NOT match:
- `/var/log/messages` (no segment between `log` and `messages`)
- `/var/log/app1/sub/messages` (crosses a segment boundary)

### 4.2 `...` — recursive multi-segment wildcard (ellipsis)

Matches **any number of path segments, including zero**, crossing directory separators. It is the recursive descent wildcard.

```
/var/log/.../messages
```
Matches:
- `/var/log/messages` (zero intervening directories)
- `/var/log/app1/messages`
- `/var/log/app1/sub/messages`
- `/var/log/a/b/c/messages`

The ellipsis can appear anywhere in a path, including at the end to mean "everything recursively from here":

```
/var/log/apache/...
```
Matches every file at any depth under `/var/log/apache/`.

### 4.3 Combining wildcards

Wildcards can be combined in the same path for fine-grained targeting:

```ini
# Monitor access.log from any server directory at any depth
[monitor:///data/servers/.../server*/access.log]
index = web
```

Here `...` crosses any number of directories, then `server*` matches any single-segment name starting with "server", and `access.log` is literal.

### 4.4 Wildcard comparison table

| Wildcard | Crosses dir boundaries | Matches zero levels | Example |
|---|---|---|---|
| `*` | No | N/A | `/log/*/app.log` matches `/log/web/app.log` |
| `...` | Yes | Yes | `/log/.../app.log` matches `/log/app.log` and `/log/a/b/app.log` |

---

## 5. Allowlist and denylist filtering

When a monitor stanza covers a broad directory path (e.g., `/var/log/...`), you often want to **include only certain files** or **exclude others**. The `allowlist` and `denylist` attributes accept regular expressions matched against the full file path.

In Splunk 9.x, the current attribute names are `allowlist` and `denylist`. The previous names `whitelist` and `blacklist` still work and are documented as deprecated synonyms — you may encounter them in older configs or documentation.

| Attribute | Current name | Deprecated synonym | Effect |
|---|---|---|---|
| Include filter | `allowlist` | `whitelist` | Monitor only files whose path matches this regex |
| Exclude filter | `denylist` | `blacklist` | Do not monitor files whose path matches this regex |

**Precedence rule:** if a file's path matches both the allowlist and the denylist, the **denylist wins** — the file is not monitored.

```ini
# Monitor /var/log but only files whose path contains "apache"
[monitor:///var/log/...]
index     = web
allowlist = apache

# Monitor /var/log/app but exclude .gz compressed files and temp files
[monitor:///var/log/app/...]
index    = app
denylist = \.gz$|\.tmp$
```

The regex is matched against the **full file path** as a substring match (not anchored unless you add `^` or `$`). Use `$` to anchor to the end (e.g., `\.log$` to match only files ending in `.log`).

### 5.1 Combining allowlist with host_regex

A common pattern: use a `...` wildcard to scan a deep directory, use `allowlist` to narrow to specific files, and use `host_regex` to extract the server name from the path — all in one stanza:

```ini
[monitor:///data/logs/...]
index      = app
allowlist  = /(server\d+)/.*\.log$
host_regex = /(server\d+)/
```

Any file matching the pattern `/(serverN)/anything.log` anywhere under `/data/logs/` will be monitored, and the host field will be set to the `serverN` portion of the path.

---

## 6. How Splunk tracks read position: the fishbucket and CRC

Understanding file tracking is critical for troubleshooting duplicate data, missed data, and the side effects of clearing the fishbucket.

### 6.1 The fishbucket

The **fishbucket** is a BTrees-based database stored at `$SPLUNK_DB/fishbucket/` (typically `$SPLUNK_HOME/var/lib/splunk/fishbucket/`). For every file Splunk has ever monitored, it stores:

- **CRC fingerprint** — a hash of the first `initCrcLength` bytes of the file (default: first 256 bytes), used to uniquely identify the file's "identity"
- **seekAddress** — the byte offset up to which Splunk has already read (how far it has gotten)
- **seekCRC** — a CRC calculated at the current seek position, used to detect rotation/replacement

At each monitoring cycle, the monitor processor:
1. Computes the CRC of the first `initCrcLength` bytes of the file
2. Looks up that CRC in the fishbucket
3. If found, seeks to `seekAddress` and reads only new bytes
4. If not found (new file), starts from byte 0 (or end if `followTail = 1`) and creates a new entry

### 6.2 The CRC collision problem and `crcSalt`

If many files share **identical opening bytes** (e.g., many application log files that all start with the same standard header, banner, or schema line), they will have the same CRC fingerprint. The fishbucket cannot distinguish between them — one file's position record will be used for all.

The `crcSalt` attribute injects an additional value into the CRC calculation:

```ini
[monitor:///var/log/app/...]
index   = app
crcSalt = <SOURCE>
```

`crcSalt = <SOURCE>` (the literal string `<SOURCE>` including angle brackets) instructs Splunk to include the **full file path** in the CRC calculation. Since paths are unique, each file gets a unique fingerprint regardless of identical content at its opening bytes.

You can also set `crcSalt` to any arbitrary string value; `<SOURCE>` is the conventional choice and the one to use by default when identical headers are a concern.

```ini
# Without crcSalt: files with identical first 256 bytes collide in fishbucket
# With crcSalt = <SOURCE>: each file's path becomes part of its fingerprint
[monitor:///var/log/applogs/...]
index   = applogs
crcSalt = <SOURCE>
```

`initCrcLength` can also be increased to reduce collision probability by fingerprinting more bytes:

```ini
[monitor:///var/log/app/...]
initCrcLength = 512
```

This is useful when files differ only after the first 256 bytes but before byte 512.

### 6.3 Clearing the fishbucket

Deleting or clearing the fishbucket causes Splunk to treat all previously seen files as new. The monitor processor will re-read them from the beginning (unless `followTail = 1`). This is occasionally necessary during testing or when a misconfiguration has corrupted fishbucket state, but in production it will cause **duplicate indexing** of all monitored file content.

The fishbucket is at `$SPLUNK_HOME/var/lib/splunk/fishbucket/`. Delete the directory while Splunk is stopped, then restart. In the CLI:

```
splunk stop
rm -rf $SPLUNK_HOME/var/lib/splunk/fishbucket/
splunk start
```

You can also clean the entry for a single file using:

```
splunk clean inputstatus <source-path>
```

---

## 7. `batch` input — one-time destructive ingest

The `batch` input is for **one-time bulk ingestion of historical data**. It reads the file and then **deletes it from disk** after indexing. It does not tail; it reads once and removes.

```ini
[batch:///data/archive/old-logs/]
index       = archive
sourcetype  = syslog
move_policy = sinkhole
```

The `move_policy = sinkhole` attribute is **required** for batch inputs. It is the explicit declaration that you understand the file will be destroyed. Without it, the batch input will not function.

Use cases for `batch`:
- Loading multi-year archives onto a new Splunk deployment
- One-time import of historical data from a previous logging system
- Processing dump files that are produced once and should not persist

Key differences from `monitor`:

| Aspect | `monitor` | `batch` |
|---|---|---|
| Continuity | Continuous, tails indefinitely | One-shot |
| File retention | Non-destructive | Deletes file after read |
| Re-read | Tracks via fishbucket, won't re-read unless fishbucket cleared | N/A — file is gone |
| Use case | Live application/OS logs | Historical archives |

---

## 8. `oneshot` input — CLI one-time upload

`oneshot` is not a persistent `inputs.conf` stanza type; it is a **CLI command** that reads a single file once, indexes it, and does not persist a monitor entry. It is the simplest way to upload a static log file for ad hoc analysis.

```
splunk add oneshot /tmp/export.log -index testing -sourcetype csv
```

The equivalent through Splunk Web is **Settings → Add Data → Upload**. Neither creates a persistent `inputs.conf` entry, and neither modifies the fishbucket in a way that affects future monitoring.

---

## 9. The `inputs.conf` file: structure and location

Inputs are defined in `inputs.conf`, which follows the standard Splunk `.conf` format:

```
[stanza_name]
attribute = value
```

Input stanzas are evaluated under the **global (index-time) precedence** context (see the config-layering topic). The precedence order is: `system/local` > `apps/<app>/local` > `apps/<app>/default` > `system/default`.

On a Universal Forwarder, the most common practice is to create a dedicated app for each monitored technology and place `inputs.conf` in the app's `local/` directory:

```
$SPLUNK_HOME/etc/apps/uf_base_inputs/
├── local/
│   └── inputs.conf
└── metadata/
    └── local.meta
```

The app structure also makes it easy to deploy via Deployment Server — the entire app directory is pushed to target forwarders as a unit.

A minimal but complete `inputs.conf` for a production scenario:

```ini
# Monitor all OS auth logs, extract server name from path segment 4
[monitor:///data/servers/.../secure]
index        = os
sourcetype   = linux_secure
host_segment = 4
disabled     = false

# Monitor Apache logs for any server, only access.log files
[monitor:///var/log/apache/...]
index      = web
sourcetype = access_combined
allowlist  = access\.log$
host_regex = /servers?/(web\d+)/
crcSalt    = <SOURCE>
```

---

## 10. Applying input changes: restart vs. reload

Changes to `inputs.conf` take effect either by **restarting Splunk** or by using the REST reload endpoint:

- `splunk restart` — full restart; guaranteed to apply all config changes
- `splunk _internal call /services/data/inputs/monitor/_reload` — reloads monitor inputs without a full restart (works for most monitor changes in Splunk 9.x)
- `btool` — verify the effective configuration before restart: `splunk btool inputs list --debug`

For inputs running on a Universal Forwarder, after editing `inputs.conf` always restart the forwarder:

```
$SPLUNK_HOME/bin/splunk restart
```

---

## 11. Terminology & version notes

- **allowlist / denylist** — current names in Splunk 9.x. `whitelist` and `blacklist` remain as deprecated synonyms and still function in all 9.x releases, but new configs should use the current names.
- **fishbucket** — stable internal mechanism since early Splunk versions; the underlying store is BTrees; the location `$SPLUNK_HOME/var/lib/splunk/fishbucket/` is consistent across versions.
- **`recursive = true`** — the default in all current releases; no need to set it explicitly unless you want to disable it.
- **`followTail`** — has been in `inputs.conf` since at least Splunk 6.x and remains unchanged in 9.x.
- **`crcSalt = <SOURCE>`** — the `<SOURCE>` literal (including angle brackets) is the canonical value; not a variable reference — it is evaluated by the monitor processor as a special token.
- **Modular inputs** — introduced in Splunk 5.0; the recommended framework for building new technology-specific inputs as of Splunk 9.x. Scripted inputs predate them and remain supported but are considered legacy for new development.

---

## 12. Common misconceptions

- **"A monitor stanza monitors only the exact path in the stanza header."** Partially true for a single file. For a directory, it monitors the whole tree (unless `recursive = false`). With wildcards (`...`, `*`), the matched set can be large.
- **"`*` recursively searches directories."** No — `*` matches within a single path segment only. Use `...` for recursive traversal.
- **"If I delete a file, Splunk re-reads it when it comes back."** Not necessarily — if a new file with the same path but identical opening bytes appears, the fishbucket may match it to the previous entry and seek to the old position, skipping the beginning. Use `crcSalt = <SOURCE>` to prevent this.
- **"Clearing the fishbucket is safe in production."** It will re-index all monitored file content from the beginning, causing duplicate events. Only do this deliberately and after understanding the consequences.
- **"Setting `followTail = 1` means Splunk reads only new lines going forward, forever."** It means Splunk starts at the end of the file at the **first time it opens it**. After that, normal tailing applies. If the fishbucket is cleared, `followTail = 1` will again seek to the end rather than re-reading.
- **"`whitelist` is deprecated and broken."** It still works in Splunk 9.x. The attribute is accepted and functions identically to `allowlist`. But write new configs with the current name.
- **"Batch and monitor can be used interchangeably."** They cannot — `batch` is destructive, `monitor` is not. Using `batch` on live log files would delete them from disk.
- **"`host_regex` and `host_segment` can both be set."** They are mutually exclusive in a stanza. Only set one.

---

## 13. Mastery checklist — what you should be able to explain

- The seven major Splunk input families and when to use each.
- The complete attribute set for a `[monitor://]` stanza: `index`, `sourcetype`, `host`, `disabled`, `followTail`, `recursive`, `crcSalt`, `initCrcLength`.
- What `followTail = 1` does and when not to use it.
- The difference between monitoring a file and a directory; what `recursive` controls.
- The precise difference between `*` (single-segment) and `...` (multi-segment recursive) wildcards, with examples of what each matches and does not match.
- How `host_segment` derives a host from a path segment number, and when it fails.
- How `host_regex` uses a capturing group to extract host from a path, and why it handles variable-depth paths that `host_segment` cannot.
- Why `allowlist`/`denylist` are needed when monitoring broad paths; how the denylist takes precedence over the allowlist.
- The fishbucket's purpose, location, and the two things it stores per file (CRC fingerprint and seek address).
- The CRC collision problem: when it occurs, and how `crcSalt = <SOURCE>` solves it.
- When and how to clear the fishbucket (and why it is dangerous in production).
- The difference between `monitor` (continuous, non-destructive), `batch` (one-shot, destructive), and `oneshot` (CLI command, no persistent stanza).

---

## 14. Key terms (flashcard seeds)

- **`[monitor://<path>]`** — `inputs.conf` stanza that continuously tails a file or directory.
- **`index`** — destination index for events from this input stanza.
- **`sourcetype`** — event classification applied at input time.
- **`host`** — static host field; overridden by `host_regex` or `host_segment`.
- **`disabled`** — `true`/`1` to pause without removing the stanza.
- **`followTail`** — `1` = start at end of file on first open; `0` = start at beginning.
- **`recursive`** — `true` (default) = descend into subdirectories.
- **`*` wildcard** — matches within one path segment; does not cross `/`.
- **`...` wildcard** — matches zero or more path segments, crosses `/` recursively.
- **`host_segment`** — integer; sets host to the Nth `/`-delimited segment of the path.
- **`host_regex`** — regex with capturing group; extracts host from path; mutually exclusive with `host_segment`.
- **`allowlist` / `denylist`** — regex filters on full file path; denylist wins on conflict; replaces deprecated `whitelist` / `blacklist`.
- **fishbucket** — `$SPLUNK_HOME/var/lib/splunk/fishbucket/`; stores CRC fingerprint + seek offset per monitored file.
- **`crcSalt`** — salt for CRC calculation; `<SOURCE>` = include full path, ensuring unique fingerprints for files with identical headers.
- **`initCrcLength`** — bytes used for initial CRC (default 256); increase to reduce collision risk.
- **`batch`** — one-shot destructive ingest; requires `move_policy = sinkhole`; deletes file after read.
- **`oneshot`** — CLI command for single-file one-time indexing; no persistent stanza.

---

## 15. Questions to drill (quiz seeds)

1. Write a complete `inputs.conf` stanza that monitors all `.log` files anywhere under `/var/log/`, sends them to the `os` index with sourcetype `syslog`, and sets the host dynamically from the second path segment after `/var/log/`.
2. You have files at `/data/app/server1/app.log` and `/data/app/server1/logs/debug/app.log`. Write a single monitor stanza that captures both. What wildcard achieves this?
3. Explain why `/var/log/*/app.log` does NOT match `/var/log/app.log`. What change to the stanza path would make it match both?
4. Your environment has 50 application servers all writing log files that begin with the same 256-byte license header. Why does this cause a problem, and what `inputs.conf` attribute fixes it?
5. Describe what the fishbucket contains for a given monitored file, where it lives on disk, and what happens if you delete it while Splunk is running.
6. You want to monitor `/data/logs/` but exclude any `.gz` or `.bz2` compressed files. Write the appropriate `inputs.conf` attribute and value.
7. A file exists at `/data/servers/web/cluster-a/prod/host05/access.log`. You want `host = host05`. Would you use `host_segment` or `host_regex`? Write the stanza attribute.
8. What is the difference between `followTail = 1` and the fishbucket's normal seek behavior? Under what scenario would setting `followTail = 1` cause you to miss data?
9. Compare `monitor`, `batch`, and `oneshot` inputs across three dimensions: persistence, destructiveness, and primary use case.
10. You set both `allowlist` and `denylist` on the same stanza. A file matches both. What happens?
