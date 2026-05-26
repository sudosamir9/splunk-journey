---
type: enhanced
theme: 03-apps-configs-layering
topic: config-files-and-layering
covers: "Lectures 19–21"
tags: [study-guide/enhanced, theme/03-apps-configs-layering]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Configuration Files & Layering / Precedence

> Deep reference on how Splunk configuration actually works: the `.conf` file format, the directory structure, `default` vs `local`, the two configuration contexts, the precedence rules that decide which setting wins, and how to inspect the result with `btool`. This is one of the most important topics in Splunk administration — almost every "why is Splunk doing that?" traces back to it. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Splunk's behavior is controlled by text **`.conf` files**. The same configuration file (say `inputs.conf`) can exist in *many* places at once, with overlapping or conflicting settings. At runtime Splunk **merges** all those copies into one effective configuration using a strict **precedence** scheme. Master this and you can confidently answer: *where do I put a setting, which copy wins, and why is the running value what it is?* Get it wrong and you'll edit a file that's being overridden by another and waste hours wondering why nothing changed.

---

## 1. The `.conf` file format

A Splunk configuration file is plain text with a `.conf` extension, organized as:

```
[stanza_name]
attribute = value
another_attribute = value

[another_stanza]
attribute = value
```

- A **stanza** is a `[bracketed]` section header that scopes a set of settings (e.g., `[general]`, a sourcetype name, an input definition).
- Under each stanza are **attribute = value** pairs.
- **Syntax is case-sensitive** — `SHOULD_LINEMERGE` is not `should_linemerge`. This trips people constantly.
- Each `.conf` file governs one area of behavior. You can edit them directly on disk (recommended for precision/automation) or, for many settings, through Splunk Web — which ultimately writes to a `.conf` file anyway.

**Common files you'll work with most:**

| File | Governs |
|---|---|
| `inputs.conf` | Data inputs (what to collect, and metadata like index/sourcetype) |
| `outputs.conf` | Forwarding (where a forwarder sends data) |
| `props.conf` | Parsing & search-time behavior per sourcetype/source/host |
| `transforms.conf` | Regex transforms referenced by `props.conf` (routing, masking, field creation) |
| `indexes.conf` | Index definitions, paths, sizing, retention |
| `server.conf` | Instance/server settings (server name, clustering, etc.) |
| `authorize.conf` | Roles and capabilities |
| `authentication.conf` | Auth (LDAP/SAML) |

---

## 2. The configuration directory structure

Configuration lives under **`$SPLUNK_HOME/etc/`** in three areas that matter:

- **`etc/system/`** — instance/system-level configuration. Contains:
  - `etc/system/default/` — Splunk's shipped defaults (**never edit**).
  - `etc/system/local/` — your instance-wide overrides.
- **`etc/apps/<app>/`** — per-app configuration. Each app contains:
  - `default/` — the app's shipped config (**never edit**).
  - `local/` — your overrides for that app.
- **`etc/users/<user>/<app>/local/`** — per-user configuration (settings a user creates in an app context).

So a given setting in, say, `props.conf` could simultaneously exist in `system/local`, several apps' `local` and `default`, and `system/default`. Splunk reconciles them by precedence.

Other directories under `$SPLUNK_HOME`: `bin/` (binaries/CLI), `var/lib/splunk/` (indexes/data), `var/log/splunk/` (Splunk's own logs — `splunkd.log` for troubleshooting).

---

## 3. `default` vs `local` — the golden rule

> **Never edit `default/`. Always put changes in `local/`. `local` overrides `default`.**

Why: Splunk **overwrites every `default/` directory on upgrade**. Anything you put there is lost. Your `local/` directories are preserved. This applies in both `system` and every app. When you change a setting in Splunk Web, Splunk writes it to the appropriate `local/` file for you. Editing files directly gives you precision and is automation-friendly; just always target `local`.

---

## 4. The two configuration contexts

This is the crux of layering. Every configuration is evaluated in one of **two contexts**, and the precedence order is *different* in each:

- **Global context (index-time / system-wide):** activities that happen independently of any app or user — **data input, parsing, indexing, forwarding**. Files like `inputs.conf`, `outputs.conf`, `indexes.conf`, and the index-time parts of `props.conf`/`transforms.conf` are evaluated here.
- **App/user context (search-time):** activities tied to *who is searching* and *which app they're in* — search-time field extractions, macros, `fields.conf`, saved searches, the search-time parts of `props.conf`.

The reason for two schemes: indexing has no "current user/app," so global settings prioritize the system; searching always happens *as a user, in an app*, so that context prioritizes the user and the active app.

---

## 5. Precedence in the GLOBAL context (index-time)

Highest priority wins. Descending order:

1. **`etc/system/local/`** — highest
2. **`etc/apps/<app>/local/`** — apps in lexicographic order (see §7)
3. **`etc/apps/<app>/default/`** — apps in lexicographic order
4. **`etc/system/default/`** — lowest

**Key takeaway:** in the global context, **`system/local` beats everything**, and `system/default` is the last resort. Within the app tier, `local` beats `default`.

## 6. Precedence in the APP/USER context (search-time)

Descending order (for the current user and the app they're in):

1. **`etc/users/<user>/<app>/local/`** — user-specific, highest
2. **`etc/apps/<current-app>/local/`**
3. **`etc/apps/<current-app>/default/`**
4. **`etc/system/local/`**
5. **`etc/system/default/`** — lowest

**Key difference from global:** here the **user** wins first, then the **current app**, and **`system/local` drops down the list** (it's near the bottom, not the top). A user's personal setting in an app beats the app's and the system's. (Objects from *other* apps participate only if they're exported/global — that's the sharing scope from the apps topic.)

> The single most important contrast to internalize: **global context → `system/local` is #1; app/user context → user/current-app is #1 and system is near the bottom.** This is the classic confusion point.

---

## 7. Lexicographic (ASCII) ordering of apps

When multiple apps each have a copy of a file at the same tier (e.g., two apps' `local/`), Splunk breaks the tie by **lexicographic (ASCII) order of the app directory name**, not by meaning:

- Compared character by character by ASCII value.
- **Numbers (0–9) > uppercase letters (A–Z) > lowercase letters (a–z).**
- So `app_A` beats `app_B`; an app named `100_x` beats `Acme`; `Cisco` beats `firewall` (uppercase `C` < lowercase `f`... by ASCII uppercase comes first, so it has **higher** precedence).
- Ordering is **lexicographic, not numeric**: `app10` sorts before `app9` (because `1` < `9` at the first differing character).

**Practical exploit:** admins prefix an app/dir with a low-ASCII string (e.g., a number or leading characters) to force it to win precedence over other apps. This is a common real-world technique for "override everything" apps.

---

## 8. How merging actually works (worked example)

At runtime Splunk **merges all copies** of a `.conf` file:

- For an attribute that exists in multiple copies (**a conflict**), the value from the **highest-precedence** file wins.
- For an attribute that exists in only one copy (**no conflict**), it's **added to the union** — every non-conflicting attribute from every layer is included.

**Example** — global context, `inputs.conf` for one stanza, copies in: `system/local`, `apps/Cisco/local`, `apps/firewall/local`, and `system/default`.

| Attribute | system/local (1) | Cisco/local (2) | firewall/local (3) | system/default (4) | **Effective** |
|---|---|---|---|---|---|
| `host` | `web01` | `fw` | `fw2` | `default-host` | **`web01`** (highest wins) |
| `index` | `os` | `net` | `net` | `main` | **`os`** |
| `sourcetype` | — | `cisco:ios` | `pan:traffic` | — | **`cisco:ios`** (Cisco beats firewall by ASCII; no higher copy) |
| `disabled` | — | — | `false` | — | **`false`** (only firewall has it → union) |
| `crcSalt` | — | — | — | `<SOURCE>` | **`<SOURCE>`** (only default has it → union) |

So the effective stanza = the highest-precedence value for each conflicting attribute, **plus** every attribute that appeared anywhere with no higher conflict. The result is a single merged stanza Splunk actually uses.

---

## 9. Attribute precedence *within* a single file

Precedence also operates inside one `.conf` file, by **stanza specificity**. In `props.conf`, for example, stanzas are applied in order of how specifically they target an event:

1. `[host::<value>]` and `[source::<value>]` — most specific
2. `[<sourcetype>]`
3. global/`[default]` — least specific

More specific stanzas override less specific ones for the same attribute. (Full detail belongs to the data-onboarding topic; know that "within-file" precedence exists in addition to "across-files" precedence.)

---

## 10. Inspecting the result: `btool`

You rarely want to trace precedence by hand. **`btool`** shows the **merged, effective configuration** Splunk is actually using, in precedence order, and (with `--debug`) **where each setting came from**:

```
splunk btool inputs list --debug
splunk btool props list <stanza> --debug
```

- Output is in precedence order; `--debug` prefixes each line with the **source file**, so you can see exactly which layer won.
- Caveats: `btool` reads files on disk (it shows what *would* be effective, not necessarily what's loaded in memory until you reload/restart); it takes **one conf file at a time**; and it historically does **not** show the `default` stanza of `inputs.conf`.

`btool` is the single best tool for answering "why is this setting the value it is?"

---

## 11. Applying changes: restart vs. reload

A config change on disk isn't live until Splunk reloads it. Some changes can be **reloaded** in place (via Splunk Web, the REST endpoint, or "debug/refresh"); others — notably many `server.conf`, `indexes.conf`, and input changes — require a **full restart** (`splunk restart`). When in doubt, or for index/clustering changes, restart.

---

## 12. Terminology & version notes

- The directory model (`system`, `apps`, `users`; `default` vs `local`) and the two-context precedence scheme are **stable across versions** — this is core, long-lived Splunk behavior.
- On **clustered indexer peers**, the precedence list expands: the **peer-apps** directories (pushed by the cluster manager) slot in at the top — roughly: `peer-apps/local` → `system/local` → `app/local` → `peer-apps/default` → `app/default` → `system/default`. (Pre-9.0 these were "slave-apps".)
- "debug/refresh" remains a practical reload mechanism, but the supported interface is the REST reload endpoint.

---

## 13. Common misconceptions

- **"There's one copy of each conf file."** No — many copies across `system`, apps, and users are merged at runtime.
- **"Precedence is the same everywhere."** No — **global** context puts `system/local` first; **app/user** context puts the user/current app first and system near the bottom.
- **"I edited a file but nothing changed."** Either a higher-precedence copy is overriding it, or you didn't reload/restart. Use `btool` + reload.
- **"App order is alphabetical/by meaning."** It's lexicographic ASCII: numbers > uppercase > lowercase, character by character.
- **"I'll just edit `default/`."** Upgrades overwrite it — use `local/`.
- **"Conflicting files mean one file completely replaces the other."** No — merge is per-attribute: highest wins on conflicts, everything else unions.

---

## 14. Mastery checklist — what you should be able to explain

- The `.conf` stanza/attribute format and that it's case-sensitive.
- The `etc/system`, `etc/apps`, `etc/users` structure and `default` vs `local`.
- Why you never edit `default/`.
- The two contexts (global/index-time vs app-user/search-time) and *why* they differ.
- The full precedence order in each context — and the key contrast (`system/local` top in global; user/app top in app/user).
- Lexicographic app ordering (numbers > uppercase > lowercase) and how to exploit it.
- How merging works per-attribute (conflict → highest wins; no conflict → union).
- How to use `btool` to find the effective value and its source.

---

## 15. Key terms (flashcard seeds)

- **`.conf` file** — text config: `[stanza]` + `attribute = value`; case-sensitive.
- **Stanza** — a bracketed section grouping settings.
- **`etc/system/{default,local}`** — instance-wide config (default shipped, local override).
- **`etc/apps/<app>/{default,local}`** — per-app config.
- **`etc/users/<user>/<app>/local`** — per-user config.
- **default vs local** — never edit default; local wins; default overwritten on upgrade.
- **Global context** — index-time/system-wide; precedence: system/local > app/local > app/default > system/default.
- **App/user context** — search-time; precedence: user > current-app local > current-app default > system/local > system/default.
- **Lexicographic (ASCII) order** — tie-break among apps; numbers > uppercase > lowercase.
- **Merging** — per-attribute: conflicts → highest precedence wins; non-conflicts → union.
- **Within-file precedence** — stanza specificity (e.g., props.conf host::/source:: > sourcetype > default).
- **`btool`** — shows merged effective config and (with `--debug`) the source file.
- **reload vs restart** — apply config changes; some need a full restart.
- **peer-apps** — clustered-peer config bundle dir (top of precedence on peers).

---

## 16. Questions to drill (quiz seeds)

1. Describe the `.conf` file format and one consequence of it being case-sensitive.
2. Name the three `etc/` configuration areas and the `default`/`local` split in each.
3. Why must you never edit `default/`, and where do changes go instead?
4. State the precedence order for the **global** context, top to bottom.
5. State the precedence order for the **app/user** context, and explain how it differs from global.
6. Two apps both have `inputs.conf` in `local`: `Acme` and `zebra`. Which wins, and why? What about `40-overrides` vs `Acme`?
7. Given conflicting and non-conflicting attributes across four copies of a file, describe the merged result.
8. What does `btool inputs list --debug` show you, and name two of its caveats.
9. In the app/user context, can a user's personal setting beat the app's default? Where does `system/local` sit?
10. You edited a `local` `.conf` and nothing changed — give two possible causes and how you'd diagnose with `btool`.
