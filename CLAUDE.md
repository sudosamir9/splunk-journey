# Splunk Architect Journey — Project Context for Claude

> Claude Code reads this file automatically at the start of every session. It is the persistent context that keeps Claude aligned with my goals, level, conventions, and workflows. Update it as the project evolves — Claude should nudge me to update the "Current state" section at the end of major sessions.

---

## Who I am

- **Role:** Threat Detection Engineer (TDE). Previously SOC Analyst.
- **Splunk experience:** 1+ year. Daily work involves writing SPL, analyzing incidents, tuning correlation rules, building lookup files, and content engineering for Splunk Enterprise Security.
- **Strong on:** SPL, knowledge objects, ES content side, detection logic
- **Intentionally weak on:** platform infrastructure, low-level engineering, conf-file mechanics, deployment architecture, clustering — this gap is exactly why this project exists
- **Location:** Baku, Azerbaijan

## Where I'm going

| Stage | Cert | When | Status |
|---|---|---|---|
| 1 | SPLK-1002 — Power User | Short-term | Light prep (daily work covers most content) |
| 2 | SPLK-1003 — Admin | Short-term | **Primary focus right now** |
| 3 | SPLK-3001 — ES Admin | Mid-term | Already work with ES from content side |
| 4 | SPLK-2002 — Architect | Long-term | Capstone for SIEM Architect role |
| 5 | Splunk Cloud Cert. Admin | Stretch | Optional |

**Long-term goal:** SIEM Architect role. Capacity planning, multi-site clustering, ITSI, SOAR integration, design and review.

## Current focus

Working through **"Complete Splunk Enterprise Certified Admin Course (NEW)"** by Saif Al-Shoker on Udemy.

- 10.5 hours, 68 lectures
- Transcripts already extracted into `02-course-saif/transcripts/`
- Covers: fundamentals → install → configs → indexes → forwarders → distributed → data inputs → onboarding (props/transforms)
- **Course gaps** (covered in `06-supplementary/`): indexer clustering, search head clustering, monitoring console, ES admin, UBA
- Capstone uses AWS; I'm on Azure. Concepts 1:1, only IaaS plumbing differs

Full TOC and theme breakdown: `02-course-saif/course-index.md`. Phase roadmap: `00-meta/roadmap.md`.

## My lab

Full distributed Splunk Enterprise Security + UBA deployment on **Azure paid subscription**, built manually (no IaC yet — pedagogical choice; Terraform/Ansible later).

- **VNet:** `10.20.0.0/16`
- **Mgmt** `10.20.1.0/24` — CM+LM, DS, SHC Deployer, MC
- **Indexer** `10.20.2.0/24` — 3 IDX peers
- **Search** `10.20.3.0/24` — 3 SHC members + ES
- **Ingest** `10.20.4.0/24` — HF, UBA
- **Endpoints** `10.20.10.0/24` — AD DC, Windows + Sysmon, Linux, Zeek, pfSense

Full diagram + subnet rationale: `01-architecture/target-architecture.md`. All `az` CLI commands I run get logged in `05-labs/azure-setup/azure-cli-commands.md` (semi-IaC by hand, makes the Terraform leap trivial later).

**Cost discipline rules:**
- Every new VM gets auto-shutdown enabled at creation time
- "Tear down Friday, rebuild Monday" for non-essential VMs
- Claude must remind me to enable auto-shutdown whenever I describe spinning up a VM

## My workflow

- **OS:** Windows 11 + WSL2 (Ubuntu)
- **Repo location:** `C:\Users\<me>\Documents\splunk-journey\` (Windows side). From WSL: `/mnt/c/Users/<me>/Documents/splunk-journey/`, aliased to `splunk`
- **Editor:** VS Code with WSL extension; Claude Code runs in WSL inside VS Code's integrated terminal
- **Notes:** Obsidian (vault = this repo) is source of truth. Notion is optional polished/mobile mirror. May converge to Obsidian-only within weeks
- **Review:** NotebookLM for podcasts, quizzes, mind maps, briefing docs — see `00-meta/notebooklm-workflow.md`
- **Memory technique:** No Anki. Labs + NotebookLM quizzes handle recall
- **Version control:** Public GitHub repo
- **Session rhythm:** Variable / opportunistic — no fixed schedule. Notes and handoff must be discoverable after multi-day gaps

---

## Repo conventions

### Folder structure (canonical)

| Folder | Content |
|---|---|
| `00-meta/` | Decisions log, chat summaries, roadmap, NBLM workflow, Obsidian config, templates |
| `00-meta/handoffs/` | Archived `handoff.md` files (dated, growing timeline) |
| `00-meta/templates/` | Obsidian/Templater note templates |
| `01-architecture/` | Target Azure architecture, mermaid diagrams, IP plans, NSG rules |
| `02-course-saif/transcripts/` | Raw extracted transcripts (mirrored to course themes) |
| `02-course-saif/notes/` | Per-lecture quick notes (course-mirrored, terse) |
| `03-topics/` | Synthesis notes per Splunk topic, cross-cutting — **this is where my understanding lives** |
| `04-concepts/` | Atomic Obsidian-linked notes for cross-referencing (organic, not forced) |
| `05-labs/runbooks/` | Reusable procedures: "how to do X" |
| `05-labs/configs/` | Sanitized Splunk `.conf` files |
| `05-labs/journal/` | Dated entries: what I built, what broke, how I fixed it — **portfolio gold** |
| `05-labs/azure-setup/` | Azure CLI command log, network design, NSG rules, VM specs |
| `06-supplementary/` | Topics outside Saif's course (clustering, MC, ES, UBA) |
| `07-practice-exam/` | Mock questions, exam blueprints, weak-area drills |
| `08-references/` | Cheatsheets, port lists, conf precedence, defaults |
| `99-notebooklm/` | NBLM source bundles per topic. See `00-meta/notebooklm-workflow.md` |

### Naming conventions

- Files: `lowercase-with-hyphens.md`
- Dated entries: `YYYY-MM-DD-short-slug.md` (ISO date first — sorts correctly)
- Handoff archives: `YYYY-MM-DD-HHMM-short-slug.md`
- Lab journal headings: `# YYYY-MM-DD — <focus>`
- Mermaid for diagrams (renders in GitHub, Obsidian, Notion)
- Tables for structured data; prose for understanding

### Public repo — strict secrets hygiene

**This is a public GitHub repo. Assume everything is public.**

Never commit:
- Real IPs from work/employer environments (lab IPs in `10.20.x.x` are fine)
- Splunk license keys, license XML files
- Azure subscription IDs, tenant IDs, real principal names
- `.env` files, credentials, SSH private keys, API tokens
- Real customer/employer data or log samples
- Screenshots with tokens, secrets, or real names visible

**Pre-commit scan (Claude runs this whenever I'm about to commit):**

```bash
git diff --cached | grep -iE "license|password|secret|token|api[_-]?key|bearer|\.lic\b" | head -20
git diff --cached | grep -E "10\.[0-9]+\.[0-9]+\.[0-9]+" | grep -v "10\.20\." | head -20
git diff --cached | grep -iE "[a-f0-9]{32,}|[A-Za-z0-9]{40,}" | head -10
```

If anything suspicious shows up that isn't lab-network IPs (`10.20.x.x`), stop and investigate.

### Hybrid note-taking style

- **`02-course-saif/transcripts/`** — raw, untouched, mechanical reference
- **`02-course-saif/notes/`** — per-lecture quick notes (what the lecture *taught*). Course-mirrored, terse
- **`03-topics/`** — synthesis notes (what I *learned*). Cross-cutting, written *after* understanding, not during
- **`04-concepts/`** — atomic linked notes. 2-4 sentences each. Heavily linked, not heavily detailed. Grows organically
- **`05-labs/journal/`** — dated entries. The most valuable artifacts in this repo. Treat as deliverables, not scratch

---

## How to help me, Claude

### Tone and depth

- **I'm not a beginner.** I write SPL daily. Skip SPL basics, knowledge objects, analyst-level concepts unless I ask. Explain infrastructure deeply
- **Be direct.** Skip "great question," skip closing summaries unless I ask, no emojis
- **Push back honestly** when I'm wrong, even on small things
- **No hedging.** "It depends" is fine, but follow with the actual decision criteria
- **Use my vocabulary.** TDE, SHC, IDX cluster, CM, RF/SF, props/transforms — don't define terms I obviously know

### Lab-first thinking

- When I ask about a concept, suggest a lab exercise that proves I understand it
- Tie features to my actual architecture (`01-architecture/`) when relevant
- "Try this command, expect this output" beats long explanations
- Cite Splunk docs when they conflict with Saif (he's from ~2022; we're in 2026)

### Course awareness

- Know where I am in Saif's course (`02-course-saif/course-index.md` has checkboxes; `handoff.md` has current state)
- Flag when his content runs out or contradicts current Splunk practice
- When I finish a section, prompt me to write or update the relevant `03-topics/` synthesis note
- Suggest NBLM bundling moments — "you've got enough on indexing now to make a podcast"

### Continuity over time

- Variable schedule. If I disappear for days and return, **catch me up on where I was** from `handoff.md` first
- If something I write today contradicts a note from a week ago, point it out
- Suggest periodic synthesis: every ~5 lectures, prompt me to write/update a `03-topics/` note
- At the end of each session, prompt me to update `handoff.md` (see protocol below)

### Commit hygiene

- Before any `git commit`, run the pre-commit scan above
- Suggest commit messages in imperative mood, < 72 chars
- Group related changes into atomic commits, not one giant "wip"

### What I want from each session

- Default opening: read `handoff.md` first, then brief me. Don't do anything else until I confirm direction
- Ask before creating large structures; just do small file edits
- Don't proactively rewrite my notes — if I want polish, I'll ask

---

## Session handoff protocol — MANDATORY

My session rhythm is variable. Without structured handoff I lose state between sessions. This is non-negotiable.

### At session start

1. Read `handoff.md` at the repo root. This is the canonical "where am I" snapshot.
2. Brief me on it: current goal, last actions, what's blocked, what's next.
3. Optional but useful: scan `git log --oneline -10` and the most recent file modifications, mention anything not reflected in `handoff.md`.
4. Confirm with me whether to continue that thread or pivot.

### At session end

Triggered by any of: "wrap up", "I have to go", "save state", "handoff", "let's stop here".

1. Read the **current** `handoff.md` (the one I'll be replacing).
2. Archive it: copy to `00-meta/handoffs/YYYY-MM-DD-HHMM-<short-slug>.md`. Use the timestamp from inside the file itself (when it was originally written), not now. The slug should describe what that session was about.
3. Write a new `handoff.md` at the repo root using the structure below.
4. Show me the new `handoff.md` before saving. Ask if I want changes.
5. Remind me to commit if there are uncommitted changes.

### `handoff.md` structure

```markdown
# Handoff — <YYYY-MM-DD HH:MM Asia/Baku>

## Current goal
<One sentence: what is the active thread? E.g., "Working through Saif lectures 17-21 on apps and conf layering">

## Where I am in the journey
- **Phase:** <which phase in roadmap.md>
- **Course progress:** <X / 68 lectures> — last completed: <lecture number + title>
- **Lab status:** <one line — what's provisioned, what's torn down, current state>
- **Active topic synthesis:** <which 03-topics/ file is in flight, if any>
- **Active runbook/journal:** <which file I was last editing>

## What I did this session
<bullets, terse — what I built, watched, wrote, broke>
-
-

## What I tried that didn't work
<be specific: command, error, what I think went wrong>
-

## What I changed
<files touched, configs modified, VMs provisioned/destroyed, commits made>
-

## What's blocked / open questions
<things I need to figure out, gaps I noticed, things to research next>
-

## Next step
<ONE concrete action to start the next session with. Not a list.>

## Notes for future-me
<anything that won't be obvious from the files: context, hunches, "I almost forgot...">
```

### Rules

- **"Next step" is one concrete action.** Not "review notes, do labs, read docs." Pick the single first thing.
- **If a session ended abruptly without a proper handoff**, the next session's first job is to reconstruct one from `git log`, recent file changes, and the lab journal.
- **Never delete handoff archives.** They're the timeline of my learning, and they're portfolio material.
- **Handoffs are committed to git.** They're not secrets, they're the project's heartbeat.

---

## NotebookLM workflow — production target

NotebookLM is not just a review layer — it's a **production destination** for podcasts, quizzes, flashcards, and mind maps. Full workflow in `00-meta/notebooklm-workflow.md`.

Quick rules for Claude:

- When I've completed a course theme or topic synthesis, prompt me: "Want to bundle this for NotebookLM?"
- Bundles live in `99-notebooklm/<topic-slug>/` as a folder of markdown files ready for upload
- Each bundle includes: source notes, lab journal references, key terms list, and a "questions to drill" file that seeds NBLM's quiz mode
- I generate four outputs per bundle: podcast (audio overview), quizzes, mind map, briefing doc
- I keep the *prompts* I used for each NBLM output in `99-notebooklm/<topic-slug>/prompts.md` so I can reproduce/improve them later

---

## Current state

> Claude, please nudge me to update this section at the end of major sessions.

- [ ] **Phase (from roadmap):** Phase 0 — Setup
- [ ] **Course progress:** 0 / 68 lectures
- [ ] **Lab status:** Azure subscription only — no VMs provisioned yet
- [ ] **Power User exam (SPLK-1002):** not scheduled
- [ ] **Admin exam (SPLK-1003):** not scheduled
- [ ] **Most recent journal entry:** none yet
- [ ] **Last decision logged:** initial setup decisions in `00-meta/decisions-log.md`
- [ ] **Active NBLM bundles:** none yet

---

## Pointers (read order for "where am I")

1. `handoff.md` — current session state (always read first)
2. `00-meta/roadmap.md` — phase/chapter plan
3. `02-course-saif/course-index.md` — Saif TOC with checkboxes
4. `01-architecture/target-architecture.md` — target Azure architecture
5. `00-meta/decisions-log.md` — decisions and rationale
6. `00-meta/chat-summary.md` — full setup history
7. `00-meta/notebooklm-workflow.md` — how to produce NBLM outputs
8. `00-meta/obsidian-setup.md` — vault config, templates, plugins
