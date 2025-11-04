# Project Restructuring Proposal: Internal vs Public Separation

**Date**: 2025-11-04
**Status**: Proposal
**Strategy**: `_internal/` prefix with allowlist-based filtering

---

## Executive Summary

This proposal restructures the project to cleanly separate **internal/private** content from **public** content using an `_internal/` directory. This allows easy maintenance of both private and public repositories using the allowlist strategy described in `private_to_public_clean_mirror_workflow.md`.

---

## Current Structure Issues

### Problems Identified

1. **Mixed content**: Internal project management (ADRs, session logs, agent instructions) mixed with public-facing docs
2. **Unclear boundaries**: No clear visual separation between what's internal vs public
3. **Complex allowlist**: Would require listing many individual files/folders
4. **Maintenance burden**: Easy to accidentally include internal content in public repo
5. **Scattered internal docs**: Internal content spread across multiple locations

### Current Internal Content Locations

```
├── project/                              # Internal PM, context, learnings
├── reports/                              # Internal status reports
├── AGENTS.md                             # Internal agent instructions
├── .github/copilot-instructions.md       # Internal agent instructions
├── docs/decisions/                       # Internal ADRs
├── docs/investigations/                  # Internal research
├── HOW_TO_USE.md                        # Internal starter pack guide
├── MANIFEST.txt                          # Internal file listing
├── STARTER_PACK_CONTENTS.md             # Internal documentation
└── [various setup docs at root]         # Internal setup guides
```

---

## Proposed Structure: `_internal/` Strategy

### Why `_internal/`?

1. **Python convention**: Single underscore indicates "internal use"
2. **Natural sorting**: Appears at top of directory listings
3. **Clear semantics**: Immediately obvious what it contains
4. **Simple allowlist**: Just exclude `_internal/*` from public repo
5. **Easy maintenance**: All internal content in one place

### New Directory Structure

```
project_root/
├── _internal/                           # ⚠️  ALL INTERNAL CONTENT
│   ├── project/                         # Project management
│   │   ├── context/                     # Tiered context system
│   │   │   ├── essential/               # Checklists, warnings
│   │   │   ├── situational/             # Patterns, solutions
│   │   │   ├── reference/               # Full specs
│   │   │   └── archive/                 # Historical
│   │   ├── learnings/                   # Session logs & distillations
│   │   │   ├── raw/sessions/            # Individual sessions
│   │   │   └── distilled/               # Summaries & patterns
│   │   ├── planning/                    # Roadmap, milestones
│   │   ├── backlog/                     # Work items
│   │   ├── process/                     # Team processes
│   │   ├── metrics/                     # Project metrics
│   │   ├── onboarding/                  # Team onboarding
│   │   ├── .distillation/               # Automation data
│   │   ├── AGENT_START_HERE.md          # Agent entry point
│   │   └── README.md                    # PM overview
│   │
│   ├── docs/                            # Internal documentation
│   │   ├── decisions/                   # ADRs (Architecture Decision Records)
│   │   ├── investigations/              # Research & analysis
│   │   ├── setup/                       # Internal setup guides
│   │   └── starter-pack/                # Starter pack documentation
│   │       ├── HOW_TO_USE.md
│   │       ├── MANIFEST.txt
│   │       └── STARTER_PACK_CONTENTS.md
│   │
│   ├── reports/                         # Status reports
│   │   ├── archive/                     # Archived reports
│   │   └── README.md
│   │
│   ├── scripts/                         # Internal automation scripts
│   │   ├── setup_dev_env.py
│   │   ├── generate_reports.py
│   │   └── mirror_to_public.sh          # Public repo mirror script
│   │
│   ├── .github/                         # Internal GitHub config
│   │   ├── copilot-instructions.md      # Comprehensive agent instructions
│   │   └── workflows/                   # Internal workflows
│   │       ├── publish-public.yml       # Auto-publish to public repo
│   │       └── internal-checks.yml      # Internal quality checks
│   │
│   ├── AGENTS.md                        # Quick agent reference
│   └── README.md                        # Internal repo overview
│
├── .github/                             # ✅ PUBLIC GitHub config
│   └── workflows/
│       └── ci.yml                       # Public CI/CD pipeline
│
├── docs/                                # ✅ PUBLIC documentation
│   ├── framework/                       # Methodology (if applicable)
│   ├── guides/                          # How-to guides
│   │   ├── getting-started/
│   │   ├── user-guides/
│   │   └── developer-guides/
│   ├── reference/                       # Technical reference
│   │   ├── architecture/                # Public architecture docs
│   │   ├── api/                         # API documentation
│   │   └── data-models/                 # Data models
│   ├── assets/                          # Images, diagrams
│   └── README.md                        # Documentation index
│
├── scripts/                             # ✅ PUBLIC utility scripts
│   ├── setup.py                         # Dev environment setup
│   ├── lint.py                          # Linting automation
│   ├── test.py                          # Test automation
│   └── README.md
│
├── src/                                 # ✅ PUBLIC source code
│   └── PROJECT_NAME/
│       ├── core/
│       ├── models/
│       ├── utils/
│       ├── __init__.py
│       └── __main__.py
│
├── tests/                               # ✅ PUBLIC test suite
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   ├── fixtures/
│   ├── conftest.py
│   └── __init__.py
│
├── .gitignore                           # ✅ PUBLIC (standard Python ignores)
├── .python-version                      # ✅ PUBLIC
├── CHANGELOG.md                         # ✅ PUBLIC
├── LICENSE                              # ✅ PUBLIC
├── README.md                            # ✅ PUBLIC
└── pyproject.toml                       # ✅ PUBLIC
```

---

## Migration Strategy

### Phase 1: Create `_internal/` Structure (Low Risk)

1. **Create the new directory structure**:
   ```bash
   mkdir -p _internal/{project,docs,reports,scripts,.github/workflows}
   mkdir -p _internal/docs/{decisions,investigations,setup,starter-pack}
   ```

2. **Move internal content** (safe, reversible):
   ```bash
   # Move project management
   git mv project _internal/

   # Move internal reports
   git mv reports _internal/

   # Move internal docs from docs/
   git mv docs/decisions _internal/docs/
   git mv docs/investigations _internal/docs/

   # Move agent instructions
   git mv AGENTS.md _internal/
   git mv .github/copilot-instructions.md _internal/.github/

   # Move starter pack docs
   mkdir -p _internal/docs/starter-pack
   git mv "HOW_TO_USE.md" _internal/docs/starter-pack/
   git mv "MANIFEST.txt" _internal/docs/starter-pack/
   git mv "STARTER_PACK_CONTENTS.md" _internal/docs/starter-pack/

   # Create _internal README
   cat > _internal/README.md << 'EOF'
   # Internal Repository Content

   This directory contains internal project management content that should NOT be
   included in the public repository.

   ## Contents

   - `project/` - Project management, planning, learnings
   - `docs/` - Internal documentation (ADRs, investigations, setup)
   - `reports/` - Status reports and analytics
   - `scripts/` - Internal automation scripts
   - `.github/` - Internal GitHub configurations
   - `AGENTS.md` - AI agent quick reference

   ## Important

   When publishing to the public repo, everything in `_internal/` is excluded
   via the allowlist strategy. See `../private_to_public_clean_mirror_workflow.md`.
   EOF
   ```

3. **Update references** in remaining files to point to new locations:
   - Update relative paths in markdown files
   - Update script paths
   - Update GitHub workflow paths (if any reference internal scripts)

### Phase 2: Create Public Repo Configuration

4. **Create `allowlist.txt`** in project root:
   ```bash
   # See detailed allowlist.txt below
   ```

5. **Create `public.gitignore`** in project root:
   ```bash
   # See detailed public.gitignore below
   ```

### Phase 3: Test & Validate

6. **Test the mirror process locally**:
   ```bash
   # Follow the testing steps in private_to_public_clean_mirror_workflow.md
   ```

7. **Validate public mirror**:
   - Verify no internal content leaked
   - Check all public docs still work
   - Test CI/CD pipeline
   - Verify relative links in docs

### Phase 4: Automate (Optional)

8. **Set up GitHub Action** to auto-publish to public repo:
   ```bash
   # Create .github/workflows/publish-public.yml
   # See workflow configuration below
   ```

---

## Required Files for Public Repo Strategy

### `allowlist.txt`

Create at project root:

```text
# === Root Configuration Files ===
README.md
LICENSE
CHANGELOG.md
pyproject.toml
.python-version

# === Source Code ===
src/

# === Tests ===
tests/

# === Public Documentation ===
docs/

# === Public Scripts ===
scripts/

# === Public GitHub Configuration ===
.github/workflows/ci.yml

# === Public .gitignore (renamed during export) ===
public.gitignore

# === Build/Package Files (if needed) ===
# setup.py
# requirements.txt
# Dockerfile
```

### `public.gitignore`

Create at project root (renamed to `.gitignore` in public repo):

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
.venv/
venv/
ENV/
build/
dist/
*.egg-info/
.eggs/
*.egg

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# Type checking
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
.pytype/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Environment
.env
.env.local

# Logs
*.log

# Databases
*.db
*.sqlite

# Documentation build
docs/_build/
docs/.doctrees/

# Jupyter
.ipynb_checkpoints/
*.ipynb

# OS
Thumbs.db
```

### `.github/workflows/publish-public.yml`

Create in **private repo** at `_internal/.github/workflows/publish-public.yml`:

```yaml
name: Publish to Public Mirror

on:
  push:
    branches: [ main ]
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
          git config user.name "Public Mirror Bot"
          git config user.email "bot@users.noreply.github.com"

      - name: Build & push filtered mirror
        env:
          PUBLIC_REPO_URL: ${{ secrets.PUBLIC_REPO_URL }}
        run: |
          # Work on throwaway branch
          git checkout -B export "$GITHUB_REF_NAME"

          # Filter to allowlisted paths only
          git filter-repo --force \
            --paths-from-file allowlist.txt \
            --path-rename public.gitignore:.gitignore

          # Push to public repo
          git remote add public "$PUBLIC_REPO_URL"
          git push --force public HEAD:main

          # Push tags
          git tag | xargs -I {} git push --force public {}

```

---

## Update Strategy for Existing Files

### Files that need path updates:

1. **`Python Project Structure/README.md`** (if it references internal structure)
2. **`Python Project Structure/starter_pack/README.md`** - Update structure diagram
3. **`_internal/AGENTS.md`** - Update file paths
4. **`_internal/.github/copilot-instructions.md`** - Update file paths
5. **Any scripts** that reference the old `project/` or `reports/` locations

---

## Benefits of This Structure

### 1. **Crystal Clear Separation**
- Single top-level directory contains ALL internal content
- No ambiguity about what's internal vs public
- Easy visual scanning

### 2. **Simple Allowlist**
- Just exclude `_internal/` (one line strategy)
- Everything else is public by default
- Easy to maintain and review

### 3. **Safe by Default**
- New internal content naturally goes into `_internal/`
- Harder to accidentally leak internal content
- Clear mental model for contributors

### 4. **Better Organization**
- Internal content properly categorized
- Related internal docs grouped together
- Cleaner project root

### 5. **Easier Automation**
- Simple filter rules for CI/CD
- Clear boundary for tooling
- Consistent structure across projects

---

## Alternative: `.internal/` vs `_internal/`

### `.internal/` (Hidden directory)
- **Pros**:
  - Hidden from `ls` by default
  - Follows Unix hidden file convention
- **Cons**:
  - Can be easy to forget about
  - Less discoverable for new team members
  - May be overlooked in searches

### `_internal/` (Visible with underscore)
- **Pros**: ✅
  - Always visible in listings
  - Python convention for internal
  - Clear and explicit
  - Easy to find and navigate
- **Cons**:
  - Visible in listings (but this is actually good)

**Recommendation**: Use `_internal/` for better visibility and discoverability.

---

## Implementation Checklist

- [ ] Review and approve this proposal
- [ ] Create `_internal/` directory structure
- [ ] Move internal content to `_internal/`
- [ ] Update file references and links
- [ ] Create `allowlist.txt`
- [ ] Create `public.gitignore`
- [ ] Test mirror process locally
- [ ] Validate public mirror
- [ ] Update documentation to reflect new structure
- [ ] (Optional) Set up automated publishing workflow
- [ ] Commit and push changes
- [ ] Initial publish to public repo

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Break internal links | Medium | Low | Test all docs after migration, use find/replace |
| Accidentally expose internal data | Low | High | Test mirror locally first, review allowlist |
| CI/CD breaks | Low | Medium | Keep public CI separate, test before merge |
| Team confusion | Low | Low | Clear documentation, update onboarding |

---

## Questions to Consider

1. **Do you want to use `_internal/` or `.internal/`?**
   - Recommendation: `_internal/` for visibility

2. **Should any current "internal" content be made public?**
   - Example: Some setup scripts might be useful for public users

3. **Are there any internal scripts needed by public users?**
   - Example: Development setup scripts

4. **What about the `docs/decisions/` (ADRs)?**
   - Keep private by default
   - Can selectively publish specific ADRs to public docs if desired

5. **How to handle the workflow?**
   - Manual publish vs automated CI/CD
   - Recommendation: Start manual, add automation once confident

---

## Next Steps

1. **Review this proposal** with team
2. **Decide on naming**: `_internal/` vs `.internal/`
3. **Identify any edge cases** or content that needs special handling
4. **Get approval** to proceed
5. **Execute Phase 1** (create structure, move files)
6. **Execute Phase 2** (create config files)
7. **Execute Phase 3** (test thoroughly)
8. **Execute Phase 4** (automate if desired)

---

## References

- `private_to_public_clean_mirror_workflow.md` - Complete workflow documentation
- `Python Project Structure/STARTER_PACK_CONTENTS.md` - Current structure
- Git-filter-repo docs: https://github.com/newren/git-filter-repo

---

**Status**: Ready for review
**Author**: AI Assistant
**Date**: 2025-11-04
