# Python Project Setup Skill

## Overview

This skill helps you scaffold new Python projects following company standards with proper internal/public content separation. It ensures AI agents understand the difference between internal project management content and public-facing code.

**Version**: 2.0.0 (Reference-Based)
**Last Updated**: 2025-11-05

---

## 📚 Complete Documentation Suite

This skill is now **reference-based** - all detailed documentation lives in separate, maintainable files:

| Document | Purpose | Audience | Size |
|----------|---------|----------|------|
| **This file (skill.md)** | Quick start, company policy, workflows | Everyone | ~10KB |
| [GUIDELINES.md](GUIDELINES.md) | Company standards (Poetry, Pydantic v2, etc.) | Everyone | ~30KB |
| [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md) | Every directory documented | Developers, AI agents | ~45KB |
| [FILE_GUIDE.md](FILE_GUIDE.md) | Every file documented | Developers, AI agents | ~35KB |
| [template/](template/) | Complete project template | Copy for new projects | 40 files |
| [scripts/](scripts/) | Automation scripts | Developers | 3 scripts |

**For detailed information on structure, files, or guidelines, see the documents above.**

---

## 🚀 Quick Start (3 Ways)

### 1. Interactive Setup (Recommended)

Use the automated setup script for guided project creation:

```bash
# Run interactive setup
python .claude/skills/python-project-setup/scripts/setup_project.py
```

Features:
- Interactive prompts with validation
- Automatic placeholder replacement
- Optional Git init
- Optional venv/Poetry setup
- Optional initial test run
- See [scripts/README.md](scripts/README.md) for details

### 2. Manual Copy

```bash
# Copy template
cp -r .claude/skills/python-project-setup/template /path/to/new-project
cd /path/to/new-project

# Customize (replace PROJECT_NAME with your package name)
PROJECT_NAME="your_package"
mv src/PROJECT_NAME "src/${PROJECT_NAME}"
find . -type f \( -name "*.md" -o -name "*.toml" -o -name "*.py" \) \
  -exec sed -i "s/PROJECT_NAME/${PROJECT_NAME}/g" {} +

# Initialize
git init
poetry install  # or: python -m venv .venv && pip install -e ".[dev]"

# Verify
pytest -v
ruff check src/
mypy src/
```

### 3. Reference Only

Use this skill as a reference without copying:
- Browse [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md) for directory purposes
- Browse [FILE_GUIDE.md](FILE_GUIDE.md) for file details
- Browse [GUIDELINES.md](GUIDELINES.md) for company standards

---

## 🏢 Company Policy (CRITICAL)

**These policies are MANDATORY and apply to all Python projects.**

### AI Artifacts Policy

⚠️ **AI files are INTERNAL ONLY:**

| File | Location | Purpose | Public Repo |
|------|----------|---------|-------------|
| `AGENTS.md` | Root | Quick agent reference (<5KB) | ❌ EXCLUDED |
| `.github/copilot-instructions.md` | `.github/` | Comprehensive agent instructions | ❌ EXCLUDED |
| `_internal/project/AGENT_START_HERE.md` | `_internal/project/` | Project-specific agent entry | ❌ EXCLUDED |
| `_internal/CONSTITUTION.md` | `_internal/` | Project governance | ❌ EXCLUDED |

**Rationale**: Company policy prohibits exposing AI tool configurations in public repositories.

**Implementation**: These files exist at root/.github for AI agent discovery but are excluded via `allowlist.txt`.

### Dotfiles Policy

⚠️ **Only specific dotfiles in public repo:**

| File/Folder | Public Repo | Reason |
|-------------|-------------|--------|
| `.github/workflows/` | ✅ INCLUDED | CI/CD workflows |
| `.gitignore` | ✅ INCLUDED | Standard practice |
| `.python-version` | ✅ INCLUDED | Version specification |
| **All other dotfiles** | ❌ EXCLUDED | Company policy |

### Technology Standards

**Required** (See [GUIDELINES.md](GUIDELINES.md) for details):
- **Python**: 3.9+ (3.11+ recommended)
- **Environment Manager**: Poetry (preferred)
- **Virtual Environment**: Local `.venv` in project root
- **Validation**: Pydantic v2 (not v1)
- **Linting**: Ruff (replaces black, isort, flake8)
- **Type Checking**: Mypy (strict mode)
- **Testing**: Pytest with coverage (80%+ required)

---

## 📋 Key Files to Understand

**Before starting, familiarize yourself with:**

1. **[GUIDELINES.md](GUIDELINES.md)** - Company standards
   - Poetry setup
   - Pydantic v2 usage
   - Tool configuration (Ruff, Mypy, Pytest)
   - CI/CD requirements

2. **[template/_internal/CONSTITUTION.md](template/_internal/CONSTITUTION.md)** - Project governance
   - Core principles
   - Immutable rules
   - Architectural decisions
   - AI agent constraints

3. **[STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md)** - Directory purposes
   - What each folder is for
   - Content guidelines
   - When to use each directory

4. **[FILE_GUIDE.md](FILE_GUIDE.md)** - File-by-file reference
   - What each file does
   - Customization requirements
   - Must-edit vs optional

---

## 🛠️ Automation Scripts

**All scripts are documented in [scripts/README.md](scripts/README.md)**

### `setup_project.py`
Interactive project scaffolding with guided prompts.
```bash
python scripts/setup_project.py
```

### `show_structure.py`
Display information about files and directories.
```bash
# Quick reference
python scripts/show_structure.py

# Specific item
python scripts/show_structure.py _internal/project/

# List all
python scripts/show_structure.py --list-dirs
```

### `validate_structure.py`
Validate project against company standards.
```bash
# Validate current project
python scripts/validate_structure.py

# Strict mode (for CI)
python scripts/validate_structure.py --strict
```

---

## 🎯 Common Use Cases

### Use Case 1: New Project Setup

```bash
# Option A: Interactive (easiest)
python .claude/skills/python-project-setup/scripts/setup_project.py

# Option B: Manual
cp -r .claude/skills/python-project-setup/template my-project
cd my-project
# ... customize ...
```

**Then**:
1. Review [FILE_GUIDE.md](FILE_GUIDE.md) - customize required files
2. Update `AGENTS.md` with project-specific info
3. Update `.github/copilot-instructions.md` with comprehensive context
4. Update `_internal/CONSTITUTION.md` with project rules
5. Update `_internal/project/AGENT_START_HERE.md` with current status

### Use Case 2: Understanding Structure

```bash
# What does this directory do?
python scripts/show_structure.py _internal/project/context/essential/

# What should I put in this file?
python scripts/show_structure.py pyproject.toml

# Show me all files
python scripts/show_structure.py --list-files
```

**Or** browse:
- [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md) - Directories
- [FILE_GUIDE.md](FILE_GUIDE.md) - Files

### Use Case 3: Validating Compliance

```bash
# Check if project follows standards
python scripts/validate_structure.py /path/to/project

# For CI/CD
python scripts/validate_structure.py --strict
```

### Use Case 4: Learning Company Guidelines

Read [GUIDELINES.md](GUIDELINES.md) for:
- Poetry setup and usage
- Pydantic v2 patterns
- Testing standards
- CI/CD configuration
- Security practices
- Documentation requirements

---

## 🤖 AI Agent Workflow

### Agent Reading Order

1. **`AGENTS.md`** (root) - Quick 30-second orientation
2. **`.github/copilot-instructions.md`** - Comprehensive project context
3. **`_internal/CONSTITUTION.md`** - Project rules and governance
4. **`_internal/project/AGENT_START_HERE.md`** - Current status and priorities
5. **Tier 0 context** (`_internal/project/context/essential/`) - Always load
6. **Tier 1 context** (`_internal/project/context/situational/`) - Load as needed

**See [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md#tiered-context-system-for-ai-agents) for complete details.**

### Agent Responsibilities

**Must follow**:
1. Company policy (this document)
2. Project constitution (`_internal/CONSTITUTION.md`)
3. Guidelines ([GUIDELINES.md](GUIDELINES.md))
4. Tiered context system
5. Session logging requirements

**Cannot**:
- Violate immutable rules in CONSTITUTION.md
- Commit secrets
- Skip tests
- Ignore type checking
- Change architecture without human approval

---

## 📊 Project Structure Overview

**For complete details, see [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md)**

### High-Level Organization

```
project-name/
├── _internal/          # ⚠️  Internal only (PM, context, reports)
├── .github/            # CI/CD + agent instructions
├── docs/               # ✅ Public documentation
├── scripts/            # ✅ Public utilities
├── src/                # ✅ Public source code
├── tests/              # ✅ Public test suite
└── [config files]      # ✅ Public configs
```

### Key Principles

1. **Separation**: Internal (`_internal/`) vs public (everything else)
2. **src/ Layout**: Never put source code at root
3. **Tiered Context**: Tier 0 (<5KB) → Tier 1 (5-20KB) → Tier 2 (20KB+) → Tier 3 (archive)
4. **Documentation Hierarchy**: docs/ (stable) vs reports/ (transient) vs _internal/
5. **Agent Discovery**: AGENTS.md and copilot-instructions.md at root for discovery

---

## ✅ Customization Checklist

**After copying template, customize these (see [FILE_GUIDE.md](FILE_GUIDE.md) for details):**

### Must Customize (Required)
- [ ] Rename `src/PROJECT_NAME/` to your package name
- [ ] Update `pyproject.toml` (name, authors, description, dependencies)
- [ ] Update `README.md` (description, features, usage)
- [ ] Update `LICENSE` (copyright holder and year)
- [ ] Update `AGENTS.md` (project-specific info)
- [ ] Update `.github/copilot-instructions.md` (comprehensive context)
- [ ] Update `_internal/CONSTITUTION.md` (project rules)
- [ ] Update `_internal/project/AGENT_START_HERE.md` (entry point)

### Should Customize (Recommended)
- [ ] Update `_internal/project/context/essential/checklists.md`
- [ ] Update `_internal/project/context/essential/warnings.md`
- [ ] Replace `tests/unit/test_example.py` with real tests
- [ ] Implement `src/your_package/__main__.py` (CLI)
- [ ] Update `docs/README.md` (documentation index)

### Optional Customization
- [ ] Adjust `.github/workflows/ci.yml` (Python versions, deployment)
- [ ] Adjust `.python-version` (if targeting different version)
- [ ] Add project-specific scripts to `scripts/`

**Validation**:
```bash
# Check for unreplaced placeholders and missing files
python scripts/validate_structure.py
```

---

## 🔍 Finding Information

### "I need to know..."

| What You Need | Where to Look |
|---------------|---------------|
| **How to set up Poetry** | [GUIDELINES.md](GUIDELINES.md#python-environment-management) |
| **How to use Pydantic v2** | [GUIDELINES.md](GUIDELINES.md#use-pydantic-v2-required) |
| **What goes in _internal/project/** | [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md##_internalproject---project-management--agent-context) |
| **What is AGENTS.md for** | [FILE_GUIDE.md](FILE_GUIDE.md#agentsmd--internal) |
| **Testing standards** | [GUIDELINES.md](GUIDELINES.md#testing-standards) |
| **CI/CD requirements** | [GUIDELINES.md](GUIDELINES.md#cicd-standards) |
| **All available scripts** | [scripts/README.md](scripts/README.md) |
| **Quick file reference** | [FILE_GUIDE.md](FILE_GUIDE.md#quick-file-finder) |
| **Tier 0/1/2 context** | [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md#tiered-context-system-for-ai-agents) |

---

## 📚 Complete Documentation Index

### Core Skill Files
1. **skill.md** (this file) - Quick start, policy, workflows
2. **[GUIDELINES.md](GUIDELINES.md)** - Company standards and practices
3. **[STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md)** - Complete directory guide
4. **[FILE_GUIDE.md](FILE_GUIDE.md)** - Complete file guide
5. **[scripts/README.md](scripts/README.md)** - Automation scripts documentation

### Template Files
6. **[template/](template/)** - Complete project template
7. **[template/_internal/CONSTITUTION.md](template/_internal/CONSTITUTION.md)** - Project governance template
8. **[template/AGENTS.md](template/AGENTS.md)** - Agent quick reference template
9. **[template/.github/copilot-instructions.md](template/.github/copilot-instructions.md)** - Comprehensive agent instructions template
10. **[template/_internal/project/AGENT_START_HERE.md](template/_internal/project/AGENT_START_HERE.md)** - Agent entry point template

### Repository Documentation
11. **Python Project Structure/PYTHON_PROJECT_STRUCTURE_SST.md** - Full SST document
12. **Python Project Structure/PYTHON_PROJECT_SETUP_CHECKLIST.md** - Setup checklist
13. **private_to_public_clean_mirror_workflow.md** - Public repo mirroring workflow

---

## 🔄 Maintenance

### Updating the Skill

**To modify structure or standards**:
1. Update relevant reference document:
   - Company standards → [GUIDELINES.md](GUIDELINES.md)
   - Directory purposes → [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md)
   - File details → [FILE_GUIDE.md](FILE_GUIDE.md)
2. Update [template/](template/) if needed
3. Update this file (skill.md) only for policy or workflow changes
4. Test with `scripts/validate_structure.py`
5. Commit changes

**Why reference-based?**
- Single source of truth for each concept
- Easier to maintain (update once)
- No duplication/drift
- Comprehensive without bloat

---

## ❓ FAQ

**Q: Where do I start?**
A: Run `python scripts/setup_project.py` for interactive setup, or read [GUIDELINES.md](GUIDELINES.md) first.

**Q: What's the difference between all these docs?**
A:
- **skill.md** (this): Quick start, policy, workflows
- **GUIDELINES.md**: Company standards (Poetry, Pydantic, etc.)
- **STRUCTURE_REFERENCE.md**: What each directory is for
- **FILE_GUIDE.md**: What each file is for

**Q: Do I have to use Poetry?**
A: Preferred but not required. See [GUIDELINES.md](GUIDELINES.md#virtual-environment-management) for alternatives.

**Q: What's the tiered context system?**
A: See [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md#tiered-context-system-for-ai-agents) - it's how we organize AI agent context by size/frequency.

**Q: How do I validate my project?**
A: Run `python scripts/validate_structure.py`

**Q: Where do internal docs go?**
A: Everything internal goes in `_internal/`. See [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md#_internal---internal-project-management).

---

## 📞 Support

- **Questions about structure**: See [STRUCTURE_REFERENCE.md](STRUCTURE_REFERENCE.md)
- **Questions about files**: See [FILE_GUIDE.md](FILE_GUIDE.md)
- **Questions about standards**: See [GUIDELINES.md](GUIDELINES.md)
- **Questions about scripts**: See [scripts/README.md](scripts/README.md)
- **Issues or improvements**: Create an issue in the template repository

---

**Version**: 2.0.0 (Reference-Based)
**Last Updated**: 2025-11-05
**Maintained By**: Company Engineering Team

