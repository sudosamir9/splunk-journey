# Splunk Journey — TDE to SIEM Architect

A learning journal documenting my path from Threat Detection Engineer to SIEM Architect, using Splunk Enterprise as the platform of focus.

## What this repo is

A working notebook, not a tutorial. It contains:

- **Course notes** from Saif Al-Shoker's *Complete Splunk Enterprise Certified Admin Course (NEW)* on Udemy
- **A structured study guide** (`09-study-guide/`) — for every course theme, a deep self-contained reference (`enhanced.md`) plus a short pre-read primer (`pre-class.md`), split into 19 topics and written as general Splunk material; doubles as ready-to-upload NotebookLM source
- **Synthesis notes** that cross-cut lectures, docs, and lab experience
- **A lab journal** documenting a full distributed Splunk Enterprise Security deployment in Azure
- **Runbooks** — reusable procedures I built or refined
- **Supplementary material** for topics not covered in the course (indexer/SH clustering, Monitoring Console, ES, UBA)
- **NotebookLM source bundles** that produce podcasts, quizzes, mind maps, and briefing docs from the repo content
- **Cheatsheets and references** built as I go

Structure documented in `CLAUDE.md`. Phase plan in `00-meta/roadmap.md`.

## Study guide (`09-study-guide/`)

Self-contained study material covering all 11 course themes in **19 topics**, verified against current Splunk documentation. Each topic folder holds:

- **`enhanced.md`** — a deep, general Splunk reference written to stand on its own (the architectural *why* and the practical *how*).
- **`pre-class.md`** — a ~1-page primer to read before the matching lecture, ending with an official-docs reference table.
- **`nblm.md`** — ready-to-paste NotebookLM prompts (podcast, quiz, flashcards) for that topic.

The design: **one topic = one NotebookLM notebook = one ~25–30 min audio overview**, plus a quiz set, flashcard deck, and mind map generated from the same source. Topics are sized so each sustains a full episode (thin lectures are merged). Full topic→lecture coverage map in `09-study-guide/README.md`.

## Target architecture

Full distributed Splunk Enterprise Security + UBA deployment on Azure:

- 3-node indexer cluster
- 3-member search head cluster with Enterprise Security
- Heavy Forwarder for syslog (Palo Alto Firewall)
- UBA for behavioral analytics
- Management tier: Cluster Manager + License Manager, Deployment Server, SHC Deployer, Monitoring Console
- Endpoint sources: AD DC, Windows + Sysmon, Linux, Zeek sensor, pfSense

Full diagram in `01-architecture/target-architecture.md`.

## Certification path

| Stage | Cert | Status |
|---|---|---|
| 1 | SPLK-1002 — Splunk Core Certified Power User | In progress |
| 2 | SPLK-1003 — Splunk Enterprise Certified Admin | In progress |
| 3 | SPLK-3001 — Splunk Enterprise Security Certified Admin | Planned |
| 4 | SPLK-2002 — Splunk Certified Architect | Planned |

## How I'm working

- **Editor:** VS Code with WSL2 on Windows 11
- **AI pair:** Claude Code (reads `CLAUDE.md`, `handoff.md`, and `00-meta/chat-summary.md` for context every session)
- **Notes:** Obsidian (vault = this repo)
- **Review and production:** NotebookLM for podcasts, quizzes, mind maps, and briefing docs (bundles in `99-notebooklm/`)
- **Lab:** Azure paid subscription, manual build (no IaC for now — pedagogical choice)

## Repo navigation

If you're landing here for the first time:

1. `CLAUDE.md` — full project context
2. `00-meta/roadmap.md` — what I'm building, in what order
3. `09-study-guide/` — deep per-topic study material (enhanced + pre-class + NotebookLM prompts) for all 11 themes
4. `01-architecture/target-architecture.md` — the lab I'm building
5. `05-labs/journal/` — what I'm actually doing day-to-day
6. `03-topics/` — my own synthesis of what I'm learning

## Disclaimer

These are personal notes from a learning project. Configuration examples are for a lab environment, not production-hardened. IPs in the `10.20.x.x` space refer to the lab network only. No customer or employer data is included.

## License

Course transcripts in `02-course-saif/transcripts/` remain copyright of Saif Al-Shoker / Udemy — kept locally as personal study aids, **not for redistribution**.
