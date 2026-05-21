# NotebookLM Workflow

NotebookLM is a **production destination**, not just a review layer. Every completed Splunk theme or topic synthesis becomes a NotebookLM bundle that produces four outputs: **podcast, quizzes, mind map, briefing doc**.

This file documents the workflow, conventions, and the prompts I use for each output type.

---

## Why NotebookLM at all

For a variable-rhythm learner, NBLM compresses passive review time:

- **Podcast (Audio Overview):** turn 5 hours of course content into a 20-minute commute companion. Two AI hosts discuss the material; great for cementing concepts I half-understand.
- **Quizzes:** instant comprehension check after a section. NBLM generates questions from my own notes — surfaces blind spots better than Saif's lectures alone.
- **Mind maps:** visualize how concepts connect. Splunk has a lot of interconnected mechanics (buckets ↔ retention ↔ clustering ↔ search affinity); the mind map shows the wiring.
- **Briefing docs:** NBLM-generated study guides. Useful right before an exam or interview.

NBLM is also good at *grounding* — it cites sources from your notes, so I can trust it more than a general LLM that might hallucinate Splunk specifics.

---

## What goes into NotebookLM (sources)

NBLM accepts up to ~50 sources per notebook (limit subject to change). Per bundle:

| Source type | What I include |
|---|---|
| **Course transcripts** | The relevant theme's transcripts from `02-course-saif/transcripts/<theme>/` |
| **My lecture notes** | From `02-course-saif/notes/<theme>/` |
| **Topic synthesis** | The `03-topics/<topic>.md` file once written |
| **Concept atoms** | Linked atoms from `04-concepts/` that relate to the topic |
| **Lab journal entries** | Dated entries from `05-labs/journal/` that involved this topic |
| **Runbooks** | Relevant `05-labs/runbooks/` procedures |
| **Splunk docs** | URLs to canonical Splunk documentation pages (NBLM accepts URLs as sources) |
| **Supplementary** | Anything in `06-supplementary/` that fills course gaps |

**Do NOT include** in NBLM bundles:
- Raw `.conf` files with secrets (even if sanitized — NBLM may surface fragments)
- Real customer data, ever
- Anything from work — keep this lab/learning only

---

## Bundle structure

Every NBLM bundle is a folder under `99-notebooklm/<topic-slug>/` with this structure:

```
99-notebooklm/
└── <topic-slug>/                          # e.g., indexes-buckets-retention/
    ├── README.md                          # bundle index + scope statement
    ├── prompts.md                         # NBLM prompts used (for reproducibility)
    ├── sources-manifest.md                # which files I uploaded to NBLM
    ├── sources/                           # symlinks or copies of source files
    │   ├── 01-transcripts/
    │   ├── 02-notes/
    │   ├── 03-synthesis/
    │   ├── 04-concepts/
    │   ├── 05-journal/
    │   └── 06-runbooks/
    ├── quiz-seeds.md                      # questions I want NBLM to drill (manually authored)
    ├── glossary.md                        # key terms NBLM should know
    └── exports/                           # gitignored — NBLM outputs I download back
        ├── podcast.mp3                    # not committed
        ├── briefing.pdf                   # not committed
        └── notes-on-output.md             # what I thought of the output
```

`exports/` is gitignored because NBLM exports may contain personal phrasings/context I don't want public. The bundle inputs are public; the polished outputs stay local.

---

## When to create a bundle

Claude prompts me to bundle at these moments:

1. **After completing a course theme** (e.g., after lectures 22-28 on indexes/buckets, prompt me to bundle the "indexes-buckets-retention" topic).
2. **After writing a topic synthesis** in `03-topics/`.
3. **After a major lab milestone** (e.g., distributed lab built — bundle "distributed-deployment").
4. **Before exam prep** (e.g., one bundle per exam domain).

I don't bundle proactively — only when prompted or when I explicitly say "let's bundle X."

---

## Bundle creation workflow

When I say "bundle for NBLM: `<topic>`", Claude:

1. Asks me to confirm the topic slug (e.g., `indexes-buckets-retention`).
2. Creates the `99-notebooklm/<topic-slug>/` folder structure.
3. Identifies relevant source files across the repo and creates the `sources-manifest.md`.
4. Copies or symlinks source files into `sources/` subfolders (copies preferred — NBLM needs to read them as standalone files, not symlinks).
5. Generates `README.md` with scope statement, learning goals, and expected output use cases.
6. Drafts `glossary.md` with key terms (extracted from sources).
7. Drafts `quiz-seeds.md` — 10-20 questions I should be able to answer cold after this topic. These seed NBLM's quiz mode.
8. Populates `prompts.md` with the canonical prompts for each of the four outputs (see below).
9. Reminds me to verify nothing in the bundle leaks secrets.

Then I:

1. Open NotebookLM in browser → New notebook → `<topic-slug>`.
2. Upload all files from `sources/` plus `glossary.md` and `quiz-seeds.md`.
3. Add Splunk doc URLs as sources (NBLM accepts URLs).
4. Run the four prompts from `prompts.md` to generate outputs.
5. Download outputs into `exports/` (gitignored).
6. Write `notes-on-output.md` reflecting on what NBLM produced vs. expected.

---

## Canonical prompts (lives in each bundle's `prompts.md`)

### 1. Audio Overview (Podcast)

NBLM has a "Customize" button on Audio Overview. Use it.

```
Focus this episode on the practical mechanics of <topic> — how things actually work
under the hood, not just definitions. Assume the listener is an experienced Splunk
content engineer (SPL, correlation rules, ES content) who is now learning the
infrastructure side. Skip introductions to Splunk itself.

Cover:
- The mental model: what is this thing fundamentally doing?
- Why it matters operationally (failure modes, performance, scale)
- How it connects to other Splunk subsystems (cite at least 3 connections)
- Common admin pitfalls and how to avoid them
- One worked example from the lab notes

Avoid: SPL basics, knowledge object basics, analyst-level material.
```

### 2. Quizzes

NBLM's quiz feature is in the studio panel. Seed it with my `quiz-seeds.md` content, then ask for more.

```
Use my quiz-seeds.md as a starting point. Generate 25 more questions on <topic>
at three difficulty levels:

- 10 conceptual (the "why")
- 10 mechanical (the "how" — exact commands, conf settings, defaults)
- 5 scenario-based (the "given X, what would you do?")

Format: multiple choice with 4 options each, 1 correct. Include a brief
explanation of the correct answer that cites the source file.

Hard mode: don't make wrong answers obviously wrong. Test whether I actually
understand the distinctions.
```

### 3. Mind map

NBLM generates mind maps in the studio panel.

```
Generate a mind map for <topic> with the root being the topic itself and
4-6 main branches covering:

- Core concepts and mental model
- Key components / mechanisms
- Configuration surface (what files, what stanzas)
- Failure modes and troubleshooting
- Connections to other Splunk subsystems
- Operational considerations at scale

Each branch should have 2-4 sub-branches. Keep node labels short (3-7 words).
```

### 4. Briefing doc

NBLM's "Briefing Doc" feature lives in the studio panel.

```
Write a briefing doc on <topic> for an experienced Splunk content engineer
preparing for SPLK-1003 and a SIEM Architect role.

Structure:
1. Executive summary (3 bullets)
2. The mental model (1 paragraph)
3. How it works (mechanics, with concrete examples)
4. Configuration reference (key stanzas, defaults, precedence)
5. Operational considerations (capacity, performance, failure modes)
6. Common pitfalls and how to avoid them
7. Cross-references to other Splunk subsystems
8. Exam-relevant facts to memorize (bulleted list)
9. Open questions or things still unclear

Skip: SPL basics, knowledge objects, analyst material.
```

---

## What to do with NBLM outputs

| Output | Use it for |
|---|---|
| Podcast | Commute, gym, driving — passive review. Listen 2x speed. |
| Quizzes | Comprehension check before moving to next theme. Anything I get wrong → back into a `03-topics/` synthesis revision. |
| Mind map | Visual review when stuck. Print or screenshot, pin near desk. |
| Briefing doc | Pre-exam review. Pre-interview reference. Spot gaps in `03-topics/` notes. |

**Critical:** after using NBLM outputs, update the source `03-topics/<topic>.md` with anything NBLM exposed that I didn't know. NBLM is a feedback loop, not a final destination — the synthesis note stays the source of truth.

---

## Bundle naming conventions

Topic slugs in `99-notebooklm/`:

| Theme/topic | Slug |
|---|---|
| Course theme 1: Fundamentals & architecture | `01-fundamentals-architecture` |
| Course theme 4: Indexes, buckets, retention | `04-indexes-buckets-retention` |
| Course theme 9: Data inputs deep dive | `09-data-inputs` |
| Cross-cutting: Forwarder topology | `topology-forwarders` |
| Supplementary: Indexer clustering | `supp-indexer-clustering` |
| Supplementary: SHC | `supp-search-head-clustering` |
| Exam prep: SPLK-1003 domain 4 | `exam-1003-d4-licensing` |

Prefix with theme number for course-mirrored bundles, `topology-` or `supp-` or `exam-` for cross-cutting bundles.

---

## Gotchas

1. **NBLM source limit.** Currently ~50 sources per notebook. Bundle scope matters — don't shove every transcript into one notebook.
2. **NBLM doesn't sync.** If I update a source file in the repo, I need to re-upload to NBLM. Worth doing after major synthesis updates.
3. **Audio Overview generation can take 5-15 minutes.** Queue it, don't wait.
4. **NBLM output quality scales with input quality.** Garbage `02-course-saif/notes/` → garbage NBLM output. Synthesis notes (`03-topics/`) lift the quality dramatically.
5. **Don't upload secrets.** Even sanitized configs can have details that look real. When in doubt, redact harder before bundling.
6. **NBLM language.** Default to English. NBLM's Audio Overview is best in English.
