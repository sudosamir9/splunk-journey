---
type: pre-class
theme: 04-indexes-buckets
topic: 1-indexes-and-bucket-lifecycle
covers: "Lectures 22–24"
read_time: "~5 min"
tags: [study-guide/pre-class, theme/04-indexes-buckets]
---

# Pre-class — Indexes & Bucket Lifecycle

> Read before the lectures (covers lectures 22–24). ~5 min. The videos move quickly through the physical layout and lifecycle triggers. Walk in already holding the mental model so you can track the details rather than rebuild the framework from scratch mid-video.

## Why this matters

Every operational question about data in Splunk — "where did my data go?", "why is that search slow?", "how much disk do I need?" — traces back to how indexes are physically stored and how Splunk ages data through the bucket lifecycle. Retention misconfiguration is one of the most common causes of unexpected data loss in production, and the fix always requires understanding what triggered a freeze.

## The mental model (hold these)

1. **An index is a directory tree of time-partitioned buckets, not a flat file or a table.** The directory `$SPLUNK_HOME/var/lib/splunk/<index_name>/` is the physical index. All its data lives in subdirectories called buckets, each holding a compressed time slice.

2. **Three directories; four live states:**
   - `db/` (the `homePath`) holds **hot** (actively written) and **warm** (recently closed) buckets — both live here.
   - `colddb/` (the `coldPath`) holds **cold** buckets — aged out of `db/`, still fully searchable.
   - `thaweddb/` holds **thawed** buckets — manually restored archive data; Splunk never auto-manages it.
   - **Frozen** is not a directory — it means the bucket was removed (deleted or archived externally).

3. **The lifecycle flows in one direction: hot → warm → cold → frozen.** Each transition is triggered by specific thresholds in `indexes.conf`. Warm and cold are both read-only and fully searchable. Frozen is gone (unless you configured `coldToFrozenDir`).

4. **Two types of retention limits, both active simultaneously:** Time-based (`frozenTimePeriodInSecs`) and size-based (`maxTotalDataSizeMB`). Whichever fires first wins. You must plan both — setting only time-based retention is a common mistake.

5. **Bucket names encode time.** Warm and cold buckets are named `db_<latest_epoch>_<earliest_epoch>_<id>`. Splunk uses these timestamps to skip entire buckets during time-scoped searches. A search without time bounds reads every bucket.

6. **On-disk size ≈ 50% of ingested volume.** Raw data is compressed; TSIDX search-acceleration files add back some size. Use 50% as the starting estimate for storage planning.

## Key terms (quick definitions)

- **Index** — logical data store; physically a set of bucket directories under `$SPLUNK_DB`.
- **Bucket** — directory containing one time slice of an index: compressed raw data + tsidx + metadata.
- **Hot** — actively written to; R/W; lives in `db/`; named `hot_v1_<guid>`.
- **Warm** — closed for writing; R/O; still in `db/`; named `db_<latest>_<earliest>_<id>`.
- **Cold** — moved to `colddb/`; R/O; same name as warm.
- **Frozen** — removed from the index; deleted by default; archived if `coldToFrozenDir` configured.
- **Thawed** — frozen data manually restored to `thaweddb/`; searchable; never auto-aged.
- **`frozenTimePeriodInSecs`** — time-based retention; requires restart to change.
- **`maxTotalDataSizeMB`** — size-based limit; oldest data freezes first when exceeded.
- **TSIDX** — time-series index file; enables fast field search without reading raw data.
- **Events index / Metrics index** — two non-interconvertible index types; `metric` is for numeric time-series only.

## Watch for this in the video

- The demo walks `$SPLUNK_HOME/var/lib/splunk/_internal/` on disk. Notice the `db/` directory contains both hot and warm buckets — they are not in separate directories.
- The video uses the terms "hot pocket" and "warm pocket" — mentally substitute "hot bucket" and "warm bucket" (the correct terminology in current Splunk documentation).
- When the video shows `indexes.conf` stanzas, pay attention to which attribute controls which transition trigger. The most important are `maxHotBuckets` (hot→warm), `maxWarmDBCount` (warm→cold), `frozenTimePeriodInSecs` and `maxTotalDataSizeMB` (cold→frozen).
- The video mentions that data goes "to bin" (deleted) when no frozen path is configured — this is correct; the default behavior on freezing is deletion.
- The video shows `$SPLUNK_DB` in `splunk-launch.conf`. This is how you redirect all index storage to a different disk.

## Questions to hold in mind while watching

1. If both hot and warm buckets are in `db/`, how can you tell them apart by name?
2. What is the difference between `homePath.maxDataSizeMB` (which causes warm→cold) and `maxTotalDataSizeMB` (which causes cold→frozen)?
3. If `frozenTimePeriodInSecs` is set to 180 days but `maxTotalDataSizeMB` is too small, what actually happens?
4. Why would an admin put `coldPath` on a different, slower disk than `homePath`?

## How this connects forward

- **Topic 04.2** covers how to create and manage indexes (CLI, Web, distributed clusters), how to delete data from indexes, and the fishbucket — the checkpoint system for monitored file inputs.
- **Data onboarding** (`props.conf`/`transforms.conf`) will reference index names constantly — you need to know what an index is before you can route data into one.
- **Indexer clustering** adds replication factor (RF) and search factor (SF) to the bucket model — each bucket gets replicated across peers. The lifecycle is the same; the mechanics add cluster-aware triggering.
- **Capacity planning** for any deployment starts with the 50% sizing rule and the retention window covered here.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| How the indexer stores indexes (bucket layout, naming, lifecycle) | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/HowSplunkstoresindexes |
| Set a retirement and archiving policy | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setaretirementandarchivingpolicy |
| indexes.conf reference (all attributes) | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Indexesconf |
| Configure index storage (homePath, coldPath, volumes) | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Configureindexstorage |
| Configure maximum index size | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Configureindexstoragesize |
| Estimate storage requirements (50% rule) | https://docs.splunk.com/Documentation/Splunk/latest/Capacity/Estimateyourstoragerequirements |
| About managing indexes | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Aboutmanagingindexes |
| Create custom indexes | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes |
