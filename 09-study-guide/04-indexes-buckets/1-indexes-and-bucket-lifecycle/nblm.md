# NBLM generation — Topic 04.1 · Indexes & Bucket Lifecycle

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk indexes and the bucket lifecycle`
- **KEY DISTINCTIONS:** `what an index is (logical store; physical bucket directories); events vs metrics index types (non-interconvertible); internal indexes and their purposes (_internal, _audit, _introspection, _thefishbucket, main); the three on-disk directories (db/, colddb/, thaweddb/) and which states they hold; what is inside a bucket (rawdata/journal.gz, tsidx, cidx, metadata); bucket naming with embedded epoch timestamps and search optimization; all five states (hot/warm/cold/frozen/thawed) and the exact indexes.conf triggers for each transition; why hot and warm both live in db/; frozen = deleted by default unless coldToFrozenDir configured; thawed = manually restored, never auto-managed; frozenTimePeriodInSecs vs maxTotalDataSizeMB (whichever fires first wins); the 50% on-disk sizing rule`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk indexes and the bucket lifecycle. Go deep on: what an index
actually is on disk (directory of time-partitioned buckets); the difference between an events
index and a metrics index and why the type cannot be changed after creation; the built-in
internal indexes (_internal, _audit, _introspection, _thefishbucket, main) and the distinct
purpose of each; the three canonical subdirectories (db/ for hot and warm, colddb/ for cold,
thaweddb/ for thawed) and why hot and warm share the same directory; what is physically
inside a bucket (rawdata/journal.gz, tsidx files, cidx bloom filters, metadata); how bucket
naming embeds epoch timestamps and how Splunk uses those for time-range search optimization;
the full lifecycle — hot → warm → cold → frozen → (deleted or archived) → thawed — with the
specific indexes.conf attributes that trigger each transition (maxHotBuckets, maxDataSize,
maxHotSpanSecs for hot→warm; maxWarmDBCount and homePath.maxDataSizeMB for warm→cold;
frozenTimePeriodInSecs and maxTotalDataSizeMB for cold→frozen); why frozen means deleted by
default and what coldToFrozenDir/coldToFrozenScript change about that; why thawed buckets
are never auto-managed; the interaction between time-based and size-based retention (whichever
fires first wins) and the classic mistake of setting only time-based retention; the 50% on-disk
sizing rule and where it comes from; and that frozenTimePeriodInSecs changes require a restart.

Keep it concrete — walk through a realistic sizing example (90-day retention, 50 GB/day
ingest) and derive the correct indexes.conf values. Call out the most common operational
mistakes: not setting maxTotalDataSizeMB, assuming frozen = still somewhere on disk, expecting
a reload to apply frozenTimePeriodInSecs changes. Near the end, pose a few of the drill
questions so the listener can self-check. Energetic and conversational, but dense and precise —
this is learning, not entertainment. Aim for a thorough episode of roughly 25–30 minutes —
go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk indexes and
the bucket lifecycle at an administrator level. Mix recall with scenario questions — for
example: given an indexes.conf stanza with specific frozenTimePeriodInSecs and maxTotalDataSizeMB
values plus a known ingest rate, predict which limit fires first; identify which directory
holds a bucket in a given state; trace what happens step by step when a hot bucket rolls;
explain why a search with no time bounds is slower than a time-scoped one in terms of bucket
mechanics. Target: bucket state definitions, the transition triggers, the three directory paths,
frozen vs thawed behavior, size-vs-time retention interaction, and the 50% sizing rule. Explain
each answer in full.
```

## Flashcards
```
Make flashcards on Splunk indexes and the bucket lifecycle. Front = term or scenario; back =
a tight definition or rule. Include: the five bucket states and their key properties; which
directory each state lives in; the indexes.conf attributes triggering each transition; the
difference between frozenTimePeriodInSecs (time-based, restart required) and maxTotalDataSizeMB
(size-based); what happens to frozen data by default vs with coldToFrozenDir; why thawed
buckets are never auto-managed; the 50% sizing rule; the events vs metrics index distinction.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
