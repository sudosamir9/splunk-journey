# NBLM generation — Topic 11.2 · Field Extraction, SEDCMD & Data Masking

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk field extraction, SEDCMD, and index-time data masking`
- **KEY DISTINCTIONS:** `search-time vs index-time extraction (schema-on-read default; index-time only for masking, routing, indexed fields); the three props.conf directives — EXTRACT- (inline, search-time), REPORT- (transforms.conf, search-time), TRANSFORMS- (transforms.conf, index-time); transforms.conf anatomy (REGEX, FORMAT with $1/$2, DELIMS, DEST_KEY, WRITE_META); SEDCMD syntax (s/// substitution with \1 groups, y/// transliterate, g flag) vs TRANSFORMS DEST_KEY=_raw masking; all DEST_KEY values (host, source, sourcetype, index routing, _meta, _raw); irreversibility of index-time changes; app context scoping of search-time extractions`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk field extraction at search time and index time, SEDCMD, and
data masking. Make sure to clearly explain: why search-time extraction is the default
(schema-on-read, retroactive, zero storage cost) and the three situations that justify
going index-time (masking, routing, indexed field creation); the three props.conf directives
— EXTRACT- (inline), REPORT- (via transforms.conf), TRANSFORMS- (index-time) — and what
separates them; the transforms.conf stanza anatomy: REGEX, FORMAT with $1/$2 capture
references, DELIMS for delimited data, DEST_KEY with all valid values (MetaData:Host,
MetaData:Source, MetaData:Sourcetype, MetaData:Index, _meta, _raw), and WRITE_META=true.

Go deep on SEDCMD: what it is, its two syntaxes (s/// and y///), the \1 capture group
syntax (and why it differs from the $1 in transforms.conf FORMAT), and its limitation to
_raw only. Then contrast it with the TRANSFORMS + DEST_KEY=_raw approach to masking —
same end result, different mechanism — and walk through the decision criteria for choosing
one over the other. Emphasize irreversibility: once data is in the index, masking cannot
be applied retroactively.

Include a worked end-to-end example that shows props.conf + transforms.conf for both
extraction and masking on the same sourcetype. Call out common errors (wrong capture group
syntax, TRANSFORMS- applying only to new data, app context scoping of search-time
extractions). Near the end, pose a few drill questions. Energetic and conversational, but
dense and precise — this is learning, not entertainment. Aim for a thorough episode of
roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk field
extraction, SEDCMD, and data masking at an administrator level. Mix recall with scenario
questions: given a raw event and a desired set of fields, write the EXTRACT or REPORT
stanza; given a sensitive data pattern, write a SEDCMD or TRANSFORMS masking config;
EXTRACT vs REPORT vs TRANSFORMS — which runs when?; DEST_KEY scenarios — which value
routes an event to a different index?; a new masking transform is deployed — which data
does it apply to?; a search-time extraction works in one app but not another — why?
Target: the three directives, transforms.conf anatomy, SEDCMD syntax, DEST_KEY values,
capture group references (\1 vs $1), irreversibility, app context scoping. Explain each
answer.
```

## Flashcards
```
Make flashcards on Splunk field extraction, SEDCMD, and data masking. Front = term or
scenario; back = the rule, syntax, or behavior. Include: EXTRACT- vs REPORT- vs
TRANSFORMS- (when each runs); DELIMS and its limitation; FORMAT $1/$2 syntax; all
DEST_KEY values; WRITE_META=true vs DEST_KEY=_meta; SEDCMD s/// syntax; \1 vs $1 capture
group references; search-time retroactivity vs index-time only-new-data; app context
scoping; irreversibility of masking.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
