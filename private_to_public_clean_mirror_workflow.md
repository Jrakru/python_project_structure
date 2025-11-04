
# Private → Public **Clean Mirror** Workflow (No Leaks, No Hints)

**Last updated:** 2025-10-12

This guide shows you how to keep a **private, source‑of‑truth** repository (with PM docs, scripts, dotfiles, notes, experiments) and continuously publish a **public mirror** that looks complete and professional—**without revealing** that anything was removed.  
The public repo’s history will contain **only** the files you explicitly allow, with a curated `.gitignore` that doesn’t hint at internal paths.

---

## Table of Contents
1. [Goals & Non‑Goals](#goals--non-goals)  
2. [Architecture Overview](#architecture-overview)  
3. [Why Allow‑List (Not Deny‑List)](#why-allow-list-not-deny-list)  
4. [Prerequisites](#prerequisites)  
5. [Set Up the Private Repo](#set-up-the-private-repo)  
6. [One‑Time Initial Publish](#one-time-initial-publish)  
7. [Automate with GitHub Actions](#automate-with-github-actions)  
8. [Day‑to‑Day Workflow](#day-to-day-workflow)  
9. [Versioning, Tags, and Releases](#versioning-tags-and-releases)  
10. [Security & Compliance Guardrails](#security--compliance-guardrails)  
11. [Local Testing of the Mirror](#local-testing-of-the-mirror)  
12. [Troubleshooting](#troubleshooting)  
13. [Migrating an Existing Public Repo](#migrating-an-existing-public-repo)  
14. [Alternatives & When to Use Them](#alternatives--when-to-use-them)  
15. [FAQs](#faqs)  
16. [Appendix A: Example `allowlist.txt` Templates](#appendix-a-example-allowlisttxt-templates)  
17. [Appendix B: Bash & PowerShell Publish Scripts](#appendix-b-bash--powershell-publish-scripts)  
18. [Appendix C: GitHub Action Workflow](#appendix-c-github-action-workflow)  
19. [Appendix D: Optional Commit‑Message Scrubbing](#appendix-d-optional-commit-message-scrubbing)  
20. [Appendix E: Pre‑Commit Hooks to Enforce the Rules](#appendix-e-pre-commit-hooks-to-enforce-the-rules)

---

## Goals & Non‑Goals

**Goals**
- Keep a **private** repo with *everything* (PM docs, internal scripts, dotfiles, notes, experiments).
- Publish a **public** repo that appears complete and self‑contained.
- **No hints** in the public repo that other files exist (no revealing `.gitignore` lines, no commit messages referencing internal paths).
- Fully **repeatable** publishing (manual script and/or CI).

**Non‑Goals**
- This is not about partial open‑sourcing with “redacted files” visible in history. We **rewrite** history so internal files were **never there**.
- This does not protect against accidental secrets pushed to the **public** repo after filtering—use additional scanners (see guardrails).

---

## Architecture Overview

```
         ┌──────────────────────────────────────────┐
         │              PRIVATE REPO                │
         │  (All files: code, PM, notes, dotfiles)  │
         └───────────────┬──────────────────────────┘
                         │
                         │  filter (allow‑list)
                         ▼
        ┌───────────────────────────────────────────┐
        │          REWRITTEN EXPORT (temp)          │
        │  - drop non‑allowlisted paths             │
        │  - rename public.gitignore → .gitignore   │
        │  - optional: scrub commit messages        │
        └───────────────────┬───────────────────────┘
                            │  force‑push
                            ▼
        ┌───────────────────────────────────────────┐
        │             PUBLIC MIRROR REPO            │
        │  (Only allowed content + clean history)   │
        └───────────────────────────────────────────┘
```

We use [`git-filter-repo`](https://github.com/newren/git-filter-repo), the modern, fast, safe replacement for `git filter-branch`.

---

## Why Allow‑List (Not Deny‑List)

- A **deny‑list** is risky: new internal files could slip into the public mirror if you forget to add exclusions.
- An **allow‑list** is safe by default: only known, reviewed paths are exported.

> TL;DR — **Always** maintain an `allowlist.txt`.

---

## Prerequisites

- Git (2.30+ recommended)
- Python 3.8+ for installing `git-filter-repo`
- GitHub (or GitLab/Gitea) repos:
  - `private-repo` — your canonical repo (all files).
  - `public-repo` — an empty repository for the mirror.

**Install `git-filter-repo`:**

**Linux/macOS**
```bash
python3 -m pip install --user git-filter-repo
# or: pipx install git-filter-repo
# or Homebrew (macOS): brew install git-filter-repo
```

**Windows (PowerShell)**
```powershell
py -m pip install --user git-filter-repo
```

> Verify: `git filter-repo --help`

---

## Set Up the Private Repo

Create these files **in the private repo**:

**`allowlist.txt`**
```text
# === core ===
README.md
LICENSE

# === app code (examples) ===
src/
app/
packages/

# === build + config you want public ===
pyproject.toml
package.json
package-lock.json
pnpm-lock.yaml
Cargo.toml
go.mod
Dockerfile

# === CI that is safe to publish ===
.github/workflows/ci.yml

# === the public .gitignore (renamed during export) ===
public.gitignore
```

**`public.gitignore`**
```gitignore
# Editor/OS/build noise only (no hints about internal files)
__pycache__/
*.py[cod]
*.log
.DS_Store
dist/
build/
.venv/
.env
.vscode/
.idea/
node_modules/
coverage/
```

> **Rule of thumb:** Never mention internal folders (e.g., `/pm/`, `/docs-internal/`) in `public.gitignore`. We’ll rename `public.gitignore` → `.gitignore` during export.

---

## One‑Time Initial Publish

Use either the **Bash** or **PowerShell** script (see [Appendix B](#appendix-b-bash--powershell-publish-scripts)).

**Quick Bash version:**
```bash
#!/usr/bin/env bash
set -euo pipefail

PRIVATE_REMOTE="git@github.com:YOU/private-repo.git"
PUBLIC_REMOTE="git@github.com:YOU/public-repo.git"
BRANCH="main"

workdir="$(mktemp -d)"; trap 'rm -rf "$workdir"' EXIT

# Clone a bare mirror of the private repo
git clone --mirror "$PRIVATE_REMOTE" "$workdir/repo.git"
cd "$workdir/repo.git"

# Ensure allowlist/public.gitignore exist on the branch
mkdir -p "$workdir/wt"
git --git-dir="$PWD" --work-tree="$workdir/wt" checkout "$BRANCH" -- allowlist.txt public.gitignore

# Rewrite history to include only allowlisted paths; rename public.gitignore → .gitignore
git filter-repo --force \
  --paths-from-file "$workdir/wt/allowlist.txt" \
  --path-rename public.gitignore:.gitignore

# Push rewritten history to the public repo
git remote add public "$PUBLIC_REMOTE"
git push --force --all public
git push --force --tags public
```

**Result:** The public repo now contains only allowed files, a clean `.gitignore`, and **no history leakage**.

---

## Automate with GitHub Actions

Create a workflow in the **private** repo to republish whenever main changes.  
See [Appendix C](#appendix-c-github-action-workflow) for the full YAML.

### Auth Options
- **Deploy key** on the public repo (read/write) and add it to the private repo’s Action as an SSH key.
- **PAT** (personal access token) with `repo` scope stored as `PUBLIC_REPO_URL` secret, e.g. `https://<token>@github.com/YOU/public-repo.git`.

### Important
- Use `actions/checkout@v4` with `fetch-depth: 0` to get full history (filtering requires full history).
- Force‑push to the public repo’s `main` after filtering.

---

## Day‑to‑Day Workflow

1. Work normally in **private** repo.
2. Update `allowlist.txt` whenever you add/remove public files or directories.
3. Commit as usual; CI publishes the filtered mirror automatically (or run the script manually).
4. Review the **public** repo after publication (spot‑check files, CI status badge, etc.).

---

## Versioning, Tags, and Releases

- **Tags:** By default, the script pushes all tags. If you want selective tags:
  ```bash
  git push --force public v1.2.3
  ```
- **Release notes:** Write release notes in a public‑safe manner (avoid internal path references).
- **Version files:** Keep versioned artifacts (e.g., `CHANGELOG.md`) **allowlisted**.

---

## Security & Compliance Guardrails

- **Never add secrets** to allowlisted files.
- Add a **secrets scanner** to the private repo *and* the public repo (e.g., Gitleaks, GitHub secret scanning).
- Optionally **scrub commit messages** during export to remove internal URLs or ticket IDs (see [Appendix D](#appendix-d-optional-commit-message-scrubbing)).
- Consider a **pre‑commit** or **pre‑push** hook to assert the allowlist contains exactly what you expect (see [Appendix E](#appendix-e-pre-commit-hooks-to-enforce-the-rules)).

> If a secret is ever exposed, **rotate** it. History rewriting alone is not sufficient.

---

## Local Testing of the Mirror

Test the end‑to‑end flow without touching GitHub:

```bash
# From your private repo root:
tmp="$(mktemp -d)"
git clone --mirror . "$tmp/mirror.git"
cd "$tmp/mirror.git"

# Ensure files exist on branch:
mkdir -p "$tmp/wt"
git --git-dir="$PWD" --work-tree="$tmp/wt" checkout main -- allowlist.txt public.gitignore

git filter-repo --force \
  --paths-from-file "$tmp/wt/allowlist.txt" \
  --path-rename public.gitignore:.gitignore

# Inspect result
git clone . ../public-inspect
ls -la ../public-inspect
```

---

## Troubleshooting

- **`git: 'filter-repo' is not a git command`**  
  Install it (`pip install git-filter-repo`) and ensure your Python user bin dir is on `PATH`.

- **Only top‑level files exported, subdirs missing**  
  `allowlist.txt` uses **prefix matching**. Include directory names with trailing slash (e.g., `src/`).

- **Action fails with shallow history**  
  Use `actions/checkout@v4` with `fetch-depth: 0`.

- **Strange commit messages in public**  
  Use the message scrubber (Appendix D).

- **Windows path issues**  
  Prefer WSL for the export step or use the PowerShell script in Appendix B.

- **“fatal: refusing to merge unrelated histories”**  
  First push can be forced; subsequent pushes must continue rewriting from the same private history base.

---

## Migrating an Existing Public Repo

If you already have a public repo with “leaky” history:
1. Back it up (clone and archive).
2. Run the export process and **force‑push** the rewritten history.
3. Communicate a one‑time history rewrite to public users if needed (optional).

---

## Alternatives & When to Use Them

- **`git archive` / `rsync` → single commit**  
  Simple one‑shot exports with no history; useful for **releases** but not for ongoing mirrored history.

- **Subtree or submodule split**  
  Good when your public content is a clearly separated subtree. Still doesn’t hide that other content exists.

- **Sparse‑checkout**  
  Great for local dev, **not** for publishing: it does **not** rewrite history or hide files.

**Best for “no hints, no leaks”** remains: **allow‑listed history rewrite** via `git-filter-repo`.

---

## FAQs

**Q: Can the public repo tell that content was removed?**  
A: No — its history is rewritten to never include those files. No `.gitignore` hints either.

**Q: Do I need to run this on every branch?**  
A: Typically only your public branch (e.g., `main`). You can export other branches if desired.

**Q: Can I keep internal CI while exporting a smaller public CI?**  
A: Yes. Put a public‑safe workflow under `.github/workflows/ci.yml` and allow‑list it.

**Q: Can I push only selected tags/releases?**  
A: Yes; push the ones you choose (see “Versioning”).

---

## Appendix A: Example `allowlist.txt` Templates

### Python (library/app)
```text
README.md
LICENSE
pyproject.toml
setup.cfg
src/
tests/            # optional if you publish tests
public.gitignore
.github/workflows/ci.yml
```

### Node / Next.js
```text
README.md
LICENSE
package.json
pnpm-lock.yaml
next.config.js
src/
app/
public/
public.gitignore
.github/workflows/ci.yml
```

### Rust
```text
README.md
LICENSE
Cargo.toml
Cargo.lock
src/
public.gitignore
.github/workflows/ci.yml
```

### Go
```text
README.md
LICENSE
go.mod
go.sum
cmd/
pkg/
internal/        # include only if safe
public.gitignore
.github/workflows/ci.yml
```

### Data Science / Notebooks (cautious!)
```text
README.md
LICENSE
environment.yml
requirements.txt
src/
notebooks/       # only if scrubbed
public.gitignore
.github/workflows/ci.yml
```

### Monorepo (selective packages)
```text
README.md
LICENSE
packages/pkg-a/
packages/pkg-b/
tooling/eslint.config.js
public.gitignore
.github/workflows/ci.yml
```

---

## Appendix B: Bash & PowerShell Publish Scripts

### `publish-public.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# === CONFIG ===
PRIVATE_REMOTE="{{YOUR_PRIVATE_REMOTE}}"   # e.g., git@github.com:YOU/private-repo.git
PUBLIC_REMOTE="{{YOUR_PUBLIC_REMOTE}}"     # e.g., git@github.com:YOU/public-repo.git
BRANCH="{{YOUR_PRIVATE_BRANCH:-main}}"

workdir="$(mktemp -d)"; trap 'rm -rf "$workdir"' EXIT

echo "[i] Cloning mirror of private repo..."
git clone --mirror "$PRIVATE_REMOTE" "$workdir/repo.git"
cd "$workdir/repo.git"

echo "[i] Extracting allowlist and public.gitignore from $BRANCH ..."
mkdir -p "$workdir/wt"
git --git-dir="$PWD" --work-tree="$workdir/wt" checkout "$BRANCH" -- allowlist.txt public.gitignore

echo "[i] Filtering history..."
git filter-repo --force \
  --paths-from-file "$workdir/wt/allowlist.txt" \
  --path-rename public.gitignore:.gitignore

echo "[i] Pushing to public..."
git remote add public "$PUBLIC_REMOTE" || true
git push --force --all public
git push --force --tags public

echo "[✓] Done."
```

### `publish-public.ps1`
```powershell
Param(
  [Parameter(Mandatory=$true)][string]$PrivateRemote,
  [Parameter(Mandatory=$true)][string]$PublicRemote,
  [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"
$workdir = New-Item -ItemType Directory -Path ([System.IO.Path]::GetTempPath()) -Name ("pub_" + [System.Guid]::NewGuid().ToString())

try {
  Write-Host "[i] Cloning mirror of private repo..."
  git clone --mirror $PrivateRemote "$workdir\repo.git"
  Set-Location "$workdir\repo.git"

  Write-Host "[i] Extracting allowlist and public.gitignore from $Branch ..."
  New-Item -ItemType Directory -Path "$workdir\wt" | Out-Null
  git --git-dir="$pwd" --work-tree="$workdir\wt" checkout $Branch -- allowlist.txt public.gitignore

  Write-Host "[i] Filtering history..."
  git filter-repo --force `
    --paths-from-file "$workdir\wt\allowlist.txt" `
    --path-rename public.gitignore:.gitignore

  Write-Host "[i] Pushing to public..."
  git remote add public $PublicRemote 2>$null
  git push --force --all public
  git push --force --tags public

  Write-Host "[✓] Done."
}
finally {
  Set-Location $PSScriptRoot
  Remove-Item -Recurse -Force $workdir
}
```

---

## Appendix C: GitHub Action Workflow

Create in **private** repo: `.github/workflows/publish-public.yml`

```yaml
name: Publish Public Mirror
on:
  push:
    branches: [ main ]  # adjust if needed
  workflow_dispatch: {}

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout full history
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install git-filter-repo
        run: python3 -m pip install --user git-filter-repo

      - name: Configure Git
        run: |
          git config user.name "Mirror Bot"
          git config user.email "mirror-bot@users.noreply.github.com"

      - name: Build & push filtered mirror
        env:
          PUBLIC_REPO_URL: ${{ secrets.PUBLIC_REPO_URL }}  # e.g. https://<token>@github.com/YOU/public-repo.git
        run: |
          # Work on a throwaway branch to avoid mutating origin
          git checkout -B export "$GITHUB_REF_NAME"

          git filter-repo --force             --paths-from-file allowlist.txt             --path-rename public.gitignore:.gitignore

          git remote add public "$PUBLIC_REPO_URL" || true
          git push --force public HEAD:main
          # Push tags if desired:
          git tag | xargs -I {{}} git push --force public {{}}
```

> Save `PUBLIC_REPO_URL` as an Actions secret; it must include credentials or use a deploy key.

---

## Appendix D: Optional Commit‑Message Scrubbing

If your commit messages mention internal folder names, ticket systems, or URLs, you can scrub them during export.

Create `message_scrubber.py` in the repo root:
```python
import re

PATTERNS = [
    (re.compile(rb"docs-internal/[^\s]*"), b""),
    (re.compile(rb"\bpm/[^\s]*"), b""),
    (re.compile(rb"https?://internal\.[^\s]+"), b""),
    (re.compile(rb"\bJIRA-\d+\b"), b""),  # example
]

def rewrite_message(message, metadata):
    for pat, repl in PATTERNS:
        message = pat.sub(repl, message)
    # Optional: normalize excessive whitespace
    message = re.sub(rb"\s{3,}", b"  ", message)
    return message
```

Use it with `git-filter-repo`:
```bash
git filter-repo --force   --paths-from-file allowlist.txt   --path-rename public.gitignore:.gitignore   --message-callback 'from message_scrubber import rewrite_message as f; message=f(message, metadata)'
```

> Keep patterns conservative to avoid mangling legitimate messages.

---

## Appendix E: Pre‑Commit Hooks to Enforce the Rules

**Pre‑commit config** (optional) to block accidental allow‑list drift and scan for secrets:

`.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/zricethezav/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
  - repo: local
    hooks:
      - id: ensure-allowlist-present
        name: Ensure allowlist present
        entry: bash -c 'test -f allowlist.txt'
        language: system
        pass_filenames: false
```

**Simple pre-push guard** (optional): `.git/hooks/pre-push`
```bash
#!/usr/bin/env bash
set -euo pipefail
if ! grep -qE '^[^#]+' allowlist.txt; then
  echo "allowlist.txt is empty or missing entries. Aborting push."
  exit 1
fi
```
(Make it executable: `chmod +x .git/hooks/pre-push`.)

---

## Final Checklist

- [ ] `allowlist.txt` contains only safe, intended paths.  
- [ ] `public.gitignore` lists only generic noise (no internal path hints).  
- [ ] One‑time export ran and public repo looks correct.  
- [ ] CI workflow added with `fetch-depth: 0` and authenticated push.  
- [ ] (Optional) Message scrubber configured.  
- [ ] (Optional) Pre‑commit hooks & secret scanning enabled.

---

**You’re set.** Your public repo will stay clean and professional, and your private repo remains your full working cockpit—without leaking that anything is missing.
