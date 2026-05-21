# Decisions Log

Dated record of project decisions and their rationale. New decisions get a dated entry at the top. The canonical setup narrative lives in `chat-summary.md`; this file is the scannable index of *what was chosen and why*.

---

## 2026-05-21 — Initial setup decisions

Seeded from the setup conversation (`chat-summary.md`). These are the foundational choices the whole repo is built on.

### Environment & tooling

- **OS: Windows 11 + WSL2 (Ubuntu).** Existing setup; WSL2 is the canonical Claude Code environment on Windows.
- **Claude shell: WSL Ubuntu, not PowerShell.** Unix-first design, matches lab work.
- **Project location: Windows side at `C:\Users\<me>\Documents\splunk-journey\`.** Obsidian indexes cleanly on NTFS; WSL accesses via `/mnt/c/`. Performance hit negligible for notes/transcripts.
- **Editor: VS Code with WSL extension**, Claude Code in the integrated terminal.

### Lab

- **Lab platform: Azure paid subscription, full distributed diagram.** Real-world scale matters for the architect track.
- **IaC: none for now.** Manual build teaches more; Terraform/Ansible come later. Every `az` command logged in `05-labs/azure-setup/azure-cli-commands.md` (semi-IaC by hand → makes the Terraform leap trivial).
- **Cost discipline: auto-shutdown every VM at creation (~23:00 local); tear down Friday, rebuild Monday for non-essentials.** Azure built-in feature. Claude reminds me whenever I describe spinning up a VM.

### Notes & knowledge

- **Note tools: Obsidian + Notion (both, initially).** Obsidian = source of truth / working notes; Notion = polished/mobile mirror. Re-evaluate at 1- and 3-month marks; likely converge to Obsidian-only.
- **Note style: hybrid.** Course-mirrored raw transcripts + terse per-lecture notes + topic synthesis (written *after* understanding) + atomic concept notes (organic) + lab journal (treated as deliverables).
- **Spaced repetition: no Anki.** Labs + NotebookLM quizzes handle recall — prefer doing over memorizing.
- **NBLM role: production target, not just review.** All four outputs (podcast, quiz, mind map, briefing) per `99-notebooklm/<topic>` bundle.

### Course & path

- **Primary course: Saif Al-Shoker's Admin course (SPLK-1003).** Cert + lab spine. Supplement separately for the gaps it skips: indexer clustering, SHC, Monitoring Console, ES admin, UBA (`06-supplementary/`).
- **Power User (SPLK-1002): exam-familiarize, don't re-learn.** I do Power User-level work daily; heavy learning goes to Admin and beyond.
- **Roadmap: phase/chapter-based, no calendar.** Variable rhythm → deliverables over deadlines.

### Process & continuity

- **Session rhythm: variable / opportunistic.** Structure must be self-explanatory after multi-day gaps.
- **Session handoff: mandatory `handoff.md` at root + dated archive in `00-meta/handoffs/`.** Rolling root file for fast pickup; archive builds the learning timeline (portfolio value). "Next step" is always *one* concrete action to avoid decision paralysis. If a session ends abruptly, next session reconstructs the handoff from `git log` + recent file changes.
- **Version control: public GitHub.** Portfolio value; strict `.gitignore` and pre-commit secrets scan from commit #1. Lab IPs (`10.20.x.x`) are fine; anything else suspicious stops a commit.
- **Context-file detail level: detailed but disciplined (~50% larger than v1).** Variable rhythm means forgetting my own conventions; thoroughness offsets that.

### Tools deliberately NOT used (and why)

- **Anki** — prefer doing over memorizing; NBLM quizzes + labs serve the same role.
- **Terraform / Ansible / IaC** — later; manual first for pedagogy.
- **Splunk Cloud trial** — redundant with the full Azure lab.
- **BOTS dataset** — flagged for later (ES/hunting practice phase).
- **PowerShell for Claude Code** — Unix-first; WSL is canonical.
- **Obsidian Git / Obsidian Sync plugins** — git handled at WSL/VS Code level to avoid `.obsidian/` merge conflicts.
