# Install Checklist — Splunk Journey Setup

Phase-by-phase setup. Work top to bottom. **Don't skip the gotchas.**

---

## Phase 1 — WSL2 / Ubuntu side (in your WSL terminal)

### 1.1 Verify WSL2 is healthy

```powershell
# From PowerShell (Windows side)
wsl -l -v
```

You should see `Ubuntu` (or similar) with `VERSION 2`. If it says VERSION 1: `wsl --set-version Ubuntu 2`.

### 1.2 Update Ubuntu and install essentials

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl unzip wget tree jq ripgrep
```

`tree` is used by Claude Code to show folder structures. `jq` and `ripgrep` are general-purpose helpers you'll want.

### 1.3 Install nvm + Node.js LTS

**Critical:** do *not* use Ubuntu's default `apt install nodejs` — versions are old. Don't use Windows Node.js from WSL either. Use nvm.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts
node --version    # should be v20.x or v22.x
npm --version
```

### 1.4 Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

**Do NOT use `sudo`** with this. If you get an EACCES permission error, your nvm setup is off — fix that first.

### 1.5 Authenticate Claude Code

```bash
claude
```

This opens a browser. Log in with your Claude Pro/Max account. You need a paid plan — the free tier doesn't include Claude Code.

### 1.6 Health check

```bash
claude doctor
```

Should report green across the board.

### 1.7 Install Azure CLI

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az --version
az login    # browser-based login to your Azure subscription
az account show    # verify the right subscription is selected
```

### 1.8 Install GitHub CLI (for repo push later)

```bash
sudo apt install -y gh
gh auth login    # follow prompts, choose SSH
```

### 1.9 Add a project alias to bash

This saves typing the long `/mnt/c/...` path every session. Replace `<YOUR_USERNAME>` with your Windows username:

```bash
echo "alias splunk='cd /mnt/c/Users/<YOUR_USERNAME>/Documents/splunk-journey'" >> ~/.bashrc
source ~/.bashrc
```

Type `splunk` from anywhere in WSL to jump to the repo.

If you don't know your Windows username:
```bash
cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r'
```

---

## Phase 2 — Windows side

### 2.1 Windows Terminal

Microsoft Store → install **Windows Terminal**. Set Ubuntu (WSL) as default profile. Much better experience than the legacy console.

### 2.2 VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/). During install:
- Tick "Add to PATH"
- Tick "Register Code as editor"
- Tick "Add 'Open with Code' action to Explorer context menu"

### 2.3 VS Code extensions

Open VS Code → Extensions panel → install:

| Extension | Why |
|---|---|
| **WSL** (Microsoft) | Develop inside WSL natively |
| **Claude Code** (Anthropic) | IDE integration with the Claude CLI |
| **Markdown All in One** | Better markdown editing |
| **Markdown Preview Mermaid Support** | Render mermaid diagrams inline |
| **GitLens** | Strong git visualization |
| **YAML** | Syntax for any YAML configs |
| **Even Better TOML** | If you touch Splunk's newer TOML configs |
| **Code Spell Checker** | Catches typos in notes you'll publish |

### 2.4 Obsidian

Download from [obsidian.md](https://obsidian.md/). Install normally. **Don't create a vault yet** — we point it at the repo in Phase 4.

### 2.5 Notion (optional surface)

Desktop app from [notion.so/desktop](https://www.notion.so/desktop). Sign in. Per your decision: this is for polished/mobile review only; Obsidian is the source of truth.

### 2.6 Git for Windows

Download from [git-scm.com/download/win](https://git-scm.com/download/win). Mainly for Git Credential Manager — handles GitHub auth cleanly across both Windows and WSL.

### 2.7 SSH key for GitHub

```bash
# In WSL
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copy the public key → GitHub → Settings → SSH and GPG keys → New SSH key → paste.

Test: `ssh -T git@github.com` (should greet you by username).

---

## Phase 3 — Workspace setup

### 3.1 Create the project folder (Windows side)

The repo lives on the Windows filesystem so Obsidian indexes cleanly. WSL accesses it via `/mnt/c/`.

```bash
# From WSL
mkdir -p /mnt/c/Users/<YOUR_USERNAME>/Documents/splunk-journey
cd /mnt/c/Users/<YOUR_USERNAME>/Documents/splunk-journey
# or just: splunk     (if you set the alias)
```

### 3.2 Configure git identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
```

### 3.3 Initialize the repo

```bash
git init
```

### 3.4 Drop in the bootstrap files

Copy these into the repo root:
- `CLAUDE.md`
- `master-prompt.md`
- `.gitignore`
- `README.md`
- `install-checklist.md` (this file)

Copy these into `00-meta/` (create the folder first):
- `chat-summary.md`
- `obsidian-setup.md`
- `notebooklm-workflow.md`
- `roadmap.md`

```bash
mkdir -p 00-meta
# then move/copy the files into place
```

### 3.5 Open in VS Code from WSL

```bash
code .
```

VS Code opens. Bottom-left corner should show **WSL: Ubuntu**. If it shows a Windows path, something's off — close and reopen via `code .` from WSL.

### 3.6 Launch Claude Code

Inside VS Code, open the integrated terminal (Ctrl+`). Confirm it's a WSL terminal. Then:

```bash
claude
```

On first launch in this folder, paste the contents of `master-prompt.md` as your first message. Claude Code will read `CLAUDE.md`, then `00-meta/chat-summary.md`, then create the full folder structure and seed files.

---

## Phase 4 — Obsidian vault

### 4.1 Point Obsidian at the repo

Open Obsidian → **Open folder as vault** → browse to `C:\Users\<YOU>\Documents\splunk-journey\`. Click **Trust author and enable plugins**.

### 4.2 Install Obsidian plugins

Round 1 (now): **Templater**, **Dataview**, **Advanced Tables**, **Mermaid Tools**.
Round 2 (later): **Excalidraw**, **Mind Map**, **Tag Wrangler**, **Kanban**.

See `00-meta/obsidian-setup.md` for full vault config, template structures, and recommended hotkeys.

---

## Phase 5 — Verify everything works

Before your first real study session:

- [ ] `claude doctor` in WSL → all green
- [ ] `code .` from WSL opens VS Code with WSL indicator
- [ ] `claude` runs inside VS Code's integrated terminal
- [ ] Obsidian opens the repo as a vault and shows files in the file pane
- [ ] Notion is signed in (if using)
- [ ] `git status` in repo shows expected output
- [ ] `az account show` returns your Azure subscription info
- [ ] `ssh -T git@github.com` greets you by username
- [ ] `splunk` alias jumps to the repo
- [ ] `tree -L 2` works (lists folder structure)

If any of these fail, fix them **before** you start studying.

---

## Gotchas (read these once now)

1. **Don't run `npm install` on `/mnt/c/`.** It's fine for our notes/transcripts workload but glacial for projects with thousands of files. For dev work do it in `~/projects/`.
2. **Obsidian sometimes leaves `.trash/` and `.obsidian/workspace.json` dirty.** The `.gitignore` handles this — don't `git add .` blindly anyway, use `git add -p` or review staged changes.
3. **WSL clock can drift** after laptop sleep, breaking `az login`. Fix: `sudo hwclock --hctosys`, or restart WSL (`wsl --shutdown` in PowerShell, then reopen).
4. **Don't run `claude` from a path with spaces** if you can avoid it. `Documents` is fine, `My Drive (Google)` is not.
5. **Auto-shutdown every Azure VM** from creation. Azure built-in feature, set to ~23:00 your local. Or get a bill that ruins your week.
6. **Public repo means public secrets exposure** if you slip. Use the pre-commit scan in `CLAUDE.md` every single commit until it's reflex.

---

## After Phase 5: first real session

1. Paste `master-prompt.md` content into Claude Code (one time only).
2. Verify the folder structure Claude built matches your expectation.
3. Drop your Udemy transcripts into `02-course-saif/transcripts/` in the right theme subfolders.
4. `git add . && git commit -m "Initial repo structure and bootstrap"`
5. Create public GitHub repo and push:
   ```bash
   gh repo create splunk-journey --public --source=. --remote=origin --description "Splunk learning journey: TDE → SIEM Architect"
   git push -u origin main
   ```
6. Start your first lab journal entry: `05-labs/journal/YYYY-MM-DD-setup-complete.md`.
7. Start Saif lecture 1.
