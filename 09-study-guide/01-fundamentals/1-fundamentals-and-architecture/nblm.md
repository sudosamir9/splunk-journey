# NBLM generation — Topic 01.1 · Fundamentals & Architecture

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots used below:
- **TOPIC NAME:** `Splunk fundamentals & architecture`
- **KEY DISTINCTIONS:** `the data pipeline Input→Parsing→Indexing→Search and which component/config file owns each; UF vs HF and cooked vs uncooked; index-time vs search-time; Deployment Server vs SHC Deployer vs Cluster Manager Node`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk fundamentals & architecture. Prioritize understanding and the
trade-offs an admin makes, not just definitions. Make sure to clearly explain the data
pipeline (Input→Parsing→Indexing→Search) and which component and config file owns each
segment; UF vs HF and cooked vs uncooked data; index-time vs search-time processing; and the
difference between the Deployment Server, the SHC Deployer, and the Cluster Manager Node.

Keep it concrete — walk through the life of a single event from source to search. Call out
common misconceptions and the legacy-vs-current terminology (master → manager node). Near the
end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a
thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk fundamentals
& architecture at an administrator level. Mix recall with scenario questions. Deliberately
target the easily-confused points: which component parses (and which never does), UF vs HF /
cooked vs uncooked, index-time vs search-time, and Deployment Server vs SHC Deployer vs Cluster
Manager Node. Assume I already know SPL. Explain why each answer is right and the others wrong.
```

## Flashcards
```
Make flashcards from the key terms and must-know distinctions in this material on Splunk
fundamentals & architecture. Front = term or scenario; back = a tight, precise definition
or rule. Include "which component / which config file / index-time vs search-time" cards.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
