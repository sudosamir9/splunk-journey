# NBLM generation — Topic 07.1 · Data Collection Methods, Metadata Fields & Sourcetypes

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk data collection methods, default metadata fields, and why sourcetype is the most important field`
- **KEY DISTINCTIONS:** `the four pipeline stages (input / parsing / indexing / search) and which component performs each; the six collection methods (monitor, TCP/UDP, HEC, scripted, modular, Windows) and when to choose each; the four primary default metadata fields (host, source, sourcetype, index) and where each is assigned in the pipeline; why _time is assigned at parse time not input time; why sourcetype is the lookup key for all props.conf rules (line breaking, timestamp extraction, field extractions, CIM mappings) and the cascading consequences of getting it wrong; automatic recognition vs explicit assignment; the vendor:product naming convention and its relationship to Technology Add-on CIM mappings`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk data collection methods, default metadata fields, and the
critical importance of sourcetype. Make sure to cover: the four pipeline stages (input,
parsing, indexing, search) and which component — forwarder vs indexer vs search head —
handles each; the six collection methods (monitor inputs, TCP/UDP network inputs, HEC,
scripted, modular, Windows-specific) with enough depth to understand when you'd choose each
one; the four primary default metadata fields (host, source, sourcetype, index) and
precisely where in the pipeline each is assigned, including why _time is NOT assigned by the
forwarder but is extracted from event text at the parsing stage; and why sourcetype is the
single most important field — it is the lookup key for all props.conf rules, which means
wrong sourcetype breaks line breaking, timestamp extraction, field extractions, and CIM
mappings simultaneously, all silently.

Be concrete: walk through what happens step-by-step when a UF monitors /var/log/secure,
sends blocks to an indexer, and the indexer tries to break events and extract timestamps.
Trace the failure path when the sourcetype is wrong. Explain the automatic recognition
fallback and why explicit assignment is always required for production onboarding. Cover the
vendor:product naming convention and why it matters for Technology Add-on CIM mappings.
Near the end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a
thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk data
collection, default metadata fields, and sourcetype at an administrator level. Mix recall
with scenario questions: given a specific input scenario (syslog relay, HEC push, file
monitor), what does each metadata field contain and why?; trace the failure path when
sourcetype is wrong; which pipeline stage assigns which fields?; what breaks when
LINE_BREAKER is not configured for a custom sourcetype?. Target: pipeline stages vs
component mapping, host override scenarios, sourcetype as props.conf key, automatic
recognition limitations, CIM naming conventions. Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk data collection, default metadata fields, and sourcetype. Front =
term/scenario; back = a tight rule or ordering. Include: the four pipeline stages and which
component handles each; when _time is assigned and why; the six input methods and their
stanza prefixes; the host/source/sourcetype/index assignment point; what sourcetype controls
in props.conf; why explicit sourcetype assignment beats automatic recognition; the
vendor:product naming convention and its CIM implication.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
