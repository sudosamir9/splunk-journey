---
type: enhanced
theme: 11-data-onboarding
topic: 2-field-extraction-sedcmd-masking
covers: "Lectures 66–68"
tags: [study-guide/enhanced, theme/11-data-onboarding]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Field Extraction, SEDCMD & Data Masking

> Deep reference on how Splunk extracts fields from events: the search-time vs index-time distinction, inline EXTRACT extractions in props.conf, REPORT extractions that reference transforms.conf stanzas, DELIMS for delimited data, and TRANSFORMS for index-time field extraction that writes to `_meta`. Then: SEDCMD in props.conf for in-place data modification at index time, and the two approaches to masking sensitive data (SEDCMD and transforms-based `DEST_KEY = _raw` rewriting) — including when to use each, their respective tradeoffs, and their behavior after the fact. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Once events are correctly broken and timestamped, the next layer is **fields**. Fields are the foundation of every search, every correlation rule, and every dashboard. Splunk's model gives you a choice at design time: extract fields when the data is *indexed* (once, irreversibly, at cost) or when a user *searches* (every time, flexibly, at zero storage cost). Understanding why the default is search-time, when you have no choice but to go index-time, and how to construct correct extraction and masking configurations is what separates ad-hoc onboarding from production-quality data pipelines.

---

## 1. Search-time vs index-time field extraction — the fundamental choice

### 1.1 The default is search-time (schema-on-read)

Splunk stores events as raw text. Fields are **not** stored in the index by default — they are extracted from `_raw` at query time. This is "schema-on-read": you define what a field means when you go to read it, not when you write it. The benefits are:

- **Flexibility:** you can add, change, or remove field extractions without touching the index or re-ingesting data.
- **Zero storage overhead:** fields are not stored; the raw event is.
- **Retroactive extraction:** a new EXTRACT stanza extracts a field from *all historical events* for that sourcetype immediately, without re-indexing.

This is the correct default for the vast majority of fields. Use search-time extraction unless you have a specific reason not to.

### 1.2 When index-time is required

There are three legitimate reasons to extract fields at index time:

| Reason | Explanation |
|---|---|
| **Data masking / anonymization** | You must rewrite `_raw` before it is stored. Masking is inherently index-time — you cannot un-store sensitive data. |
| **Routing** | `DEST_KEY = _MetaData:Index` in a transforms stanza, controlled from props, routes events to different indexes based on field values. This routing decision happens at index time. |
| **Required cross-search consistency on a field that searches must filter at indexer level** | Rare in practice; search-time extraction is faster to change and costs nothing to add. |

Index-time field extraction is irreversible (like all index-time operations) and adds overhead at write time. **Default to search-time. Go index-time only when the use case genuinely requires it.**

### 1.3 The pipeline diagram

```
Event arrives at parsing tier
         │
         ▼
INDEX-TIME TRANSFORMS run (TRANSFORMS- stanzas in props.conf)
  └─► transforms.conf stanza
       ├── REGEX + DEST_KEY = _meta  →  writes indexed field to _meta
       ├── REGEX + DEST_KEY = _raw   →  rewrites _raw (masking)
       └── REGEX + DEST_KEY = _MetaData:Index  →  routes to index
         │
         ▼
Event stored in bucket (_raw text, _time, indexed fields in .tsidx)
         │
         ▼
SEARCH-TIME EXTRACTIONS run (EXTRACT- / REPORT- stanzas in props.conf)
  └─► from _raw on every search
         │
         ▼
Fields available to search pipeline
```

---

## 2. Search-time extraction — EXTRACT in props.conf

### 2.1 Syntax

```ini
[<sourcetype>]
EXTRACT-<unique_class_name> = <named-group regex>
```

The `<unique_class_name>` is an arbitrary label (it is part of the configuration key but has no effect on the field names produced). The regex must contain at least one **named capture group** `(?P<field_name>pattern)` — the group name becomes the field name.

```ini
[my_app_log]
EXTRACT-src_ip = src_ip="(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
```

This extracts a field named `src_ip` from events of sourcetype `my_app_log`. No `transforms.conf` entry is needed.

### 2.2 Multiple fields in one EXTRACT

A single regex can extract multiple fields at once using multiple named groups:

```ini
[my_app_log]
EXTRACT-network_fields = src_ip="(?P<src_ip>[\d.]+)"\s+dst_ip="(?P<dst_ip>[\d.]+)"\s+action="(?P<action>\w+)"
```

This is the most common pattern — one compact regex per logical group of related fields.

### 2.3 Considerations

- EXTRACT runs against `_raw` on every search that touches this sourcetype. For high-cardinality data at high query volume, a very expensive regex can add search latency.
- Multiple EXTRACT stanzas for the same sourcetype all run at search time. Use descriptive class names to distinguish them.
- EXTRACT is processed **before** REPORT in the search-time extraction order. This matters if one extraction depends on the result of another (it does not — they are independent).

---

## 3. Search-time extraction via transforms.conf — REPORT

### 3.1 When to use REPORT instead of EXTRACT

Use `REPORT` when:
- The same regex needs to be reused across multiple sourcetypes, sources, or hosts — define it once in `transforms.conf`, reference it from multiple `props.conf` stanzas.
- The extraction logic is complex enough that centralizing it in `transforms.conf` improves maintainability.
- You need to use `FORMAT` to produce field values that are not just the captured string.

### 3.2 props.conf side

```ini
[<sourcetype>]
REPORT-<class_name> = <transform_stanza_name>
```

Multiple transforms can be referenced as a comma-separated list:

```ini
[my_app_log]
REPORT-network = extract_network_fields
REPORT-user    = extract_user_fields
```

### 3.3 transforms.conf side — REGEX-based extraction

```ini
[extract_network_fields]
REGEX  = src="(?P<src_ip>[\d.]+)"\s+dst="(?P<dst_ip>[\d.]+)"
FORMAT = src_ip::$1 dst_ip::$2
```

When named capture groups are used in the REGEX, the `FORMAT` is optional — Splunk uses the group names directly. When positional groups are used, `FORMAT` maps positions to field names:

```ini
[extract_network_fields]
REGEX  = src="([\d.]+)"\s+dst="([\d.]+)"
FORMAT = src_ip::$1 dst_ip::$2
```

`$1`, `$2` etc. refer to capture groups by position. The `FORMAT` syntax is `<field_name>::<value>` where the value can be a literal or a `$n` reference.

### 3.4 transforms.conf side — DELIMS for delimited data

`DELIMS` is an alternative to `REGEX` for **ASCII-only delimiter-based** data (CSV, TSV, space-separated, key=value pairs separated by known delimiters). It is **only valid for search-time** extractions.

```ini
[csv_sourcetype]
DELIMS = ","
```

This splits each event on commas and assigns the values to fields. If the data is `field1=val1,field2=val2`, you also specify a field/value delimiter:

```ini
[kv_sourcetype]
DELIMS = ",", "="
```

The first delimiter separates field/value pairs from each other; the second separates field name from field value within each pair.

> Use DELIMS for simple structured formats. Use REGEX when the structure is irregular, fields are optional, or the data contains the delimiter within values.

---

## 4. Index-time field extraction — TRANSFORMS in props.conf

### 4.1 Mechanism

Index-time field extraction uses a **different props.conf directive**: `TRANSFORMS-<class>` (not `REPORT-` or `EXTRACT-`). This is the key distinction — the same transforms.conf stanza format is used, but the props.conf side determines whether it runs at index time or search time.

```ini
[<sourcetype>]
TRANSFORMS-<class_name> = <transform_stanza_name>
```

The class name is an arbitrary label. The referenced stanza in transforms.conf must specify `DEST_KEY` or `WRITE_META`.

### 4.2 transforms.conf for index-time field extraction

```ini
[index_time_field_example]
SOURCE_KEY = _raw
REGEX      = src_ip="(?P<src_ip>[\d.]+)"
WRITE_META = true
```

`WRITE_META = true` writes the extracted field into the `_meta` field, which becomes an indexed field stored in the `.tsidx` file alongside the event. This field is then available for filtering at the indexer level without reading `_raw`.

Alternatively:

```ini
[index_time_field_example]
SOURCE_KEY = _raw
REGEX      = src_ip="([\d.]+)"
DEST_KEY   = _meta
FORMAT     = src_ip::$1
```

`DEST_KEY = _meta` is equivalent to `WRITE_META = true` when combined with `FORMAT`. Use `WRITE_META = true` to append to `_meta` safely; multiple transforms each with `WRITE_META = true` will all write to `_meta`. If you use `DEST_KEY = _meta` without `WRITE_META`, each transform overwrites the previous — so only use `WRITE_META = true` when multiple index-time transforms need to coexist.

### 4.3 SOURCE_KEY

`SOURCE_KEY` specifies which data stream to run the REGEX against. Default is `_raw` (the full event text). You can also use `SOURCE_KEY = MetaData:Host`, `MetaData:Source`, or `MetaData:Sourcetype` to match against those metadata fields.

### 4.4 Overwriting metadata fields at index time

A common use case is overwriting the `host` metadata field based on a value in the event content — useful when the data arrives from an intermediary (e.g., a syslog relay) and the host field reflects the relay rather than the originating device.

```ini
# props.conf
[my_sourcetype]
TRANSFORMS-host_override = set_host_from_event

# transforms.conf
[set_host_from_event]
SOURCE_KEY = _raw
REGEX      = src_ip="(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
DEST_KEY   = MetaData:Host
FORMAT     = host::$1
```

`DEST_KEY = MetaData:Host` overwrites the host field. The `FORMAT` uses the literal `host::` prefix followed by `$1` (the first capture group).

Other metadata DEST_KEY values:

| DEST_KEY value | What it writes |
|---|---|
| `MetaData:Host` | The `host` field |
| `MetaData:Source` | The `source` field |
| `MetaData:Sourcetype` | The `sourcetype` field |
| `MetaData:Index` | Routing — sends event to the named index |
| `_meta` | Indexed field (use with `WRITE_META = true` or `FORMAT`) |
| `_raw` | Rewrites the raw event text (masking) |

---

## 5. SEDCMD — inline data modification at index time

### 5.1 What SEDCMD does

`SEDCMD` is a `props.conf` setting that applies a sed-like substitution to `_raw` at index time. It is the quickest way to do in-place data modification — adding, removing, or replacing text in the raw event before it is stored.

```ini
[<sourcetype>]
SEDCMD-<class_name> = <sed_expression>
```

The class name is an arbitrary label (like EXTRACT- and REPORT- class names). Multiple SEDCMD entries can exist in one stanza.

### 5.2 Sed expression syntax

Two operations are supported:

**Substitution (`s///`):**

```
s/<search_regex>/<replacement>/[flags]
```

Flags:
- `g` — global: replace all occurrences in the event, not just the first.
- `i` — case-insensitive match.
- `gi` — both.

**Transliterate (`y///`):**

```
y/<source_chars>/<dest_chars>/
```

Replaces each character in `source_chars` with the corresponding character in `dest_chars`. Used for simple character substitutions (e.g., changing separators, normalizing case for specific characters).

### 5.3 Capture groups in SEDCMD

Capture groups work with standard regex syntax. The replacement uses `\1`, `\2`, … (backslash-number) to reference groups, **not** `$1` (that syntax is for transforms.conf FORMAT):

```ini
[my_sourcetype]
SEDCMD-mask_cc = s/(\d{4})-(\d{4})-(\d{4})-(\d{4})/XXXX-XXXX-XXXX-\4/g
```

This replaces the first three groups of four digits (the card prefix) with `XXXX` while preserving the last four digits. The result: `4532-1234-5678-9012` → `XXXX-XXXX-XXXX-9012`.

### 5.4 Complete worked example — masking a MAC address prefix

Raw event contains: `src_mac="aa:bb:cc:dd:ee:ff"`

Goal: mask the first three octets (the OUI) and preserve the last three.

```ini
[my_sourcetype]
SEDCMD-mask_mac_oui = s/([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}):([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})/XX:XX:XX:\2/g
```

The first capture group matches the OUI (3 octets). The second capture group matches the device ID (3 octets). The replacement writes `XX:XX:XX:` followed by `\2` (the preserved device ID).

### 5.5 SEDCMD operates only on _raw

SEDCMD applies to the raw event text (`_raw`) only. It cannot target individual metadata fields like `host` or `source`. For metadata manipulation, use the TRANSFORMS approach with `DEST_KEY`.

---

## 6. Data masking at index time — two approaches

Masking sensitive data (credit card numbers, SSNs, passwords, API keys) must happen at index time — the data must never reach the storage layer in clear text. There are two mechanisms in Splunk. Understanding the tradeoffs determines which to use.

### 6.1 Approach 1: SEDCMD

```ini
[payment_log]
SEDCMD-mask_pan = s/(\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?)(\d{4})/XXXX-XXXX-XXXX-\2/g
```

**How it works:** sed substitution is applied directly to `_raw` before the event is stored. The masked text replaces the original in storage.

**Characteristics:**
- Simpler to configure — everything in one props.conf line.
- Slightly faster at index time.
- Applies to `_raw` only.
- Limited to substitution and transliteration operations.

### 6.2 Approach 2: TRANSFORMS with DEST_KEY = _raw

```ini
# props.conf
[payment_log]
TRANSFORMS-mask_pan = mask_credit_card

# transforms.conf
[mask_credit_card]
SOURCE_KEY = _raw
REGEX      = (\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?)(\d{4})
FORMAT     = XXXX-XXXX-XXXX-$2
DEST_KEY   = _raw
```

**How it works:** the transforms.conf stanza matches the REGEX against SOURCE_KEY (default `_raw`), formats a replacement using `FORMAT`, and writes it back to `DEST_KEY = _raw`. This overwrites the raw event with the masked version.

**Characteristics:**
- More verbose but more flexible.
- Supports `SOURCE_KEY` targeting (could match against a specific metadata field before writing to `_raw`).
- Can be combined with other DEST_KEY operations in the same transforms workflow.
- `FORMAT` with `$n` capture group references.

> **Key syntax difference:** SEDCMD replacements use `\1`, `\2`; transforms.conf FORMAT uses `$1`, `$2`. Mixing them up is a common error.

### 6.3 Choosing between them

| Factor | SEDCMD | TRANSFORMS + DEST_KEY=_raw |
|---|---|---|
| Simplicity | Simpler — one props.conf line | Requires both props and transforms |
| Speed | Slightly faster | Slightly more overhead |
| Flexibility | Substitution and transliterate only | Full REGEX + FORMAT power |
| SOURCE_KEY control | Always _raw | Can target metadata fields as source |
| Reuse across sourcetypes | Separate SEDCMD per stanza | One transforms stanza, multiple REPORT/TRANSFORMS references |

For simple, one-off masking of a known pattern in a single sourcetype, SEDCMD is the pragmatic choice. For a masking policy that applies across multiple sourcetypes, or where the pattern logic is complex, use TRANSFORMS.

### 6.4 Masking is irreversible

Once data lands in the index with masked content, the original values are gone. Verify your masking regex against sample data before deploying to production. Use Data Preview or regex101.com to confirm the pattern matches correctly and the replacement produces the intended output.

---

## 7. The index-time vs search-time tradeoff — decision framework

```
                    SEARCH-TIME                  INDEX-TIME
Default?            Yes                          No — explicit choice
Storage cost?       Zero (not stored)            Some (indexed field in .tsidx)
Indexing cost?      Zero                         CPU at write time
Query latency?      Extract on every query       Pre-computed — marginally faster
Retroactive?        Yes — new stanza applies      No — must re-ingest
                    to all historical data
Reversible?         Yes — remove the stanza       No — data is stored as-is
Use for masking?    No — data would already       Yes — only option for masking
                    be stored in clear text
Use for routing?    No                           Yes — DEST_KEY = MetaData:Index
Recommendation?     Default for all fields        Reserve for masking, routing,
                    unless a specific reason      and genuinely required
                    applies                       index-level filters
```

---

## 8. Worked end-to-end example — extraction and masking on a custom log

Sample event (custom network device log):

```
{ts:"2024-03-15T14:32:07", src_ip:"10.20.10.50", src_mac:"aa:bb:cc:11:22:33", action:"DENY"}
```

Requirements:
1. Extract `src_ip`, `src_mac`, and `action` as search-time fields.
2. Mask the first three octets of `src_mac` at index time.

**props.conf:**

```ini
[network_device]
SHOULD_LINEMERGE         = false
LINE_BREAKER             = ([\r\n]+)
TIME_PREFIX              = \{ts:"
TIME_FORMAT              = %Y-%m-%dT%H:%M:%S
MAX_TIMESTAMP_LOOKAHEAD  = 20
TZ                       = UTC

# Search-time field extraction
EXTRACT-fields = src_ip:"(?P<src_ip>[\d.]+)"\S+src_mac:"(?P<src_mac>[0-9a-fA-F:]+)"[^}]+action:"(?P<action>\w+)"

# Index-time masking
TRANSFORMS-mask_mac = mask_mac_oui
```

**transforms.conf:**

```ini
[mask_mac_oui]
SOURCE_KEY = _raw
REGEX      = (src_mac:")([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}):([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})(")
FORMAT     = $1XX:XX:XX:$3$4
DEST_KEY   = _raw
```

After indexing, `_raw` contains: `{ts:"2024-03-15T14:32:07", src_ip:"10.20.10.50", src_mac:"XX:XX:XX:11:22:33", action:"DENY"}`

The EXTRACT stanza then runs at search time against the already-masked `_raw`, so `src_mac` will be extracted as `XX:XX:XX:11:22:33` — the masked value.

> Order matters: index-time TRANSFORMS runs before the event is stored; search-time EXTRACT runs against the stored (potentially masked) `_raw`.

---

## 9. App context and search-time field extractions

Search-time field extractions defined via EXTRACT or REPORT are **knowledge objects**. They are scoped to the **app context** in which they are saved. A user searching in "Search & Reporting" does not see extractions saved in your custom app unless they switch to that app context (or the object is exported/shared globally).

This is the practical implication: when you save a field extraction using the Field Extractor GUI, it writes to `props.conf` in the currently active app's `local/` directory. If you later search from a different app, the extraction is invisible. For production deployments, package your `props.conf` in an app that is deployed to search heads (for search-time extractions) and to the parsing tier (for index-time transforms).

---

## 10. Debugging field extractions

**For search-time extractions:**
- Run `| fieldsummary` or click "Fields" in the sidebar after a search to see which fields are being extracted.
- Use `| rex` in a search to prototype a regex before committing it to `props.conf`: `| rex field=_raw "src_ip=\"(?P<src_ip>[\d.]+)\""`.
- Use `btool`: `splunk btool props list <sourcetype> --debug` shows the effective merged configuration and which file each extraction came from.

**For index-time transforms and masking:**
- Changes only take effect on newly indexed data. A debug/refresh via `http://<splunk>:8000/en-US/debug/refresh` or the CLI equivalent reloads the configuration, but existing indexed data is unaffected.
- Always test masking on a sample — upload a test file, verify the masked result in the search, then delete and re-ingest the real data if needed.
- Regex101.com (PCRE flavor) is the fastest way to verify your REGEX and capture groups against a real event sample before deploying.

---

## 11. Terminology & version notes

- **`EXTRACT-` / `REPORT-` / `TRANSFORMS-`** in props.conf: all three are props.conf directives, but `TRANSFORMS-` runs at index time and the others at search time. The distinction is entirely in the directive prefix, not in the transforms.conf stanza itself.
- **`WRITE_META` vs `DEST_KEY = _meta`:** `WRITE_META = true` appends to `_meta` safely when multiple transforms write indexed fields. `DEST_KEY = _meta` alone will overwrite, so the last transform wins. Splunk 9.x docs consistently recommend `WRITE_META = true` for index-time field creation.
- **`$1` vs `\1`:** FORMAT in transforms.conf uses `$1`; SEDCMD replacements use `\1`. Consistent with respective origins (transforms = Splunk FORMAT notation; SEDCMD = Unix sed notation).
- **`_raw` rewrite:** when DEST_KEY = `_raw`, Splunk writes the FORMAT output as the new raw event. The FORMAT must contain the full desired event text, not just the replaced portion — unless the REGEX captures the surrounding context in groups.
- **Splunk 9.x:** no behavioral changes to EXTRACT/REPORT/TRANSFORMS/SEDCMD relative to 8.x — these are stable platform primitives.

---

## 12. Common misconceptions

- **"EXTRACT and TRANSFORMS do the same thing."** No — `EXTRACT-` / `REPORT-` run at search time (reversible, zero storage cost). `TRANSFORMS-` runs at index time (irreversible, applies to new data only).
- **"I can mask data after it's indexed."** No — masking must happen at index time before the event is written. After indexing, the data is in `_raw` permanently.
- **"SEDCMD and `DEST_KEY = _raw` both modify the event — they're interchangeable."** They achieve the same end result (overwriting `_raw`) but by different mechanisms. SEDCMD is self-contained in props.conf. The TRANSFORMS approach requires a transforms.conf stanza and is more flexible.
- **"SEDCMD replacements use `$1` for capture groups."** No — SEDCMD uses `\1` (sed syntax). transforms.conf FORMAT uses `$1`. Mixing this up silently produces wrong output.
- **"A search-time field extraction defined in one app is visible everywhere."** Not by default — it is scoped to the app context. It is only visible in other app contexts if the knowledge object is explicitly shared globally.
- **"DELIMS can be used for index-time extraction."** No — DELIMS is only valid for search-time field extractions.
- **"A new TRANSFORMS- stanza applies to existing indexed data."** No — index-time operations apply only to data ingested after the configuration change. Existing data is unaffected.

---

## 13. Mastery checklist — what you should be able to explain

- The search-time vs index-time distinction, why search-time is the default, and the three legitimate reasons to go index-time.
- The difference between `EXTRACT-`, `REPORT-`, and `TRANSFORMS-` in props.conf — what tier each runs on and what configuration files each needs.
- How to write an EXTRACT stanza with named capture groups for field extraction.
- When to use REPORT + transforms.conf instead of EXTRACT, and how to write the transforms.conf stanza with REGEX and FORMAT.
- What DELIMS does and when it applies (search-time, ASCII delimiters only).
- How index-time field extraction works: `TRANSFORMS-` in props.conf + `WRITE_META = true` or `DEST_KEY = _meta` in transforms.conf.
- All DEST_KEY values and what each writes (host, source, sourcetype, index routing, _meta, _raw).
- What SEDCMD does, its two syntaxes (substitution `s///` and transliterate `y///`), and the `\1` capture group reference.
- The two masking approaches (SEDCMD and TRANSFORMS DEST_KEY=_raw) and how to choose between them.
- That `_raw` rewrite via either approach is permanent and cannot be reversed.
- The capture group reference syntax difference: `\1` in SEDCMD vs `$1` in transforms.conf FORMAT.
- App context scoping of search-time extractions and its practical consequence.

---

## 14. Key terms (flashcard seeds)

- **Search-time extraction** — fields extracted from `_raw` at query time; default; reversible; retroactive; zero storage cost.
- **Index-time extraction** — fields extracted at write time; irreversible; applies only to new data; use for masking, routing, or indexed field creation.
- **EXTRACT-** — props.conf directive for search-time inline extraction (no transforms.conf needed); uses named groups.
- **REPORT-** — props.conf directive for search-time extraction via transforms.conf stanza; enables reuse.
- **TRANSFORMS-** — props.conf directive for index-time extraction via transforms.conf stanza.
- **transforms.conf stanza (search-time)** — `REGEX` + optionally `FORMAT` or `DELIMS`; produces field/value pairs.
- **DELIMS** — transforms.conf setting for ASCII delimiter-based search-time extraction; alternative to REGEX.
- **FORMAT** — transforms.conf setting specifying field name/value pairs; uses `$1`, `$2` for capture groups.
- **WRITE_META = true** — appends extracted fields to `_meta` (index-time indexed fields); safe with multiple transforms.
- **DEST_KEY = _meta** — writes to indexed field store; equivalent to WRITE_META for single-transform scenarios.
- **DEST_KEY = _raw** — rewrites the raw event text; used for masking and anonymization.
- **MetaData:Host / Source / Sourcetype / Index** — DEST_KEY values for overwriting metadata fields or routing.
- **SEDCMD** — props.conf setting; sed-like substitution on `_raw` at index time; `s/regex/replacement/flags`; `\1` groups.
- **`s///g`** — SEDCMD global substitution; replaces all matches in the event.
- **`y///`** — SEDCMD transliterate; character-by-character substitution.
- **Data masking** — irreversible index-time operation; SEDCMD or TRANSFORMS DEST_KEY=_raw; must verify before indexing real data.
- **Schema-on-read** — Splunk's default model; fields defined at query time, not write time.
- **App context scoping** — search-time knowledge objects visible only in the app they are saved in, unless exported globally.

---

## 15. Questions to drill (quiz seeds)

1. Explain the difference between `EXTRACT-`, `REPORT-`, and `TRANSFORMS-` in props.conf. Which runs at index time? Which require a transforms.conf entry?
2. Write a `props.conf` EXTRACT stanza for sourcetype `web_log` that extracts `client_ip`, `method`, and `uri` from an event of the form `client="10.20.1.5" method="GET" uri="/index.html"`.
3. When would you use REPORT instead of EXTRACT? What is the advantage of centralizing the regex in transforms.conf?
4. Write the full props.conf + transforms.conf configuration to extract a field `session_id` from events of the form `… session_id=ABCD1234 …` at search time using REPORT.
5. What does DELIMS do? What is its main limitation?
6. Your organization requires that the `host` field reflect the originating device IP taken from the event body, not the relay host that sent it. Write the props.conf and transforms.conf stanzas to accomplish this at index time.
7. A payment processing log contains lines like `card=4532123456789012 amount=99.00`. Write a SEDCMD that masks all but the last four digits of the card number.
8. Explain the difference between SEDCMD and a TRANSFORMS stanza with `DEST_KEY = _raw` for masking. When would you prefer one over the other?
9. What is the capture group reference syntax in SEDCMD? How does it differ from the syntax in transforms.conf FORMAT?
10. You deploy a new TRANSFORMS- masking stanza for a sourcetype that has already had data indexed for six months. Which data does the masking apply to?
11. A search-time field extraction defined in the `demo_lab` app is not visible when a user searches in `Search & Reporting`. Why? How do you fix it?
12. What does `WRITE_META = true` do, and why is it preferred over `DEST_KEY = _meta` when multiple index-time transforms write to indexed fields?
13. In `DEST_KEY = _raw` masking, the FORMAT must contain the full desired event text, not just the replacement. Write a transforms.conf stanza that masks a Social Security Number (pattern `\d{3}-\d{2}-\d{4}`) while preserving all other event content.
14. Name all the valid DEST_KEY values and what each one does.
15. Why is search-time extraction considered "schema-on-read"? What operational advantage does this give over index-time?
