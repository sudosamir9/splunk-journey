---
type: enhanced
theme: 11-data-onboarding
topic: 1-onboarding-parsing-props-transforms
covers: "Lectures 62–65"
tags: [study-guide/enhanced, theme/11-data-onboarding]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Data Onboarding, Parsing, props.conf & Transforms

> Deep reference on the full data onboarding workflow: how to identify and categorize a data source, assign a sourcetype, control event line breaking and timestamp recognition at parse time via `props.conf`, validate the result with Data Preview before committing to an index, and where regex fits in the whole picture. These settings — and the discipline of getting them right before data lands in an index — are the foundation of every Splunk deployment that produces reliable search results. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Getting data into Splunk is not just a plumbing problem. When raw bytes arrive at the parsing tier, Splunk must make a series of decisions — where does one event end and the next begin? What time does each event represent? What is the data? Those decisions are controlled by `props.conf`, applied at parse time, and they are **irreversible once data lands in an index**. Understanding the onboarding workflow and the key parsing controls saves you from the two most common admin failures: events that are broken incorrectly (unreadable multi-line blobs, or single lines split into thousands of micro-events) and events whose `_time` field is wrong (searches that return nothing, or retention that expires too early/late).

---

## 1. The data onboarding workflow

Data onboarding should be treated as a structured process, not an ad-hoc upload. The workflow has four phases:

### 1.1 Discover and document the sources

Before touching Splunk, gather the following for every data source:

| Question | Why it matters |
|---|---|
| What produces the data? (application, appliance, OS agent, syslog relay, API) | Determines collection method and whether an existing add-on exists |
| Where does the data reside? (flat file, network socket, Windows event log, HTTP endpoint) | Determines which input type to use (`monitor`, `tcp`/`udp`, `wineventlog`, `modular input`) |
| What is the expected volume and velocity? | Capacity planning for the parsing tier |
| What are the retention requirements? | Index selection and `frozenTimePeriodInSecs` in `indexes.conf` |
| Are there PII or sensitive fields (card numbers, SSNs)? | Triggers masking requirement before indexing |

### 1.2 Check Splunkbase for an existing add-on

Before writing any `props.conf` from scratch, check Splunkbase. A Technology Add-on (TA) from a vendor or the Splunk community bundles all the parsing configuration (sourcetype definitions, field extractions, timestamp patterns, CIM normalization) for the specific data source. Using a TA saves significant time and aligns your data with the Common Information Model for use with ES and other premium apps.

Only when no suitable add-on exists — or when the data is proprietary/custom — should you configure parsing manually.

### 1.3 Configure parsing — the subject of the rest of this note

This is where `props.conf` and `transforms.conf` come in. The parsing tier reads the raw data stream and applies the controls you specify to produce indexed, time-stamped events.

### 1.4 Validate with Data Preview before indexing

Always use Data Preview (covered in §9 below) to confirm event breaking and timestamps look correct on a sample before committing data to the index. Index-time changes cannot be undone without re-indexing.

---

## 2. The parsing tier — where props.conf runs

**Index-time parsing** happens on the tier that receives raw data and prepares it for indexing. That is:

- A **heavy forwarder (HF)** when you have deployed one as the parsing/routing tier (most enterprise deployments).
- The **indexer** itself when universal forwarders send directly to indexers (the indexer acts as both parser and writer).
- A **universal forwarder (UF)** handles only lightweight aggregation and forwarding — it does **not** apply `props.conf` parsing rules. Deploy parsing configuration to the tier that does the actual parsing, not the UF.

```
[UF] ─── raw bytes ──► [HF or IDX: applies props.conf] ──► [IDX: writes to bucket]
         (no parsing)         (parsing tier)
```

---

## 3. props.conf — structure and stanza types

`props.conf` lives in `$SPLUNK_HOME/etc/apps/<app>/local/props.conf` on the parsing tier. Its stanzas can target data in three ways:

```
[<sourcetype>]         # matches by sourcetype name — most common
[source::<glob>]       # matches by file path or URI using glob/regex
[host::<value>]        # matches by the host metadata field
```

Within each stanza you place **attribute = value** pairs that control parsing behavior. Attributes are **case-sensitive**.

> **Precedence within a file:** `source::` and `host::` stanzas take precedence over `<sourcetype>` stanzas when multiple stanzas match the same event. `<sourcetype>` takes precedence over `[default]`. This is the within-file specificity rule.

---

## 4. Sourcetype assignment — where it happens and why it matters

The sourcetype is the most important piece of metadata on an event. It controls:
- Which `props.conf` stanzas apply (and therefore all parsing)
- Which search-time field extractions run
- Which CIM mapping applies

**Where sourcetype is set (in priority order):**

1. **At the input** — in `inputs.conf`, via a `sourcetype = <value>` attribute. This is set on the forwarder or the data collection node. **If set here, it cannot be overridden later in `props.conf`.** This is the preferred location when the data source has a single, well-known type.
2. **In `props.conf`** using `sourcetype = <new_value>` under a `[source::<pattern>]` stanza — useful when you cannot control the input configuration.
3. **Automatic** — if neither of the above is configured, Splunk attempts to autodetect the sourcetype by matching against pretrained patterns.

> Do not attempt to set `sourcetype` in a `[<sourcetype>]` stanza in `props.conf` — that would create a circular reference. Use `source::` stanzas for sourcetype-overriding via props.

---

## 5. The event parsing pipeline — what happens in order

When data arrives at the parsing tier, Splunk processes it in this sequence:

```
Raw data stream
   │
   ▼
1. Charset / encoding normalization (CHARACTER_SET)
   │
   ▼
2. Line breaking — split stream into raw lines
   │  (LINE_BREAKER regex)
   │
   ▼
3. Line merging — optionally combine lines into multi-line events
   │  (SHOULD_LINEMERGE + BREAK_ONLY_BEFORE / MUST_BREAK_AFTER)
   │
   ▼
4. Truncation — enforce maximum event size (TRUNCATE)
   │
   ▼
5. Timestamp extraction — assign _time
   │  (TIME_PREFIX + TIME_FORMAT + MAX_TIMESTAMP_LOOKAHEAD + TZ)
   │
   ▼
6. Index routing / field transforms (TRANSFORMS- stanzas)
   │
   ▼
Indexed event in bucket
```

---

## 6. The "Great 8" event-processing settings in props.conf

These eight settings are the core of index-time event parsing. Every Splunk admin must know all of them.

### 6.1 SHOULD_LINEMERGE

```ini
SHOULD_LINEMERGE = [true|false]
# Default: true
```

When `true`, Splunk tries to combine consecutive lines into a single multi-line event using the merge settings (BREAK_ONLY_BEFORE, MUST_BREAK_AFTER). This is legacy behavior that predates the LINE_BREAKER approach.

**Best practice: set to `false` and use LINE_BREAKER instead.** There is a significant processing-speed advantage to the LINE_BREAKER approach because it avoids the overhead of the line-merging algorithm.

### 6.2 LINE_BREAKER

```ini
LINE_BREAKER = <regex>
# Default: ([\r\n]+)
```

A regex applied to the raw data stream. **The match itself is consumed (removed from the event boundary); the event starts with the first character of the capture group.** The default breaks on newline characters — one line = one event. For single-line data this default is usually correct. For multi-line events (stack traces, JSON blobs, structured records that span lines) you define a LINE_BREAKER regex that matches the *start* of a new event.

**Key technique:** anchor on a distinctive start-of-event pattern. For a log where every event begins with a timestamp like `2024-03-15`, the LINE_BREAKER should match just before that pattern:

```ini
[my_sourcetype]
SHOULD_LINEMERGE = false
LINE_BREAKER = ([\r\n]+)(?=\d{4}-\d{2}-\d{2})
```

The lookahead `(?=...)` asserts without consuming — the timestamp stays in the event.

### 6.3 BREAK_ONLY_BEFORE

```ini
BREAK_ONLY_BEFORE = <regex>
# Only used when SHOULD_LINEMERGE = true
```

When line merging is enabled, Splunk starts a new event **only** when a line matches this regex. Use when your events have a known header line pattern (e.g., a line beginning with a date). Subsequent lines with no match are merged into the previous event.

### 6.4 MUST_BREAK_AFTER

```ini
MUST_BREAK_AFTER = <regex>
# Only used when SHOULD_LINEMERGE = true
```

When line merging is enabled, Splunk forces a new event after any line matching this regex, regardless of what follows. Useful when events have a known terminator line.

> **BREAK_ONLY_BEFORE vs LINE_BREAKER:** These are two different models. BREAK_ONLY_BEFORE works with merging (`SHOULD_LINEMERGE = true`). LINE_BREAKER works without merging (`SHOULD_LINEMERGE = false`). The LINE_BREAKER + `SHOULD_LINEMERGE = false` combination is the modern preferred approach for multi-line data.

### 6.5 TRUNCATE

```ini
TRUNCATE = <integer>
# Default: 10000 (bytes)
```

Maximum event size in bytes. Events longer than this value are truncated at the byte boundary. The default 10,000 bytes is usually sufficient. Raise it if your data has legitimately large events (e.g., verbose JSON payloads). Setting it to `0` disables truncation entirely — use with caution, as unbounded event sizes cause memory and indexing problems.

### 6.6 TIME_PREFIX

```ini
TIME_PREFIX = <regex>
```

A regex that Splunk must match before it begins looking for a timestamp. Timestamp extraction starts from the position **immediately after** the end of the first match of this regex. If TIME_PREFIX is not found in the event, **no timestamp is extracted** and Splunk falls back to the current time (receipt time). Essential when the timestamp is not at the very beginning of the event (e.g., JSON where the time field appears mid-event).

Example — timestamp follows the literal key `"timestamp":`:

```ini
TIME_PREFIX = "timestamp":\s*"
```

### 6.7 TIME_FORMAT

```ini
TIME_FORMAT = <strptime string>
```

Specifies the exact format of the timestamp, using `strptime`-style format codes. Splunk reads this immediately after the position established by TIME_PREFIX.

Common format codes:

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | `2024` |
| `%m` | 2-digit month (01–12) | `03` |
| `%d` | 2-digit day | `15` |
| `%H` | Hour, 24-hour clock (00–23) | `14` |
| `%M` | Minutes (00–59) | `32` |
| `%S` | Seconds (00–59) | `07` |
| `%b` | Abbreviated month name | `Mar` |
| `%z` | Timezone offset | `+0400` |
| `%Z` | Timezone name | `UTC` |

Example — parse `2024-03-15T14:32:07`:

```ini
TIME_FORMAT = %Y-%m-%dT%H:%M:%S
```

### 6.8 MAX_TIMESTAMP_LOOKAHEAD

```ini
MAX_TIMESTAMP_LOOKAHEAD = <integer>
# Default: 128 (characters)
```

How many characters (starting from where TIME_PREFIX left off, or from the start of the event if TIME_PREFIX is not set) Splunk searches for a timestamp. Reduce this to speed up parsing on high-volume sources with known, compact timestamps. Increase it only if your timestamp genuinely appears far into the event.

### 6.9 TZ (timezone)

```ini
TZ = <timezone string>
# Example: TZ = Asia/Baku
# Example: TZ = UTC
```

Sets the assumed timezone for events from this source. Splunk's timestamp extraction first checks whether the raw event text contains an explicit timezone (e.g., `UTC`, `-05:00`, `+04:00`). If found, that takes precedence. If not found and TZ is set in `props.conf`, that timezone is applied. If neither, Splunk uses the indexer's local timezone — which is a common source of `_time` errors in distributed environments.

Use IANA timezone names (e.g., `America/New_York`, `Europe/London`, `Asia/Baku`) or UTC offset notation.

---

## 7. Worked example — custom log, fully configured

Suppose you have a custom application log format:

```
{RECV:"2024-03-15T14:32:07", src_ip:"10.20.10.50", action:"DENY", proto:"TCP"}
{RECV:"2024-03-15T14:32:08", src_ip:"10.20.10.51", action:"ALLOW", proto:"UDP"}
```

Each event is one JSON-like line. There is no timezone in the data; the application runs in UTC.

```ini
[my_app_log]
SHOULD_LINEMERGE = false
LINE_BREAKER     = ([\r\n]+)
TRUNCATE         = 10000
TIME_PREFIX      = \{RECV:"
TIME_FORMAT      = %Y-%m-%dT%H:%M:%S
MAX_TIMESTAMP_LOOKAHEAD = 20
TZ               = UTC
```

Explanation:
- `SHOULD_LINEMERGE = false` + default `LINE_BREAKER` = one line per event (correct here).
- `TIME_PREFIX = \{RECV:"` — Splunk starts looking for the time only after it matches `{RECV:"`.
- `TIME_FORMAT` — exact format of the ISO 8601-style timestamp.
- `MAX_TIMESTAMP_LOOKAHEAD = 20` — the timestamp `2024-03-15T14:32:07` is 19 characters; 20 gives a small buffer.
- `TZ = UTC` — events have no embedded timezone; force UTC interpretation.

---

## 8. Multi-line events — Java stack trace example

Java stack traces are the canonical multi-line case. A single exception event looks like:

```
2024-03-15 14:32:07 ERROR Exception in thread "main"
    at com.example.App.main(App.java:42)
    at java.lang.reflect.Method.invoke
```

New events always start with a line beginning with a date. Continuation lines start with whitespace.

**LINE_BREAKER approach (recommended):**

```ini
[java_app]
SHOULD_LINEMERGE = false
LINE_BREAKER     = ([\r\n]+)(?=\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})
TIME_FORMAT      = %Y-%m-%d %H:%M:%S
MAX_TIMESTAMP_LOOKAHEAD = 20
```

The lookahead `(?=\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})` matches a newline followed by a date — the boundary between events — without consuming the date, so the new event starts with its timestamp.

**BREAK_ONLY_BEFORE approach (legacy):**

```ini
[java_app]
SHOULD_LINEMERGE  = true
BREAK_ONLY_BEFORE = ^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}
```

Both produce the same result. Use the LINE_BREAKER approach for performance.

---

## 9. Data Preview — validate before you index

Data Preview is a GUI tool in Splunk Web (Settings → Add Data → Upload or Monitor → Set Source Type page). It allows you to upload a sample of your data, apply parsing settings interactively, and see the resulting events and extracted timestamps **before writing anything to an index**. Because index-time changes are irreversible, this step is not optional for any non-trivial data source.

**What to check in Data Preview:**

| What to verify | What wrong looks like |
|---|---|
| Event boundaries | One 500-line blob instead of 500 individual events; or 500 micro-events each containing one character |
| Timestamp (`_time`) | `_time` = now (receipt time) instead of the event's actual time; wrong year/timezone |
| Event content | Truncated events; stray newlines inside an event |

**Workflow:**
1. Upload a representative sample (200–1000 lines).
2. Observe the default event breaking under the "Event Breaks" section.
3. Adjust `LINE_BREAKER` (shown as a regex field in Advanced settings) until event boundaries are correct.
4. Verify timestamps. Add `TIME_PREFIX`, `TIME_FORMAT`, and `MAX_TIMESTAMP_LOOKAHEAD` as needed.
5. **Save the sourcetype** — Splunk writes the configuration to `props.conf` in the app context you specify.
6. Then index the real data.

The settings you adjust in Data Preview translate directly to `props.conf` stanzas. Saving a sourcetype from the GUI is equivalent to manually writing the stanza to `$SPLUNK_HOME/etc/apps/<app>/local/props.conf`.

---

## 10. Regex fundamentals for Splunk parsing

The parsing settings above (LINE_BREAKER, TIME_PREFIX, and later EXTRACT/REPORT field extractions) all use PCRE (Perl Compatible Regular Expressions). A working understanding of the following constructs is necessary.

### 10.1 Core syntax

| Construct | Meaning | Example |
|---|---|---|
| `.` | Any character except newline | `a.c` matches `abc`, `a1c` |
| `*` | Zero or more of the preceding | `a*` matches ``, `a`, `aaa` |
| `+` | One or more of the preceding | `a+` matches `a`, `aaa` |
| `?` | Zero or one (also makes quantifiers lazy) | `a?` matches `` or `a` |
| `{n,m}` | Between n and m repetitions | `\d{1,3}` matches 1–3 digits |
| `^` | Start of string (or line in multiline mode) | `^\d` |
| `$` | End of string/line | `\d$` |
| `\d` | Any digit `[0-9]` | `\d+` matches `42` |
| `\w` | Word character `[a-zA-Z0-9_]` | `\w+` matches `foo_bar` |
| `\s` | Whitespace | `\s+` matches spaces/tabs |
| `[abc]` | Character class — any of a, b, c | `[0-9]` = digit |
| `[^abc]` | Negated class — anything except a, b, c | `[^\s]+` = non-whitespace token |
| `\` | Escape literal metacharacter | `\.` matches a literal dot |

### 10.2 Capture groups and named groups

Parentheses `( )` create a **capture group**. The matched content is addressable:

- By position: `\1`, `\2` … in replacement strings (SEDCMD) or `$1`, `$2` in `FORMAT`.
- **By name** (named groups) — the preferred form in Splunk field extractions:

```
(?P<field_name>pattern)
```

Named groups directly produce field names. For example:

```
(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
```

In an EXTRACT stanza this creates a field named `src_ip` populated with the matched IP address.

### 10.3 Non-greedy matching

By default `.*` is **greedy** — it matches as much as possible. Append `?` to make it **non-greedy** (matches as little as possible):

- `".*"` on `"foo" and "bar"` matches `"foo" and "bar"` (greedy — takes everything between first `"` and last `"`).
- `".*?"` on the same string matches `"foo"` then `"bar"` separately (non-greedy — stops at the first `"`).

Non-greedy matching is almost always correct for extracting delimited field values.

### 10.4 Lookahead and lookbehind

- **Positive lookahead** `(?=...)` — asserts the pattern is ahead without consuming characters.
- **Negative lookahead** `(?!...)` — asserts the pattern is NOT ahead.
- **Positive lookbehind** `(?<=...)` — asserts the pattern is behind without consuming.

These are particularly useful in LINE_BREAKER to match a boundary without consuming the text that belongs to the next event.

---

## 11. Deploying props.conf to the parsing tier

`props.conf` containing index-time parsing settings must be present **on the tier that performs parsing** (heavy forwarder or indexer). In a distributed deployment, the canonical approach is to package the configuration in an app and deploy it:

- **To heavy forwarders:** via Deployment Server (DS) — the HF is a deployment client and receives app bundles from the DS.
- **To indexer cluster peers:** via the Cluster Manager (CM) — place the app in the CM's `manager-apps/` directory and push the bundle. The peers receive it in their `peer-apps/` directory, which has top precedence.
- **To a standalone indexer or single-instance:** manually copy the app or edit `local/props.conf` directly.

Place parsing configuration in `$SPLUNK_HOME/etc/apps/<your_ta>/local/props.conf`, not in `system/local`, to keep it portable and reviewable.

---

## 12. Terminology & version notes

- **Parsing tier:** since Splunk 7.x, consistent terminology. Heavy forwarder and indexer both serve this role depending on architecture.
- **PCRE:** Splunk's regex engine is PCRE. Named groups use Python syntax `(?P<name>...)` in Splunk (not `(?<name>...)` which is .NET/PCRE2 syntax). Both are accepted in modern Splunk 9.x but `(?P<name>...)` is the documented form.
- **`BREAK_ONLY_BEFORE_DATE`:** a special-case setting equivalent to `BREAK_ONLY_BEFORE` with an automatic date-matching regex. Documented but rarely needed when you have `LINE_BREAKER`.
- **`DATETIME_CONFIG`:** controls which datetime library (C or Splunk's own) is used for timestamp parsing. Default is fine for most sources; only relevant for extremely unusual timestamp formats.
- **Splunk 9.x** has no behavioral changes to the core parsing settings described here — these are stable, long-lived platform fundamentals.

---

## 13. Common misconceptions

- **"I can fix event breaking after data is indexed."** No — line merging and LINE_BREAKER operate at index time. To fix a parsing error you must delete the data from the index and re-ingest.
- **"SHOULD_LINEMERGE = true is the right way to handle multi-line data."** It works, but LINE_BREAKER with SHOULD_LINEMERGE = false is significantly faster and is the recommended approach.
- **"TIME_PREFIX is the timestamp itself."** No — TIME_PREFIX is the regex that positions the cursor *before* the timestamp. The timestamp starts after the match ends.
- **"If I don't set TIME_FORMAT, Splunk can't find the timestamp."** Splunk has heuristic timestamp detection that handles many common formats automatically. TIME_FORMAT is only required when autodetection fails or is unreliable.
- **"props.conf on the universal forwarder controls index-time parsing."** No — the UF does not perform parsing. Put parsing config on the HF or indexer.
- **"Setting sourcetype in props.conf under a sourcetype stanza overrides what was set at input time."** No — if sourcetype is set in `inputs.conf`, it cannot be overridden downstream in `props.conf`. The input-time assignment wins.
- **"Data Preview writes data to an index."** No — Data Preview is a read-only interactive validation tool. Data is not indexed until you complete the Add Data wizard.

---

## 14. Mastery checklist — what you should be able to explain

- The four-phase data onboarding workflow and where parsing fits.
- Why sourcetype is the most important metadata field, and the three places it can be assigned (input, props, automatic).
- Why parsing config must live on the parsing tier (HF or indexer), not the UF.
- The full event-parsing pipeline in order (charset → line break → merge → truncate → timestamp → transform).
- All eight core parsing settings: SHOULD_LINEMERGE, LINE_BREAKER, BREAK_ONLY_BEFORE, MUST_BREAK_AFTER, TRUNCATE, TIME_PREFIX, TIME_FORMAT, MAX_TIMESTAMP_LOOKAHEAD, TZ — what each does and its default.
- Why `SHOULD_LINEMERGE = false` + LINE_BREAKER is preferred over `SHOULD_LINEMERGE = true`.
- How to construct a LINE_BREAKER regex for single-line and multi-line events.
- How TIME_PREFIX and TIME_FORMAT work together to locate and parse a timestamp.
- How to write a strptime TIME_FORMAT string for a given timestamp.
- How to use Data Preview to validate event breaking and timestamps before indexing.
- The consequences of getting parsing wrong (no fix without re-indexing).
- Named capture groups, non-greedy quantifiers, and lookaheads in PCRE.

---

## 15. Key terms (flashcard seeds)

- **Sourcetype** — primary metadata field that controls which props.conf stanzas apply; set at input, in props, or auto-detected.
- **props.conf** — the parsing control file; stanza targets: `[<sourcetype>]`, `[source::<glob>]`, `[host::<value>]`.
- **Parsing tier** — the component that applies props.conf (heavy forwarder or indexer); NOT the universal forwarder.
- **SHOULD_LINEMERGE** — controls line merging; default true; best practice: set false, use LINE_BREAKER instead.
- **LINE_BREAKER** — regex applied to raw stream; match is consumed; defines event boundaries; default `([\r\n]+)`.
- **BREAK_ONLY_BEFORE** — line-merge setting; starts a new event only when the line matches the regex.
- **MUST_BREAK_AFTER** — line-merge setting; forces a new event after any line matching the regex.
- **TRUNCATE** — max event size in bytes; default 10000; set 0 to disable (dangerous).
- **TIME_PREFIX** — regex that positions timestamp extraction; time search starts after the match.
- **TIME_FORMAT** — strptime string describing the exact timestamp format.
- **MAX_TIMESTAMP_LOOKAHEAD** — character count (from TIME_PREFIX end) to search for timestamp; default 128.
- **TZ** — assumed timezone for events without an embedded timezone; use IANA names or UTC offsets.
- **`_time`** — the indexed timestamp field; always stored in epoch seconds; used for all time-based operations.
- **Data Preview** — GUI tool in Add Data → Set Source Type; validates event breaking and timestamps on a sample before indexing.
- **PCRE** — Splunk's regex engine; named groups `(?P<name>...)`, non-greedy `.*?`, lookaheads `(?=...)`.
- **Index-time vs search-time** — parsing settings are index-time; field extractions default to search-time (covered in topic 11.2).

---

## 16. Questions to drill (quiz seeds)

1. Name the four phases of the data onboarding workflow. At which phase is parsing configured?
2. Why can a Universal Forwarder not apply `props.conf` parsing settings? Where do those settings belong?
3. Sourcetype is set both in `inputs.conf` and in a `props.conf` source:: stanza. Which wins?
4. Describe the event-parsing pipeline from raw bytes to indexed event, listing steps in order.
5. What is the default value of `SHOULD_LINEMERGE`? Why is the recommended practice to disable it?
6. Write a `props.conf` stanza (sourcetype `my_app`) that correctly handles single-line events with timestamps in the format `2024-03-15 14:32:07 INFO …`, setting all relevant parsing controls.
7. Your log file has Java stack traces. New events always start with a date. Write a `LINE_BREAKER` regex that keeps the date as part of the next event (use a lookahead).
8. `TIME_PREFIX = "ts":"` and `TIME_FORMAT = %Y-%m-%dT%H:%M:%S`. Draw a timeline: the raw event is `… "ts":"2024-03-15T14:32:07", "action":"deny" …`. Trace exactly how Splunk extracts the timestamp.
9. An event's timestamp shows as "now" (receipt time) instead of the actual event time. What are three possible causes?
10. What does setting `TZ = UTC` do? When would you leave it unset instead?
11. How does `MAX_TIMESTAMP_LOOKAHEAD` interact with `TIME_PREFIX`?
12. What is `TRUNCATE = 0` and why is it risky?
13. In PCRE, what is the difference between `.*` and `.*?`? Give an example where the greedy form gives the wrong result.
14. Write a named capture group regex to extract an IPv4 address into a field named `dest_ip`.
15. What does Data Preview validate, and why can you not validate the same things after indexing?
