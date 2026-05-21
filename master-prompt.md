# Master Prompt — First Claude Code Session

**Instructions for me (the human):** Paste the block below into Claude Code in your *first* session, after you've placed the bootstrap files into the repo directory. Claude Code reads them and builds the rest.

**Prerequisites before pasting:**
- Repo folder exists at `/mnt/c/Users/<me>/Documents/splunk-journey/` (or your equivalent)
- These files are at root: `CLAUDE.md`, `master-prompt.md`, `.gitignore`, `README.md`, `install-checklist.md`
- These files are in `00-meta/`: `chat-summary.md`, `obsidian-setup.md`, `notebooklm-workflow.md`, `roadmap.md`
- `git init` has been run
- Claude Code is launched (`claude`) inside the repo folder

---

## The prompt to paste

```
I'm starting a long-running learning project. This is the bootstrap session. Read this entire prompt, then read CLAUDE.md, then read 00-meta/chat-summary.md, 00-meta/roadmap.md, and 00-meta/notebooklm-workflow.md, THEN do anything else. Ask clarifying questions if files contradict this prompt — don't guess.

## Context

I'm an experienced Threat Detection Engineer (1+ year Splunk, daily SPL/correlation rule work) moving toward becoming a SIEM Architect. Short-term: pass SPLK-1002 (Power User) and SPLK-1003 (Admin). Mid-term: SPLK-3001 (ES Admin). Long-term: SIEM Architect role.

Starting with Saif Al-Shoker's "Complete Splunk Enterprise Certified Admin Course (NEW)" on Udemy. 10.5 hours, 68 lectures, transcripts already extracted. Lab is on Azure paid subscription, building a full distributed architecture (3-IDX cluster + 3-SHC + supporting components). Manual build, no IaC yet.

CLAUDE.md has my full profile, conventions, and how I want you to interact with me. chat-summary.md has the entire conversation history that led to this setup. roadmap.md has the phase/chapter plan. notebooklm-workflow.md describes how I produce NBLM outputs from this repo.

## What I need you to do in this session, in order

1. Read CLAUDE.md thoroughly. Confirm you understand the conventions before proceeding. Specifically confirm you understand:
   - The hybrid note-taking style
   - The handoff protocol (mandatory)
   - The pre-commit secrets scan
   - That I'm not a beginner — skip SPL/analyst-level explanations
   - That NotebookLM is a production target, not just review

2. Read 00-meta/chat-summary.md. This is the canonical history — every decision and rationale.

3. Read 00-meta/roadmap.md. Know what phase I'm in (Phase 0 — Setup, transitioning to Phase 1 — Foundations).

4. Read 00-meta/notebooklm-workflow.md. Understand how NBLM bundles are structured and when to suggest creating one.

5. Create the folder structure documented in CLAUDE.md if it doesn't exist:
   - 00-meta/
   - 00-meta/handoffs/
   - 00-meta/templates/
   - 01-architecture/
   - 02-course-saif/transcripts/
   - 02-course-saif/notes/
   - 03-topics/
   - 04-concepts/
   - 05-labs/runbooks/
   - 05-labs/configs/
   - 05-labs/journal/
   - 05-labs/azure-setup/
   - 06-supplementary/
   - 07-practice-exam/
   - 08-references/
   - 99-notebooklm/

6. In each top-level folder, create a README.md with one paragraph explaining what goes there. Use the table in CLAUDE.md as the source of truth. Don't pad — one paragraph.

7. Create 00-meta/decisions-log.md. Seed it with the decisions documented in chat-summary.md, formatted as dated entries. Use today's date for the first entry covering "initial setup decisions."

8. Create 01-architecture/target-architecture.md. Reconstruct the Splunk ES + UBA Azure diagram from chat-summary.md (it includes the full mermaid source). Add sections for:
   - Subnet purpose and CIDR table
   - Component-to-role mapping
   - Identified course gaps that the architecture exposes (clustering, MC, ES, UBA)
   - Planned NSG rules (one bullet per direction, leave the actual rules as TBD)

9. Create 02-course-saif/course-index.md. Populate it with the full 68-lecture TOC from chat-summary.md. Group by theme as documented. Add a checkbox per lecture so I can track progress. At the top, link to roadmap.md.

10. Create the subfolder skeleton for 02-course-saif/transcripts/ matching the themes (see chat-summary.md for the theme list). Add a one-line README in each saying which lecture range belongs there:
    - 01-fundamentals/
    - 02-install-bestpractices/
    - 03-apps-configs-layering/
    - 04-indexes-buckets/
    - 05-users-ldap/
    - 06-forwarders-distributed/
    - 07-data-flow-concepts/
    - 08-deployment-server/
    - 09-data-inputs/
    - 10-capstone-lab/
    - 11-data-onboarding/

11. Create 00-meta/templates/ with these template files (full structure in obsidian-setup.md):
    - lecture-note.md
    - topic-synthesis.md
    - lab-journal-entry.md
    - runbook.md
    - concept-atom.md
    - nblm-bundle-readme.md (NBLM bundle index)

12. Create the initial handoff.md at the repo root using the structure in CLAUDE.md. Populate with:
    - Current goal: "Bootstrap repo and start Phase 1 of roadmap"
    - Phase: Phase 0 → transitioning to Phase 1
    - Course progress: 0 / 68 lectures
    - Lab status: Azure subscription only, no VMs provisioned
    - What I did this session: bootstrap actions you took
    - Next step: ONE concrete action — "Drop Udemy transcripts into 02-course-saif/transcripts/ subfolders, then watch Saif lecture 1"

13. Verify .gitignore is in place at the root. If missing, create it from the template in chat-summary.md.

14. Run `git status`. Tell me what's staged for the initial commit.

15. Show me a tree of what you created: `tree -L 3 -I 'node_modules|.obsidian'` (or equivalent). Be thorough.

16. Stop. Don't commit. Wait for my next instruction.

## Rules for this session and every future session

- Be direct. No preamble, no "great question," no emojis, no closing summaries unless I ask.
- I'm not a beginner. Skip SPL basics and analyst-level concepts.
- Lab-first thinking: when explaining a concept, suggest the exercise that proves I understand it.
- I'm on Windows + WSL2. Repo lives at /mnt/c/Users/<me>/Documents/splunk-journey/.
- PUBLIC GitHub repo. Run the pre-commit scan from CLAUDE.md before any commit. Lab IPs (10.20.x.x) are fine; flag anything else suspicious.
- Push back honestly when I'm wrong.
- If something contradicts CLAUDE.md, ask before acting.
- **Session handoff is mandatory.** Start of every future session: read handoff.md, brief me. End of session (or when I signal wrap-up): archive old handoff.md to 00-meta/handoffs/, write fresh one at root. Follow the structure in CLAUDE.md exactly.
- **NotebookLM prompts:** when I finish a course theme or topic synthesis, prompt me to bundle for NBLM. Don't bundle unprompted.
- **VM cost reminders:** any time I describe provisioning an Azure VM, remind me to enable auto-shutdown unless I confirm I already did.

Begin.
```

---

## After the first session

1. Verify Claude Code built the folder structure correctly. Spot-check 3-4 README.md files. Open `01-architecture/target-architecture.md` and confirm the mermaid diagram renders.

2. Drop your extracted Udemy transcripts into `02-course-saif/transcripts/` in the appropriate theme subfolders.

3. Make your first commit:
   ```bash
   git add .
   git commit -m "Initial repo structure and bootstrap files"
   ```

4. Create the public GitHub repo and push:
   ```bash
   gh repo create splunk-journey --public --source=. --remote=origin \
     --description "Splunk learning journey: TDE → SIEM Architect"
   git push -u origin main
   ```

5. Open Obsidian, point at the repo folder as vault, configure per `00-meta/obsidian-setup.md`.

6. Write your first lab journal entry: `05-labs/journal/YYYY-MM-DD-setup-complete.md`. Use the template in `00-meta/templates/`.

---

## Future session opener

You don't need to re-paste the master prompt. For subsequent sessions:

> "Read handoff.md and brief me."

Claude reads `CLAUDE.md`, then `handoff.md`, then catches you up. When you're done:

> "Wrap up — update the handoff."

Claude archives the current `handoff.md`, writes a fresh one, shows it for approval.

---

## Specialized session openers (use when relevant)

- **Resume after long gap (1+ week):** "I've been away. Catch me up — read handoff.md, scan git log, scan the last 3 journal entries, then brief me."
- **Start a topic synthesis:** "Help me write a synthesis note in 03-topics/ for `<topic>`. Reference the relevant transcripts and any lab work."
- **Prepare a NBLM bundle:** "I'm done with `<theme>`. Bundle for NBLM — see 00-meta/notebooklm-workflow.md."
- **Lab journal entry:** "Start a lab journal entry for today. The focus is `<focus>`."
- **Pre-commit audit:** "I'm about to commit. Run the secrets scan and show me what's staged."
- **Roadmap check:** "Where am I in roadmap.md? What should I focus on next?"
