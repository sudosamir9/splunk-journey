# NBLM generation — Topic 07.2 · Routing, Load Balancing & Event Breaking

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk forwarder load balancing, event breaking, data routing, null-queue filtering, and UF vs HF`
- **KEY DISTINCTIONS:** `autoLBFrequency and autoLBVolume and how they interact; why large continuous files break load balancing (end-of-file / event boundary constraint); EVENT_BREAKER_ENABLE / EVENT_BREAKER on the UF vs LINE_BREAKER / SHOULD_LINEMERGE on the indexer — different components, different purposes, both needed; two routing mechanisms (_TCP_ROUTING for physical indexer routing vs _MetaData:Index for index assignment); nullQueue filtering — DEST_KEY=queue FORMAT=nullQueue, irreversible, license impact; intermediate forwarder tier — why UF by default, when HF is justified; useACK and why each hop needs it independently`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk forwarder load balancing, event breaking, data routing,
null-queue filtering, and the UF vs HF decision. Make sure to cover: how automatic load
balancing works — autoLBFrequency and autoLBVolume and how they interact (first threshold
wins); why large continuous files defeat time-based load balancing (the forwarder only
switches at event boundaries or end-of-file); how EVENT_BREAKER_ENABLE and EVENT_BREAKER
in props.conf on a UF solve this by activating a lightweight event-boundary detector before
forwarding, and why these are different from LINE_BREAKER / SHOULD_LINEMERGE which run on
the indexer's parsing pipeline; the two routing mechanisms — _TCP_ROUTING for physically
directing data to named indexer groups in outputs.conf versus _MetaData:Index in
transforms.conf for dynamically reassigning the destination index; how to drop events
permanently using nullQueue (DEST_KEY=queue, FORMAT=nullQueue) and the license implication
of doing this at the forwarder vs at the indexer; when to use an intermediate forwarder tier
and why UF is the correct default (free, raw, low overhead) while HF is only justified for
specific capabilities (data masking, content routing, HEC hosting); and indexer
acknowledgment (useACK) and why it must be enabled at each hop independently.

Walk through a worked configuration: a UF monitoring two log paths, routing them to
different indexer groups, filtering debug noise to nullQueue, and using EVENT_BREAKER for
clean load balancing. Call out the common confusions (event-boundary constraint on LB;
EVENT_BREAKER vs LINE_BREAKER; nullQueue irreversibility; _TCP_ROUTING vs _MetaData:Index).
Near the end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a
thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk load
balancing, event breaking, routing, and filtering at an administrator level. Mix recall
with scenario questions: a large file sticks to one indexer despite autoLBFrequency — what
is the cause and fix?; write the outputs.conf for two indexer groups with specific LB
settings; what is the difference between _TCP_ROUTING and _MetaData:Index?; write the
props.conf and transforms.conf stanzas to drop events matching a pattern; when is an HF
intermediate forwarder justified vs a UF?; what happens if useACK is only enabled on the
first hop of a three-tier deployment? Target: LB mechanics, event boundary constraint,
EVENT_BREAKER vs LINE_BREAKER, routing mechanisms, nullQueue pattern, UF vs HF decision.
Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk load balancing, event breaking, routing, and filtering. Front =
term/scenario; back = a tight rule or the exact config pattern. Include: autoLBFrequency and
autoLBVolume defaults and interaction; the event-boundary constraint on LB switching;
EVENT_BREAKER_ENABLE scope (UF only) vs LINE_BREAKER scope (indexer); _TCP_ROUTING usage in
inputs.conf vs _MetaData:Index in transforms.conf; the exact DEST_KEY / FORMAT pair for
nullQueue; intermediate forwarder UF vs HF decision criteria; useACK per-hop requirement.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
