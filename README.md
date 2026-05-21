# Splunk Journey — TDE to SIEM Architect

A learning journal documenting my path from Threat Detection Engineer to SIEM Architect, using Splunk Enterprise as the platform of focus.

## What this repo is

A working notebook, not a tutorial. It contains:

- **Course notes** from Saif Al-Shoker's *Complete Splunk Enterprise Certified Admin Course (NEW)* on Udemy
- **Synthesis notes** that cross-cut lectures, docs, and lab experience
- **A lab journal** documenting a full distributed Splunk Enterprise Security deployment in Azure
- **Runbooks** — reusable procedures I built or refined
- **Supplementary material** for topics not covered in the course (indexer/SH clustering, Monitoring Console, ES, UBA)
- **NotebookLM source bundles** that produce podcasts, quizzes, mind maps, and briefing docs from the repo content
- **Cheatsheets and references** built as I go

Structure documented in `CLAUDE.md`. Phase plan in `00-meta/roadmap.md`.

## Target architecture

Full distributed Splunk Enterprise Security + UBA deployment on Azure:

- 3-node indexer cluster
- 3-member search head cluster with Enterprise Security
- Heavy Forwarder for syslog (pfSense, Zeek)
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
3. `01-architecture/target-architecture.md` — the lab I'm building
4. `05-labs/journal/` — what I'm actually doing day-to-day
5. `03-topics/` — my own synthesis of what I'm learning

## Disclaimer

These are personal notes from a learning project. Configuration examples are for a lab environment, not production-hardened. IPs in the `10.20.x.x` space refer to the lab network only. No customer or employer data is included.

## License

Notes and original prose: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code snippets (where present): MIT.

Course transcripts in `02-course-saif/transcripts/` remain copyright of Saif Al-Shoker / Udemy — kept locally as personal study aids, **not for redistribution**.
