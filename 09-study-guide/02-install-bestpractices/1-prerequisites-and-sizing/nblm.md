# NBLM generation — Topic 02.1 · Prerequisites & Sizing

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk deployment prerequisites and capacity planning`
- **KEY DISTINCTIONS:** `the three sizing dimensions (ingest volume vs search load vs retention) and what each drives; why IOPS matters more than raw capacity for indexers; reference hardware (12 cores/12 GB) and Splunk Validated Architectures; trial vs free license limits; the storage formula (volume × retention × ~0.5 × replication factor)`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk deployment prerequisites and capacity planning. Prioritize
understanding and the trade-offs an admin makes. Make sure to clearly explain the three sizing
dimensions (ingest volume vs search load vs retention) and what each drives; why storage IOPS
matters more than raw capacity for indexers; reference hardware (12 cores / 12 GB) and Splunk
Validated Architectures; trial vs free license limits; and the storage sizing formula
(daily volume × retention × ~0.5 × replication factor).

Keep it concrete — walk through a worked sizing example (e.g. 300 GB/day, 90-day retention,
RF 2). Call out common misconceptions (capacity vs IOPS; "ingest volume is all that matters").
Near the end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a
thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk deployment
prerequisites and capacity planning at an administrator level. Mix recall with sizing/scenario
questions (given X GB/day, Y retention, RF Z, estimate storage and indexer count). Target the
easily-confused points: IOPS vs capacity, the three sizing dimensions, trial vs free license
limits, reference hardware, and key ports (8000/8089/9997/8088/8191). Explain each answer.
```

## Flashcards
```
Make flashcards from the key terms and must-know facts on Splunk prerequisites and sizing.
Front = term/port/limit or scenario; back = a tight, precise definition or value. Include
port-to-purpose cards and the license-limit and reference-hardware numbers.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
