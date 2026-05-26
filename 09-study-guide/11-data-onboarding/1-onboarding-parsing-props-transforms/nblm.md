# NBLM generation — Topic 11.1 · Data Onboarding, Parsing, props.conf & Transforms

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk data onboarding workflow, index-time parsing, and props.conf`
- **KEY DISTINCTIONS:** `the four-phase onboarding workflow (discover → check Splunkbase → configure parsing → validate); sourcetype as the key parsing selector and why input-time assignment beats props; parsing runs on HF or indexer, not the UF; the eight core index-time parsing settings (SHOULD_LINEMERGE, LINE_BREAKER, BREAK_ONLY_BEFORE, MUST_BREAK_AFTER, TRUNCATE, TIME_PREFIX, TIME_FORMAT, MAX_TIMESTAMP_LOOKAHEAD, TZ); why LINE_BREAKER + SHOULD_LINEMERGE=false is preferred over line merging; how TIME_PREFIX and TIME_FORMAT work together to locate and parse timestamps; using Data Preview to validate event boundaries and _time before indexing; PCRE fundamentals (named groups, non-greedy, lookaheads); index-time changes are irreversible`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk data onboarding and index-time parsing. Make sure to clearly
explain: the four-phase onboarding workflow and why each step exists; why sourcetype is the
primary parsing selector and why setting it at the input is preferred; why the Universal
Forwarder does not parse data and what that means for where props.conf must live in a
distributed deployment; the full event-parsing pipeline in order; and all eight core
index-time parsing settings — SHOULD_LINEMERGE, LINE_BREAKER, BREAK_ONLY_BEFORE,
MUST_BREAK_AFTER, TRUNCATE, TIME_PREFIX, TIME_FORMAT, MAX_TIMESTAMP_LOOKAHEAD, and TZ —
what each does, its default value, and a concrete example of when to change it.

Go deep on LINE_BREAKER vs the SHOULD_LINEMERGE merging approach: why is LINE_BREAKER +
SHOULD_LINEMERGE=false faster, and when would BREAK_ONLY_BEFORE still be the right tool?
Walk through a worked example of TIME_PREFIX + TIME_FORMAT + MAX_TIMESTAMP_LOOKAHEAD
working together to extract a timestamp from a mid-event JSON field. Explain the consequences
of getting index-time parsing wrong — and why Data Preview exists as the validation step
before committing data.

Near the end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a thorough
episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk data
onboarding and index-time parsing at an administrator level. Mix recall with scenario
questions: given a specific log format, which props.conf settings do you need and why?;
TIME_PREFIX + TIME_FORMAT — trace through a raw event and show exactly where _time comes
from; SHOULD_LINEMERGE=true vs LINE_BREAKER approach — when does each apply?; a UF is
sending data directly to indexers — where does the parsing props.conf stanza live?;
sourcetype is set in both inputs.conf and props.conf — which wins? Target: the eight
parsing settings, the parsing pipeline, sourcetype precedence, Data Preview purpose,
irreversibility of index-time changes. Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk data onboarding and index-time parsing. Front = term or scenario;
back = a tight rule, default value, or config pattern. Include: all eight core parsing
settings with default values; the LINE_BREAKER vs SHOULD_LINEMERGE tradeoff; where parsing
runs (not the UF); TIME_PREFIX + TIME_FORMAT interaction; what happens if TIME_PREFIX doesn't
match; TZ and when it applies; Data Preview purpose; named-group regex syntax; non-greedy
quantifier syntax.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
