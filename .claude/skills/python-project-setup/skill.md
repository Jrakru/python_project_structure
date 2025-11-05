# Python Project Setup Skill

## Overview

This skill helps you scaffold new Python projects following company standards with proper internal/public content separation. It ensures AI agents understand the difference between internal project management content and public-facing code.

## When to Use This Skill

- Setting up a new Python project from scratch
- Converting an existing Python project to use internal/public separation
- Ensuring proper structure for dual-repository workflow (private internal + public mirror)

## 📚 Comprehensive Documentation Available

This skill includes complete reference materials for both new users and AI agents:

### For Quick Setup
- **`template/`** - Complete, ready-to-copy project template with all files
- **This file (skill.md)** - Quick start guide and workflows

### For Understanding Structure
- **`STRUCTURE_REFERENCE.md`** - Comprehensive guide to every directory
  - Purpose of each folder
  - Content guidelines
  - Usage patterns
  - Size limits for AI context
  - Customization instructions

### For Understanding Files
- **`FILE_GUIDE.md`** - Complete guide to every template file
  - Purpose of each file
  - Customization requirements
  - Template variables
  - Must-edit vs optional
  - Quick file finder reference

### Recommended Reading Order

**For New Users:**
1. Read this file (skill.md) for overview and quick start
2. Copy `template/` to your project location
3. Reference `FILE_GUIDE.md` while customizing files
4. Reference `STRUCTURE_REFERENCE.md` when adding new directories

**For AI Agents:**
1. Read this file (skill.md) for company policy and philosophy
2. Reference `STRUCTURE_REFERENCE.md` for detailed directory purposes
3. Reference `FILE_GUIDE.md` for file-specific customization
4. Use `template/` as source for copying files

## Project Structure Philosophy

### Internal vs Public Separation

**Internal Content** (`_internal/`):
- Project management (planning, metrics, backlog)
- AI agent context (tiered context system)
- Session learnings and distillations
- Architecture Decision Records (ADRs)
- Internal investigations and research
- Status reports
- Internal automation scripts
- **AI agent instructions** (AGENTS.md, copilot-instructions.md at root for discovery)

**Public Content** (root level):
- Source code (`src/`)
- Tests (`tests/`)
- Public documentation (`docs/`)
- Public utility scripts (`scripts/`)
- CI/CD configuration (`.github/workflows/`)
- Standard config files (README.md, LICENSE, pyproject.toml, etc.)

### Company Policy (CRITICAL)

⚠️ **AI Artifacts Policy:**
- `AGENTS.md` is kept at **root** for AI agent discovery (internal use only)
- `.github/copilot-instructions.md` is kept at **root/.github/** for AI agent discovery (internal use only)
- **BOTH are EXCLUDED from public repository** per company policy
- All other AI tool configurations go in `_internal/` or are excluded

⚠️ **Dotfiles Policy:**
- **Only** `.github/` (CI/CD workflows), `.gitignore`, and `.python-version` are included in public repo
- All other dotfiles/dotfolders are excluded from public repo

## Directory Structure

```
project-name/
├── _internal/                        # ⚠️  INTERNAL ONLY - Never in public repo
│   ├── docs/
│   │   ├── decisions/               # ADRs
│   │   ├── investigations/          # Research & spikes
│   │   ├── setup/                   # Internal setup guides
│   │   └── starter-pack/            # Template documentation
│   ├── project/
│   │   ├── context/
│   │   │   ├── essential/           # Tier 0: <5KB (checklists, warnings)
│   │   │   ├── situational/         # Tier 1: 5-20KB (patterns, solutions)
│   │   │   ├── reference/           # Tier 2: 20KB+ (full specs)
│   │   │   └── archive/             # Tier 3: Historical
│   │   ├── learnings/
│   │   │   ├── raw/sessions/        # Individual session logs
│   │   │   └── distilled/           # Summaries & patterns
│   │   ├── planning/                # Roadmap, milestones
│   │   ├── backlog/                 # Work items
│   │   ├── metrics/                 # Project metrics
│   │   ├── AGENT_START_HERE.md      # <5KB agent entry point
│   │   └── README.md
│   ├── reports/                     # Status reports
│   │   ├── archive/
│   │   └── README.md
│   └── scripts/                     # Internal automation
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml                   # ✅ Public CI/CD
│   └── copilot-instructions.md      # ⚠️  Internal only (excluded from public)
│
├── docs/                            # ✅ Public documentation
│   ├── guides/
│   ├── reference/
│   └── README.md
│
├── scripts/                         # ✅ Public utility scripts
│   ├── setup.py
│   ├── lint.py
│   └── test.py
│
├── src/                             # ✅ Public source code
│   └── PROJECT_NAME/
│       ├── core/
│       ├── models/
│       ├── utils/
│       ├── __init__.py
│       └── __main__.py
│
├── tests/                           # ✅ Public tests
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── conftest.py
│
├── .gitignore                       # ✅ Public
├── .python-version                  # ✅ Public
├── AGENTS.md                        # ⚠️  Root for discovery, EXCLUDED from public
├── CHANGELOG.md                     # ✅ Public
├── LICENSE                          # ✅ Public
├── allowlist.txt                    # Controls public repo mirroring
├── public.gitignore                 # Template .gitignore for public repo
├── pyproject.toml                   # ✅ Public
└── README.md                        # ✅ Public
```

## Usage

### Quick Start - Copy Template

```bash
# Copy template from this skill
cp -r .claude/skills/python-project-setup/template /path/to/new-project
cd /path/to/new-project

# Alternative: Copy from repository source
# cp -r "Python Project Structure/starter_pack" /path/to/new-project

# Customize project name
PROJECT_NAME="your_package_name"
mv src/PROJECT_NAME "src/${PROJECT_NAME}"
find . -type f \( -name "*.md" -o -name "*.toml" -o -name "*.py" \) \
  -exec sed -i "s/PROJECT_NAME/${PROJECT_NAME}/g" {} +

# Initialize
git init
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"

# Verify
pytest -v
ruff check src/
mypy src/
```

### Manual Setup Steps

If you prefer manual setup or need to understand each component:

1. **Create directory structure** (use `template/` directory or copy from repository)
2. **Review** `STRUCTURE_REFERENCE.md` for directory purposes
3. **Review** `FILE_GUIDE.md` for file-by-file customization guide
4. **Set up pyproject.toml** with:
   - Ruff for linting/formatting
   - Mypy for type checking
   - Pytest for testing
   - Coverage for code coverage
3. **Create AGENTS.md at root** with project-specific instructions
4. **Create .github/copilot-instructions.md** with comprehensive agent context
5. **Set up _internal/project/AGENT_START_HERE.md** (<5KB quick reference)
6. **Configure allowlist.txt** per company policy
7. **Create public.gitignore** for public repo

## Key Files to Customize

### Must Customize (5 items)
1. `PROJECT_NAME` → your_package_name (in src/ and all files)
2. `PROJECT_DISPLAY_NAME` → Your Project Name (in docs)
3. `USERNAME` → your-github-username (in pyproject.toml)
4. Author name and email (in pyproject.toml)
5. Copyright holder (in LICENSE)

### Should Customize (8 items)
1. Project description (README.md, pyproject.toml)
2. Features list (README.md)
3. Dependencies (pyproject.toml)
4. Python version (.python-version, pyproject.toml)
5. Keywords and classifiers (pyproject.toml)
6. Repository URLs (pyproject.toml)
7. License type (if not MIT)
8. Project-specific gotchas (AGENTS.md)

## Tiered Context System for AI Agents

**Tier 0 - Essential** (<5KB each):
- `_internal/project/AGENT_START_HERE.md` - Always load first
- `_internal/project/context/essential/checklists.md`
- `_internal/project/context/essential/warnings.md`

**Tier 1 - Situational** (5-20KB):
- Load as needed based on task
- Patterns, antipatterns, common solutions

**Tier 2 - Reference** (20KB+):
- Lookup only when Tier 0/1 insufficient
- Full specifications, detailed patterns

**Tier 3 - Archive**:
- Historical context, rarely needed

## Public Repository Mirroring

### Testing Locally

```bash
# Install git-filter-repo
pip install git-filter-repo

# Test mirror in temporary directory
cd /tmp
git clone /path/to/private-repo test-public-mirror
cd test-public-mirror

# Filter to allowlisted content only
git filter-repo --force \
  --paths-from-file allowlist.txt \
  --path-rename public.gitignore:.gitignore

# Verify no internal content leaked
ls -la  # Should not see _internal/, AGENTS.md, copilot-instructions.md
git log --all --full-history -- _internal/  # Should be empty
git log --all --full-history -- AGENTS.md  # Should be empty

# Clean up
cd /tmp && rm -rf test-public-mirror
```

### Company Policy Compliance

✅ **Verify before publishing:**
- [ ] No `_internal/` directory in public repo
- [ ] No `AGENTS.md` in public repo
- [ ] No `.github/copilot-instructions.md` in public repo
- [ ] Only `.github/workflows/ci.yml` in `.github/`
- [ ] No other AI tool configurations exposed
- [ ] Only approved dotfiles present (.gitignore, .python-version)
- [ ] All internal documentation removed
- [ ] All session logs and learnings removed
- [ ] All ADRs and investigations removed

## AI Agent Workflow

When working on a project with this structure:

1. **Start**: Read `AGENTS.md` (root) for quick project overview
2. **Deep dive**: Read `.github/copilot-instructions.md` for comprehensive context
3. **Task-specific**: Load relevant files from `_internal/project/context/`
4. **Learning**: Log sessions in `_internal/project/learnings/raw/sessions/`
5. **Distillation**: Periodically summarize learnings into `distilled/` directories

## Common Tasks

### Adding a New Feature

1. Check `_internal/project/context/essential/checklists.md`
2. Review relevant patterns in `_internal/project/context/situational/`
3. Implement in `src/PROJECT_NAME/`
4. Add tests in `tests/`
5. Update public docs in `docs/`
6. Log session in `_internal/project/learnings/raw/sessions/YYYY-MM-DD-feature-name.md`

### Making Architectural Decisions

1. Create ADR in `_internal/docs/decisions/NNNN-decision-title.md`
2. Update `_internal/project/context/` if patterns emerge
3. Update `.github/copilot-instructions.md` if affects agent workflow

### Publishing to Public Repository

1. Review `allowlist.txt` for correctness
2. Test locally (see above)
3. Verify company policy compliance
4. Run manual mirror or use automated GitHub Action
5. Verify public repo has no internal artifacts

## Tool Configuration

### Ruff (Linting & Formatting)
- Line length: 88
- Target: Python 3.9+
- Rules: E, W, F, I, B, C4, UP

### Mypy (Type Checking)
- Strict mode enabled
- Tests excluded

### Pytest (Testing)
- Coverage threshold: 80%
- Markers: slow, integration

### CI/CD
- GitHub Actions for Python 3.9-3.12
- Automated linting, type checking, testing
- Coverage upload to Codecov

## Best Practices

1. **Keep AGENTS.md current** - Update as project evolves
2. **Use tiered context** - Don't overload agents with unnecessary context
3. **Log learnings** - Capture insights from every session
4. **Distill regularly** - Weekly/monthly summaries prevent context bloat
5. **Test mirror locally** - Before publishing to public repo
6. **Follow company policy** - No AI artifacts in public repo
7. **Separate concerns** - Internal PM vs. public code

## Troubleshooting

**Q: Agent can't find AGENTS.md?**
A: Ensure it's at project root, not in `_internal/`

**Q: Internal content leaked to public repo?**
A: Review and fix `allowlist.txt`, test locally before pushing

**Q: CI/CD failing?**
A: Check `.github/workflows/ci.yml` is in public repo allowlist

**Q: Type errors with mypy?**
A: Ensure `src/` is in PYTHONPATH (configured in pyproject.toml)

## References

### Within This Skill
- **Template**: `.claude/skills/python-project-setup/template/` - Complete project template
- **Structure Guide**: `.claude/skills/python-project-setup/STRUCTURE_REFERENCE.md` - Every directory documented
- **File Guide**: `.claude/skills/python-project-setup/FILE_GUIDE.md` - Every file documented
- **This File**: `.claude/skills/python-project-setup/skill.md` - Quick start and workflows

### In Repository
- Starter Pack Source: `Python Project Structure/starter_pack/`
- Full SST Doc: `Python Project Structure/PYTHON_PROJECT_STRUCTURE_SST.md`
- Setup Checklist: `Python Project Structure/PYTHON_PROJECT_SETUP_CHECKLIST.md`
- Mirroring Workflow: `private_to_public_clean_mirror_workflow.md`
- Restructuring Proposal: `RESTRUCTURING_PROPOSAL.md`

## Version

- **Version**: 1.0.0
- **Last Updated**: 2025-11-05
- **Maintained By**: Company Engineering Team
