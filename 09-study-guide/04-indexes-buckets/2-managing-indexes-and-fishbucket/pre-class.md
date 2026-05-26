---
type: pre-class
theme: 04-indexes-buckets
topic: 2-managing-indexes-and-fishbucket
covers: "Lectures 25–28"
read_time: "~5 min"
tags: [study-guide/pre-class, theme/04-indexes-buckets]
---

# Pre-class — Managing Indexes & the Fishbucket

> Read before the lectures (covers lectures 25–28). ~5 min. These lectures cover practical index management and the fishbucket concept. The fishbucket section in particular moves fast and the concept is easy to misunderstand — walk in knowing what it is and what it is not.

## Why this matters

Creating indexes is a daily administrative task. Doing it incorrectly in a distributed or clustered environment causes configuration drift and broken replication. Data deletion has two methods with very different behaviors; picking the wrong one is a common and sometimes expensive mistake. The fishbucket is something every Splunk admin encounters eventually — usually when data goes missing or gets duplicated — and "what is the fishbucket and why did deleting it cause duplicates?" is a real production incident scenario.

## The mental model (hold these)

1. **Index creation writes a stanza to `indexes.conf` in a `local/` directory.** Via Splunk Web, the target directory is determined by the active app context (check the browser URL). Via CLI, it defaults to `system/local`. Direct file editing is the most controlled method. All three produce the same result.

2. **In a clustered environment, `indexes.conf` is managed on the cluster manager and pushed to peers — never edited directly on peers.** Clustered indexes also require `repFactor = auto` or data will not be replicated.

3. **Hot buckets cannot be safely file-copied while Splunk is running.** Warm and cold buckets (read-only, closed) are safe to back up. For hot buckets: use the `roll-hot-buckets` REST endpoint to force a hot→warm roll first, or stop Splunk, or use a filesystem snapshot.

4. **There are two ways to delete indexed data, and they are fundamentally different:**
   - **`| delete`** (SPL command) — marks events as unsearchable; data stays on disk; does not reclaim space; needs the `can_delete` role (not given to `admin` by default).
   - **`splunk clean eventdata -index <name>`** (CLI) — permanently destroys all data in an index; requires Splunk to be stopped; irreversible.

5. **The fishbucket is NOT a data bucket.** It is a checkpoint database that tracks how far Splunk has read into each monitored file. Its sole purpose is to prevent re-indexing already-ingested data. It stores three values per file: CRC (first 256 bytes of the file — its identifier), seekAddress (byte offset where reading last stopped), and seekCRC (fingerprint at that position).

6. **Deleting the fishbucket causes full re-ingestion of all monitored files.** Every file is treated as new; all content is re-sent to the indexer; duplicates appear. This is the key operational risk.

## Key terms (quick definitions)

- **`indexes.conf` stanza** — `[index_name]` with `homePath`, `coldPath`, `thawedPath`, retention attributes.
- **`repFactor = auto`** — required for a clustered index; enables bucket replication to peers.
- **Cluster manager** — distributes config bundles to peer nodes; formerly "master node" in older docs.
- **`| delete`** — SPL command; marks events unsearchable; requires `can_delete` role; no disk reclaim.
- **`can_delete` role** — Splunk built-in role with only the `delete_by_keyword` capability.
- **`splunk clean eventdata -index <name> -f`** — wipes all data from an index; Splunk must be stopped.
- **Fishbucket** — checkpoint DB for monitored file inputs; lives at `$SPLUNK_HOME/var/lib/splunk/fishbucket/`; no event data.
- **CRC** — hash of first 256 bytes; identifies the file in the fishbucket.
- **seekAddress** — byte offset of last read position; where Splunk resumes reading.
- **`crcSalt = <SOURCE>`** — literal value (not a placeholder) in `inputs.conf`; makes CRCs unique per file path.
- **`btprobe`** — CLI tool to inspect/reset fishbucket entries; Splunk must be stopped before use.
- **`splunk clean inputdata`** — wipes the entire fishbucket; causes full re-ingestion on next start.

## Watch for this in the video

- The lab creates an index via Splunk Web, then switches to the CLI. Notice the comment about which app context matters — this is the practical reason experienced admins create a dedicated admin app before making configuration changes.
- The backup section emphasizes "stop Splunk first, then copy, then start Splunk again." This is correct for hot buckets. The REST roll-hot-buckets approach is an alternative to stopping, but is not shown in the video — know it exists.
- For `splunk clean eventdata`, the video shows the `-f` flag and the stop-first requirement. The video also warns "if you don't specify index, all indexes will be deleted" — take this warning seriously.
- The fishbucket explanation uses the words "Sikh address" and "Sikh CRC" — these are the speaker's pronunciation of "seek address" and "seek CRC" (as in seek pointer, a file I/O term). Mentally substitute those terms.
- When the video refers to "CRC" of "the first 256 bytes," this is `initCrcLength` in `inputs.conf` — the default value of 256 is what the video is demonstrating.

## Questions to hold in mind while watching

1. When creating an index via Splunk Web, how would you verify which `indexes.conf` file the stanza was written to after saving?
2. If `| delete` does not remove data from disk, when does the disk space actually get freed?
3. The fishbucket stores a CRC of the first 256 bytes. What happens if two different log files on the same forwarder have identical first 256 bytes? How do you fix it?
4. Why does deleting the fishbucket cause duplicates rather than just missing data?

## How this connects forward

- **Data onboarding** (`props.conf`, `transforms.conf`) routes incoming events to specific indexes by name — you need to be able to create and manage indexes before routing data into them.
- **Indexer clustering** builds directly on the `repFactor`, cluster manager, and bundle-push workflow introduced here. In a clustered deployment, every index management operation goes through the manager.
- **Universal Forwarder deployment** heavily involves the fishbucket — understanding the CRC mechanism and `crcSalt` is essential for troubleshooting missed or duplicated data on monitored endpoints.
- **Capacity planning and retention** connect back to Topic 04.1 — the creation attributes (`frozenTimePeriodInSecs`, `maxTotalDataSizeMB`) you set when creating an index are the retention controls from that topic.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Create custom indexes | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes |
| Configure peer indexes in an indexer cluster | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Configurethepeerindexes |
| Back up indexed data | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Backupindexeddata |
| Remove indexes and indexed data | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/RemovedatafromSplunk |
| delete (SPL search command) | https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Delete |
| Splexicon: Fishbucket | https://docs.splunk.com/Splexicon:Fishbucket |
| How Splunk handles log file rotation | https://docs.splunk.com/Documentation/Splunk/latest/Data/Howlogfilerotationishandled |
| inputs.conf reference (crcSalt, initCrcLength, monitor stanza) | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf |
| Command-line tools for use with Support (btprobe) | https://docs.splunk.com/Documentation/Splunk/latest/Troubleshooting/CommandlinetoolsforusewithSupport |
