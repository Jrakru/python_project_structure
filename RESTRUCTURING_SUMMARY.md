# Project Restructuring Summary

**Quick Reference Guide for Implementation**

---

## What We're Doing

Moving ALL internal content into a single `_internal/` directory to cleanly separate private repository content from public repository content.

---

## Key Changes

### Before:
```
project_root/
├── project/                    # Internal (scattered)
├── reports/                    # Internal (scattered)
├── docs/                       # Mixed (some internal, some public)
├── AGENTS.md                   # Internal (at root)
├── .github/copilot-instructions.md  # Internal (mixed)
└── [other mixed content]
```

### After:
```
project_root/
├── _internal/                  # ALL internal content here
│   ├── project/
│   ├── reports/
│   ├── docs/
│   ├── scripts/
│   ├── .github/
│   └── AGENTS.md
├── src/                        # PUBLIC
├── tests/                      # PUBLIC
├── docs/                       # PUBLIC (user-facing only)
└── [public content]            # PUBLIC
```

---

## The Strategy: Allowlist-Based Filtering

**Private Repo** (this one):
- Contains EVERYTHING (both internal and public content)
- Develop normally here

**Public Repo** (mirror):
- Contains ONLY allowlisted files
- Generated automatically using `git-filter-repo`
- No history of internal files (clean history)

---

## Three Core Files

### 1. `allowlist.txt` ✅ CREATED
- Lists ONLY files/directories to include in public repo
- Uses prefix matching (e.g., `src/` includes all of src/)
- Anything NOT listed is excluded
- `_internal/` is NOT in this list (so it's automatically excluded)

### 2. `public.gitignore` ✅ CREATED
- Renamed to `.gitignore` in the public repo
- Contains only generic Python ignores
- NO references to internal paths (keeps public repo clean)

### 3. `RESTRUCTURING_PROPOSAL.md` ✅ CREATED
- Complete implementation plan
- Migration strategy
- Benefits and risk assessment
- Step-by-step instructions

---

## What Goes Where

### ❌ Internal (goes in `_internal/`):
- Project management (planning, backlog, metrics)
- Context system (checklists, warnings, patterns)
- Session learnings and distillations
- ADRs (Architecture Decision Records)
- Internal investigations and research
- Status reports
- Internal scripts and automation
- Agent instructions (AGENTS.md, copilot-instructions.md)
- Starter pack documentation
- Internal workflows

### ✅ Public (stays at root):
- Source code (`src/`)
- Tests (`tests/`)
- User-facing documentation (`docs/`)
- Public scripts (`scripts/`)
- Standard files (README, LICENSE, CHANGELOG, etc.)
- Public CI/CD (`.github/workflows/ci.yml`)
- Package configuration (`pyproject.toml`)

---

## Implementation Steps

### Step 1: Create Structure
```bash
mkdir -p _internal/{project,docs,reports,scripts,.github/workflows}
mkdir -p _internal/docs/{decisions,investigations,setup,starter-pack}
```

### Step 2: Move Content
```bash
# Move internal directories
git mv project _internal/
git mv reports _internal/

# Move internal docs
git mv docs/decisions _internal/docs/
git mv docs/investigations _internal/docs/

# Move agent files
git mv AGENTS.md _internal/
git mv .github/copilot-instructions.md _internal/.github/

# Move starter pack docs
git mv "HOW_TO_USE.md" _internal/docs/starter-pack/
git mv "MANIFEST.txt" _internal/docs/starter-pack/
git mv "STARTER_PACK_CONTENTS.md" _internal/docs/starter-pack/
```

### Step 3: Update References
- Update paths in markdown files
- Update script paths
- Update workflow paths

### Step 4: Test Locally
```bash
# Test the mirror process without pushing
tmp="$(mktemp -d)"
git clone --mirror . "$tmp/mirror.git"
cd "$tmp/mirror.git"

mkdir -p "$tmp/wt"
git --git-dir="$PWD" --work-tree="$tmp/wt" checkout main -- allowlist.txt public.gitignore

git filter-repo --force \
  --paths-from-file "$tmp/wt/allowlist.txt" \
  --path-rename public.gitignore:.gitignore

# Inspect result
git clone . ../public-inspect
ls -la ../public-inspect
```

### Step 5: Publish to Public Repo
```bash
# Manual one-time publish (see private_to_public_clean_mirror_workflow.md)
# Or set up automated workflow (optional)
```

---

## Benefits

1. **Crystal Clear Separation**: One directory contains ALL internal content
2. **Simple Allowlist**: Just exclude `_internal/` (one line strategy)
3. **Safe by Default**: Hard to accidentally leak internal content
4. **Better Organization**: Internal content properly categorized
5. **Easier Automation**: Clear boundary for tooling

---

## Files Created

1. ✅ `RESTRUCTURING_PROPOSAL.md` - Detailed implementation plan
2. ✅ `allowlist.txt` - Public repo allowlist configuration
3. ✅ `public.gitignore` - Public repo gitignore (will be renamed)
4. ✅ `RESTRUCTURING_SUMMARY.md` - This quick reference

---

## Next Actions

1. **Review** the proposal with your team
2. **Decide** on `_internal/` vs `.internal/` (recommend `_internal/`)
3. **Identify** any edge cases or special content
4. **Get approval** to proceed
5. **Execute** the migration (follow RESTRUCTURING_PROPOSAL.md)
6. **Test** thoroughly before publishing
7. **Publish** to public repo

---

## Important Notes

- The private repo (this one) will continue to have ALL content
- You develop normally in the private repo
- The public repo is a filtered mirror (read-only, generated)
- Changes to public content happen in private repo, then mirrored
- `_internal/` never appears in public repo (clean history)

---

## Questions?

See the detailed proposal: `RESTRUCTURING_PROPOSAL.md`
See the workflow guide: `private_to_public_clean_mirror_workflow.md`

---

**Status**: Ready for Implementation
**Created**: 2025-11-04
