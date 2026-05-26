---
type: pre-class
theme: 11-data-onboarding
topic: 1-onboarding-parsing-props-transforms
covers: "Lectures 62–65"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/11-data-onboarding]
---

# Pre-class — Data Onboarding, Parsing, props.conf

> Read before the videos (covers lectures 62–65). ~4–5 min. Index-time parsing is irreversible — the decisions you make in `props.conf` before data lands in a bucket cannot be undone without deleting and re-indexing. Walk in holding the model.

## Why this matters
When raw bytes arrive at Splunk's parsing tier, the platform must answer two questions before it can write a single event: *where does this event start and end?* and *what time does it represent?* Both answers come from `props.conf`, applied at index time. Get them wrong and you have either unreadable blobs, or events whose `_time` field is wrong — and you cannot fix it without touching the index. This is the topic where knowing what you're doing before you write a config saves you hours of remediation.

## The mental model (hold these)
1. **Data onboarding is a four-phase workflow:** discover and document sources → check Splunkbase for an add-on → configure parsing → validate with Data Preview before indexing. Each phase has a reason; skipping one creates problems later.
2. **Parsing happens on the parsing tier, not the Universal Forwarder.** The UF passes raw bytes. Parsing runs on the Heavy Forwarder (if deployed) or the indexer. Put `props.conf` parsing config on that tier.
3. **Sourcetype is the key.** It controls which `props.conf` stanzas apply. Set it at the input (`inputs.conf`) when possible. If set at the input, it cannot be overridden in `props.conf`.
4. **The eight core index-time parsing settings (the "Great 8")** in `props.conf`:
   - `SHOULD_LINEMERGE` — default `true` (merge lines); best practice: set to `false` and use `LINE_BREAKER` instead (faster).
   - `LINE_BREAKER` — regex that defines event boundaries in the raw data stream; the match is consumed.
   - `BREAK_ONLY_BEFORE` / `MUST_BREAK_AFTER` — merge-mode settings; start or end a multi-line event at a matching line.
   - `TRUNCATE` — max event size in bytes; default 10,000.
   - `TIME_PREFIX` — regex that positions Splunk's timestamp search; time extraction starts after the match.
   - `TIME_FORMAT` — strptime format string describing the exact timestamp layout.
   - `MAX_TIMESTAMP_LOOKAHEAD` — character count Splunk searches for the timestamp after TIME_PREFIX; default 128.
   - `TZ` — assumed timezone for events without an embedded one.
5. **TIME_PREFIX positions, TIME_FORMAT parses.** They work together: TIME_PREFIX moves the cursor to just before the timestamp; TIME_FORMAT tells Splunk exactly how to read what follows. If TIME_PREFIX doesn't match, no timestamp is extracted and `_time` defaults to receipt time.
6. **Data Preview lets you validate before committing.** Upload a sample, adjust settings interactively, watch event boundaries and timestamps update in real time. Save the sourcetype — that writes the `props.conf` stanza. Only then index real data.

## Key terms (quick definitions)
- **Sourcetype** — metadata field controlling all parsing; set at input, in props, or auto-detected; input wins.
- **props.conf** — parsing control file; stanzas: `[<sourcetype>]`, `[source::<glob>]`, `[host::<value>]`.
- **Parsing tier** — HF or indexer; where props.conf runs; NOT the UF.
- **LINE_BREAKER** — regex defining event start boundaries; default `([\r\n]+)` = one line per event.
- **SHOULD_LINEMERGE** — legacy line-merge control; set to `false` when using LINE_BREAKER.
- **TIME_PREFIX** — regex to locate timestamp start position.
- **TIME_FORMAT** — strptime string; e.g., `%Y-%m-%dT%H:%M:%S` for ISO 8601.
- **TZ** — IANA timezone name or UTC offset applied when event has no embedded timezone.
- **Data Preview** — interactive parsing validator in Add Data → Set Source Type; no data is indexed until you proceed.
- **PCRE** — Splunk's regex engine; key constructs: `(?P<name>...)` named groups, `.*?` non-greedy, `(?=...)` lookahead.

## Watch for this in the video
- The workflow opens with a data discovery checklist — notice it asks about data location, volume, retention, and PII *before* touching Splunk. This is a real pre-engagement pattern.
- Pay attention to when `SHOULD_LINEMERGE` is set to `false` and `LINE_BREAKER` is adjusted — observe the event boundary change in the preview pane in real time.
- Watch how `TIME_PREFIX` and `TIME_FORMAT` are built together: TIME_PREFIX narrows where to look, TIME_FORMAT tells Splunk what the timestamp looks like once found. The `MAX_TIMESTAMP_LOOKAHEAD` count is then set to match the character length of the actual timestamp.
- The Data Preview workflow ends with "Save source type" — notice that this writes the config to the app context you select, not globally.

## Questions to hold in mind while watching
1. The parsing settings are applied at index time. What are the consequences of discovering a misconfiguration one week after data was indexed?
2. When would you choose `SHOULD_LINEMERGE = true` + `BREAK_ONLY_BEFORE` over `SHOULD_LINEMERGE = false` + `LINE_BREAKER`?
3. If `TIME_PREFIX` doesn't match anything in the event, what does `_time` show?
4. Why does the Universal Forwarder not parse data, and how does that affect where you deploy `props.conf`?

## How this connects forward
- **Topic 11.2** (field extraction, SEDCMD, masking) is the direct continuation — once events are correctly broken and timestamped, the next step is extracting fields and, where required, masking sensitive data. Both operate via `props.conf` and `transforms.conf`.
- **Deployment Server / Cluster Manager** (from the distributed deployment theme): parsing config ships as an app bundle pushed to HFs via DS, or to indexer peers via the CM. The config you write here needs to land on the parsing tier, which determines how it's deployed.
- **`btool`** (from the config layering theme): `splunk btool props list <sourcetype> --debug` shows you the effective merged parsing config and which file each setting came from — the correct tool for diagnosing "why isn't my timestamp being extracted?"

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Configure event line breaking | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configureeventlinebreaking |
| Configure timestamp recognition | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configuretimestamprecognition |
| props.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Propsconf |
| Assign sourcetypes | https://docs.splunk.com/Documentation/Splunk/latest/Data/Setsourcetype |
| Why source types matter | https://docs.splunk.com/Documentation/Splunk/latest/Data/Whysourcetypesmatter |
| Configure timestamp assignment (multiple timestamps) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configurepositionaltimestampextraction |
