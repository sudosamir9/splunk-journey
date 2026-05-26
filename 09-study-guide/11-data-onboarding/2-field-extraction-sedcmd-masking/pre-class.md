---
type: pre-class
theme: 11-data-onboarding
topic: 2-field-extraction-sedcmd-masking
covers: "Lectures 66–68"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/11-data-onboarding]
---

# Pre-class — Field Extraction, SEDCMD & Data Masking

> Read before the videos (covers lectures 66–68). ~4–5 min. This topic is where parsing configuration gets practical — extracting business fields from events and making sure sensitive data never reaches the index in clear text.

## Why this matters
Correct event boundaries and timestamps (topic 11.1) are necessary but not sufficient. What makes data *searchable and useful* is fields. Splunk gives you a choice: extract fields when data is written to the index (once, at cost, irreversibly) or when a user runs a search (every time, flexibly, at zero storage cost). Understanding when each approach is right — and how to configure both — is core admin knowledge. Add data masking, which *must* happen at index time, and you have the complete picture of how raw events become structured, policy-compliant data in Splunk.

## The mental model (hold these)
1. **Default is search-time — schema-on-read.** Splunk stores raw text. Fields are extracted from `_raw` at query time. Adding or changing a search-time extraction applies to all historical data for that sourcetype *immediately*, without touching the index. This is the correct default for the vast majority of fields.
2. **Three index-time reasons to go against the default:** data masking (must happen before storage), event routing (DEST_KEY = MetaData:Index), or a genuinely required index-level filter. Treat index-time as an exception, not a default.
3. **Three props.conf directives, three behaviors:**
   - `EXTRACT-<class>` — search-time, inline (no transforms.conf needed). Uses named capture groups `(?P<field>...)`.
   - `REPORT-<class>` — search-time, via a transforms.conf stanza. Good for reuse across multiple sourcetypes.
   - `TRANSFORMS-<class>` — index-time, via a transforms.conf stanza. Irreversible; only applies to data ingested after the config change.
4. **transforms.conf stanza anatomy:**
   - `REGEX` — the extraction or match pattern.
   - `FORMAT` — the field/value output; uses `$1`, `$2` for capture groups (not `\1`).
   - `DELIMS` — alternative to REGEX for simple ASCII delimiter-based search-time extraction.
   - `DEST_KEY` — where to write; controls what the transform does (field creation, metadata overwrite, raw rewrite, routing).
   - `WRITE_META = true` — appends an indexed field to `_meta`; safe when multiple transforms write indexed fields.
5. **SEDCMD in props.conf** applies a sed-like substitution to `_raw` at index time. Syntax: `s/regex/replacement/g`. Capture groups use `\1` (not `$1`). Simpler than a transforms stanza for single-stanza masking. Cannot target metadata fields.
6. **Two masking approaches — same result, different mechanism:**
   - SEDCMD: self-contained in props.conf; `\1` groups; slightly simpler.
   - `TRANSFORMS-` + `DEST_KEY = _raw`: props.conf references a transforms.conf stanza; `$1` groups; more flexible and reusable.
   Both rewrite `_raw` before the event is stored. Both are irreversible.

## Key terms (quick definitions)
- **EXTRACT-** — search-time inline extraction in props.conf; named group regex; no transforms.conf.
- **REPORT-** — search-time extraction in props.conf referencing a transforms.conf stanza.
- **TRANSFORMS-** — index-time extraction/transform in props.conf referencing a transforms.conf stanza.
- **DELIMS** — transforms.conf alternative to REGEX for ASCII-delimited search-time extraction.
- **FORMAT** — transforms.conf field/value output; `$1`/`$2` capture group references.
- **DEST_KEY** — transforms.conf destination: `_meta` (indexed field), `_raw` (rewrite), `MetaData:Host/Source/Sourcetype/Index`.
- **WRITE_META = true** — appends to indexed `_meta`; use this instead of DEST_KEY=_meta when multiple transforms write fields.
- **SEDCMD** — props.conf index-time sed-like substitution on `_raw`; `s/regex/replacement/g`; `\1` groups.
- **Data masking** — irreversible index-time rewrite of sensitive values in `_raw`; must validate before indexing real data.
- **App context scoping** — search-time knowledge objects are visible only within the app context they are saved in.

## Watch for this in the video
- When fields are extracted via the Field Extractor GUI, watch which app context is selected when saving — that determines where the `props.conf` EXTRACT stanza lands. Then observe that those fields are only visible when searching from that same app.
- In the SEDCMD lab, pay attention to the capture group structure: what is captured in group 1, what is kept, and what is replaced with literals. The `\1` syntax versus `$1` in FORMAT is a subtle but important distinction.
- The masking-via-transforms lab constructs `DEST_KEY = _raw` with a `FORMAT` that includes both literal replacement text and `$1` to re-insert preserved content. Note that the regex must match enough context to reconstruct the surrounding event text via capture groups.
- For both masking approaches: the config change requires deleting and re-ingesting data to see the effect on already-indexed events. That is the definition of an irreversible operation.

## Questions to hold in mind while watching
1. A field extraction is added to a sourcetype that already has six months of indexed data. Does the extraction apply retroactively? Does the answer change if it's a search-time extraction vs an index-time transform?
2. Why are search-time extractions scoped to an app context? What would you do to make them available globally?
3. When you use SEDCMD with `\1` to preserve a capture group, what happens to the rest of the match? What gets replaced?
4. If you need the same masking logic for three different sourcetypes, which approach — SEDCMD or TRANSFORMS — is easier to maintain?

## How this connects forward
- **ES / CIM normalization:** search-time EXTRACT and REPORT stanzas are exactly what Splunk Technology Add-ons use to normalize vendor-specific fields to CIM field names. Every TA you deploy to the search tier contains these in `props.conf`. Understanding the mechanism means you can troubleshoot when CIM fields are missing or wrong.
- **Deployment architecture:** EXTRACT/REPORT stanzas belong on **search heads** (search-time). TRANSFORMS- stanzas for masking and routing belong on the **parsing tier** (HF or indexer). The same `props.conf` file can contain both; Splunk applies the right ones on the right tier. In practice, package them separately in TAs — one deployed to the search tier, one to the parsing tier.
- **`btool` for troubleshooting:** `splunk btool props list <sourcetype> --debug` on the relevant tier shows which extraction stanzas are active and which file they came from — the correct first step when "why isn't this field appearing?" arises.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Configure advanced extractions with field transforms | https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Configureadvancedextractionswithfieldtransforms |
| Example field transform extraction configurations | https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Exampleconfigurationsusingfieldtransforms |
| Create custom fields at index time | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configureindex-timefieldextraction |
| Anonymize data (SEDCMD and masking) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Anonymizedata |
| transforms.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Transformsconf |
| props.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Propsconf |
