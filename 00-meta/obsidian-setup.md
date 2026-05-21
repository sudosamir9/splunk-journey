# Obsidian Vault Setup

The Obsidian vault **is** the repo. One folder, two surfaces. No sync layer to maintain.

---

## Initial vault setup

1. Open Obsidian → **Open folder as vault** → browse to `C:\Users\<YOU>\Documents\splunk-journey\`
2. Trust the author and enable plugins when prompted
3. Settings → **Files & Links**:
   - "Default location for new notes": **Same folder as current file**
   - "Default location for new attachments": **In subfolder under current folder**, name `attachments`
   - "Use [[Wikilinks]]": **ON**
   - "Detect all file extensions": **OFF**

4. Settings → **Appearance**: pick a theme you can stand for hours (suggested: *Minimal* or *Things*). Font size readable at end of day, not start.

5. Settings → **Editor**:
   - "Readable line length": **ON**
   - "Strict line breaks": **OFF** (standard markdown)
   - "Auto pair brackets" + "Auto pair Markdown syntax": **ON**

---

## Core plugins (Settings → Core plugins)

Enable: **Templates**, **Daily notes** (optional — see below), **Outline**, **Tags**, **Graph view**, **Backlinks**, **Command palette**, **Page preview**, **File recovery**.

Disable plugins you won't use (Audio recorder, Bookmarks if unused, Workspaces) to keep the UI tight.

---

## Community plugins (Settings → Community plugins)

Install in this order. Don't install all at once.

### Round 1 (install now)

| Plugin | Purpose |
|---|---|
| **Templater** | Smarter templates than core (dates, file paths, variable expansion) |
| **Dataview** | Query notes like a database (e.g., "all lab entries from this week") |
| **Advanced Tables** | Sane markdown table editing |
| **Mermaid Tools** | Better mermaid editing/preview |

### Round 2 (add when needed)

| Plugin | Purpose |
|---|---|
| **Excalidraw** | Hand-drawn architecture sketches |
| **Mind Map** | Visualize concept relationships |
| **Tag Wrangler** | Manage your tag taxonomy |
| **Kanban** | Track exam prep todos as boards |
| **Iconize** | Folder icons (visual scannability) |

### Deliberately not using

- **Obsidian Git plugin** — git handled at WSL/VS Code level. Adding here creates merge conflicts on `.obsidian/`.
- **Obsidian Sync (paid)** — overlaps with git-based workflow.
- **Spaced repetition plugins** — decided no Anki.

---

## Folder ↔ template mapping (Templater)

Settings → Templater:

- **Template folder location:** `00-meta/templates`
- **Enable folder templates:** ON
- **Folder template mappings:**

| Folder | Template |
|---|---|
| `02-course-saif/notes` | `lecture-note.md` |
| `03-topics` | `topic-synthesis.md` |
| `04-concepts` | `concept-atom.md` |
| `05-labs/journal` | `lab-journal-entry.md` |
| `05-labs/runbooks` | `runbook.md` |
| `06-supplementary` | `topic-synthesis.md` |
| `99-notebooklm` | `nblm-bundle-readme.md` (root of each bundle) |

Claude Code generates these templates in the bootstrap session (master prompt step 11).

---

## Template structures (Claude Code creates these)

### `lecture-note.md`
```markdown
---
course: saif-admin
theme: <theme-slug>
lecture: <number>
lecture-title: <title>
duration: <min>
date-watched: <YYYY-MM-DD>
tags: [course/saif-admin, theme/<theme>]
---

# Lecture <number> — <title>

## Key points
-

## Commands / configs shown
```bash
```

## Questions / gaps
-

## Links to topic notes
- [[<related topic synthesis>]]
```

### `topic-synthesis.md`
```markdown
---
topic: <splunk-topic>
last-updated: <YYYY-MM-DD>
status: draft | working | stable
tags: [topic/<area>]
sources:
  - course-lecture-<n>
  - splunk-docs: <url>
  - my-lab: <date>
---

# <Topic>

## In one sentence
<one-line definition>

## Why it matters
<paragraph>

## How it actually works
<detail with examples>

## How it shows up in my architecture
<tie-in to 01-architecture/target-architecture.md>

## Common pitfalls
-

## Related
- [[<other topic>]]
- [[<concept atom>]]
```

### `lab-journal-entry.md`
```markdown
---
date: <YYYY-MM-DD>
session-length: <approx minutes>
focus: <single sentence>
tags: [journal, lab]
---

# <Date> — <Focus>

## Goal of this session
<what I wanted to accomplish>

## What I built / changed
<actual actions, commands, configs touched>

## What broke
<errors, surprises, dead-ends>

## How I fixed it
<resolution + the reasoning that got me there>

## What I now understand that I didn't this morning
<the synthesis line — the most important paragraph in the entry>

## Next session: pick this up by
<concrete first action>
```

### `runbook.md`
```markdown
---
title: <how to X>
splunk-version: 9.x
last-verified: <YYYY-MM-DD>
tags: [runbook]
---

# <How to X>

## When to use this
<one sentence>

## Prerequisites
-

## Steps
1.
2.

## Verification
<how to confirm it worked>

## Rollback
<how to undo>

## Notes
<surprises, gotchas>
```

### `concept-atom.md`
```markdown
---
concept: <one thing>
tags: [concept]
---

# <Concept>

<2–4 sentences. Single-purpose. Heavily linked, not heavily detailed.>

## See also
- [[ ]]
```

### `nblm-bundle-readme.md`
```markdown
---
bundle: <topic-slug>
created: <YYYY-MM-DD>
status: draft | uploaded | outputs-generated
tags: [nblm-bundle]
---

# NBLM Bundle — <topic>

## Scope
<what this bundle covers, what it does NOT cover>

## Learning goals
- I should be able to: <verb> <thing>
-

## Sources (see sources-manifest.md for files)
- Saif lectures: <range>
- Topic synthesis: [[<file>]]
- Lab journal: <dates>
- Runbooks: [[<file>]]
- Splunk docs URLs: (add directly in NBLM)

## Outputs generated
- [ ] Podcast (Audio Overview)
- [ ] Quizzes
- [ ] Mind map
- [ ] Briefing doc

## Reflections
<what NBLM exposed that I didn't know>
```

---

## Recommended hotkeys (Settings → Hotkeys)

| Action | Hotkey |
|---|---|
| Templater: Insert template | `Ctrl+Alt+T` |
| Toggle right sidebar | `Ctrl+Shift+\` |
| Open graph view | `Ctrl+G` |
| Quick switcher | `Ctrl+O` |
| Command palette | `Ctrl+P` |
| Insert link | `Ctrl+K` |
| Toggle source/reading mode | `Ctrl+E` |
| Insert callout | `Ctrl+Shift+C` (Advanced Tables) |

---

## Daily notes (optional)

If you want a scratch surface:

- **Template:** `00-meta/templates/daily.md` (minimal — just a `## Quick log` heading)
- **Date format:** `YYYY-MM-DD`
- **Location:** `00-meta/daily/`

Don't force daily notes if your rhythm is variable — they become guilt artifacts. Use only if they help.

---

## Graph view tips

Once `04-concepts/` fills out, the graph becomes useful. Settings:

- **Filters:** include `04-concepts/`, `03-topics/`. Exclude `02-course-saif/transcripts/` (too noisy).
- **Groups (colors):**
  - Tag `topic/*` → one color
  - Tag `concept` → another
  - Folder `05-labs/journal/*` → third color
  - Folder `99-notebooklm/*` → fourth color
- **Forces:** lower link force (~0.2), higher repel (~12) — produces a more readable layout

---

## Useful Dataview queries

Drop these into a note like `00-meta/dashboards.md` for a personal dashboard.

### Recent lab journal entries (last 14 days)

````
```dataview
TABLE focus, session-length AS "min"
FROM "05-labs/journal"
WHERE date >= date(today) - dur(14 days)
SORT date DESC
```
````

### Topic synthesis status

````
```dataview
TABLE status, last-updated
FROM "03-topics"
SORT last-updated DESC
```
````

### Open NBLM bundles

````
```dataview
TABLE status, created
FROM "99-notebooklm"
WHERE status != "outputs-generated"
```
````

### Course progress

````
```dataview
TABLE theme, lecture, date-watched
FROM "02-course-saif/notes"
SORT lecture ASC
```
````

---

## On running Notion alongside Obsidian

You decided to run both at first. The split:

- **Obsidian is source of truth.** All writing happens here.
- **Notion is for mobile review + sharing with humans** (mentors, study buddies, future employers).
- Sync by hand for now (copy/paste polished `03-topics/` notes). Don't automate until you know whether you'll keep both.
- Re-evaluate at the 1-month and 3-month marks. Most people converge to one.
