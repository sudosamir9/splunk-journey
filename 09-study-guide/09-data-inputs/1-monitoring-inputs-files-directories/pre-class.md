---
type: pre-class
theme: 09-data-inputs
topic: 1-monitoring-inputs-files-directories
covers: "Lectures 46–50"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/09-data-inputs]
---

# Pre-class — Data Inputs: Monitoring Files and Directories

> Read before the videos (covers lectures 46–50). ~4–5 min. The demos move fast through attributes and wildcards — walk in already holding the model so you can watch what's happening rather than trying to absorb vocabulary.

## Why this matters
Every event in Splunk arrived through a data input. The `monitor` input — which continuously tails files and directories — is the most widely deployed input type. Getting it right means knowing: which file, which index, what host, which files to skip, and how Splunk avoids re-indexing data it already read. Get any of these wrong and you'll have missing data, duplicate data, or miscategorized events — all silent failures that are painful to diagnose after the fact.

## The mental model (hold these)
1. **Inputs live in `inputs.conf` as `[monitor://<path>]` stanzas.** Attributes underneath set the destination (`index`, `sourcetype`, `host`). The stanza path can be a single file, a directory, or a wildcard expression.
2. **Two wildcards, two behaviors:**
   - `*` — matches within a single path segment; does not cross `/`. `/log/*/app.log` matches `/log/web/app.log` but not `/log/web/sub/app.log`.
   - `...` — crosses directory boundaries, matching zero or more segments recursively. `/log/.../app.log` matches `/log/app.log`, `/log/a/app.log`, `/log/a/b/app.log`, etc.
3. **`host_segment` vs `host_regex`** — when logs from multiple servers land on one machine, the hostname is wrong unless you extract it from the path. `host_segment = N` picks the Nth `/`-delimited segment. `host_regex` uses a regex capturing group for variable-depth paths. They are mutually exclusive.
4. **Allowlist/denylist filter which files within a broad path are monitored.** Both accept regexes matched against the full file path. If a file matches both, the denylist wins. Current names: `allowlist`/`denylist` (formerly `whitelist`/`blacklist` — deprecated but still functional in 9.x).
5. **The fishbucket prevents re-indexing.** For every monitored file, Splunk stores a CRC fingerprint of the first 256 bytes plus the byte offset already read. On each cycle it looks up the file's CRC, seeks to that offset, and reads only new bytes. If many files share identical first 256 bytes, their CRCs collide — fix this with `crcSalt = <SOURCE>`, which adds the full file path to the fingerprint.
6. **`monitor` is continuous and non-destructive. `batch` is one-shot and deletes the file after read.** `oneshot` is a CLI command for a single file, no persistent stanza.

## Key terms (quick definitions)
- **`[monitor://<path>]`** — stanza that continuously tails a file or directory tree.
- **`followTail`** — `1` = start at current end of file on first open; `0` = read from beginning.
- **`recursive`** — default `true`; set `false` to skip subdirectories.
- **`*`** — single-segment wildcard (no directory crossing).
- **`...`** — multi-segment recursive wildcard (crosses directory boundaries).
- **`host_segment`** — set host to the Nth path segment (integer).
- **`host_regex`** — regex with capturing group extracts host from path.
- **`allowlist` / `denylist`** — regex filters; denylist wins on conflict.
- **fishbucket** — database at `$SPLUNK_HOME/var/lib/splunk/fishbucket/`; stores CRC + seek offset per file.
- **`crcSalt = <SOURCE>`** — adds file path to CRC, prevents fingerprint collision on identical-header files.
- **`batch`** — one-shot, destructive; requires `move_policy = sinkhole`.

## Watch for this in the video
- The demo creates an app on the Universal Forwarder with `local/inputs.conf` — notice how the directory structure mirrors the config-layering model.
- Clearing the fishbucket mid-demo is deliberate; in production this causes duplicates — note *why* they do it (forcing a re-read of already-indexed data for demo purposes).
- The ellipsis (`...`) wildcard in action: watch how it matches files at different depths within the same monitor stanza.
- `host_segment` is shown first with a caveat (breaks when path depth varies), then `host_regex` is introduced as the fix.
- The allowlist demo uses a regex, not a glob — watch the capturing group construct that also feeds `host_regex`.

## Questions to hold in mind while watching
1. If a monitored directory contains 200 files and `allowlist = \.log$`, how many `inputs.conf` stanzas do you need?
2. When would `crcSalt = <SOURCE>` be essential versus just good hygiene?
3. What would happen if you deleted the fishbucket directory on a production indexer right now?
4. Why can't you use `*` to match `/var/log/.../app.log`?

## How this connects forward
- **Scripted inputs and HEC** (next topic) expand the input surface beyond files — the metadata model (`index`, `sourcetype`, `host`) is identical; only the delivery mechanism changes.
- **Data onboarding** (`props.conf`/`transforms.conf`) acts on the data *after* it's delivered by the input — sourcetype assignment here is the first thing props.conf looks up.
- **Deployment Server** — in production, `inputs.conf` inside an app is pushed to every forwarder by the Deployment Server; understanding the stanza model first makes that deployment model obvious.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| Monitor files and directories with inputs.conf | https://docs.splunk.com/Documentation/Splunk/latest/Data/Monitorfilesanddirectorieswithinputs.conf |
| Specify input paths with wildcards | https://docs.splunk.com/Documentation/Splunk/latest/Data/Specifyinputpathswithwildcards |
| Set a default host for a file or directory input | https://docs.splunk.com/Documentation/Splunk/latest/Data/Setadefaulthostforaninput |
| Include or exclude specific incoming data (allowlist/denylist) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Whitelistorblacklistspecificincomingdata |
| inputs.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf |
| How Splunk handles log file rotation (fishbucket) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Howlogfilerotationishandled |
