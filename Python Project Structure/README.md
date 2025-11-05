# Python Project Structure - SST (Single Source of Truth)

**Status**: ✅ Canonical Reference  
**Version**: 1.0.0  
**Last Updated**: 2025-10-21  
**Authority**: This is the authoritative source for Python project structure patterns

---

## 🎯 Purpose

This folder contains the **Single Source of Truth (SST)** for Python project structure, incorporating proven patterns from the 1C4D5 project and optimized for both human developers and AI agents.

**Use this as the canonical reference** when setting up new Python projects or reorganizing existing ones.

---

## 📚 Documents in This Folder

### 1. Primary SST Document

**`PYTHON_PROJECT_STRUCTURE_SST.md`**
- **Size**: ~923 lines, comprehensive reference
- **Purpose**: Complete specification of Python project structure
- **Use For**: 
  - Deep understanding of structure rationale
  - Reference for all directory purposes
  - Tool configuration examples
  - Best practices and anti-patterns
  - Agent collaboration patterns

**Contents**:
- Canonical directory structure (50+ directories)
- Purpose and guidelines for each directory
- Tool configuration (pyproject.toml, ruff, mypy, pytest)
- Context tier system (Tier 0-3) for AI agents
- Agent workflows (6 complete workflows)
- Quality gates and automation
- 15+ production-ready templates
- Maintenance schedules
- 20+ FAQ answers

### 2. Quick Start Checklist

**`PYTHON_PROJECT_SETUP_CHECKLIST.md`**
- **Size**: ~555 lines, actionable steps
- **Purpose**: Step-by-step setup guide
- **Use For**:
  - Setting up new project in ~5 minutes
  - Quick reference during setup
  - Validation checklist
  - Template copying

**Contents**:
- 4 setup phases (initialization, structure, files, configuration)
- Copy-paste ready commands
- File templates for all essentials
- Testing setup examples
- AI agent collaboration setup
- Scripts setup patterns
- CI/CD configuration
- Final validation checklist

---

## 🚀 Quick Start

### For New Projects (5 minutes)
1. Open `PYTHON_PROJECT_SETUP_CHECKLIST.md`
2. Follow Phase 1-4 step-by-step
3. Customize templates with your project info
4. Run validation steps
5. You're done!

### For Understanding/Reference
1. Open `PYTHON_PROJECT_STRUCTURE_SST.md`
2. Use table of contents to navigate
3. Review rationale and examples
4. Apply patterns to your project

---

## 🔗 SST Relationship

### Authority Hierarchy

```
Second-Brain (THIS LOCATION) = SST (Authoritative Source)
  ↓
  Synced to implementation repositories
  ↓
  1C4D5/docs/reference/ (Reference Implementation)
```

### Golden Rule

> **When conflicts arise, this second-brain version takes precedence.**

### Sync Protocol

- **This folder** is the authoritative source
- **Implementation repos** sync FROM here
- **Updates** should be made here first, then synced to implementations
- **Conflicts** are resolved in favor of second-brain version

---

## 📦 What's Covered

### Directory Structure
- `.github/` - GitHub configuration, AI agent instructions
- `docs/` - Stable documentation (framework, guides, reference, decisions, investigations)
- `reports/` - Transient reports with archival policy
- `project/` - AI agent collaboration system (tiered context, learnings, process)
- `scripts/` - Utility automation
- `specs/` - Formal specifications
- `src/` - Source code organization
- `tests/` - Test suite structure

### Key Patterns
- **Three-tier documentation**: docs/reports/archive separation by lifespan
- **Tiered context system**: Tier 0-3 for optimized AI agent token usage
- **Session logging + distillation**: Continuous learning loop
- **Navigate, don't duplicate**: Link to SST rather than duplicating
- **Automation-first scripts**: Consistent conventions for all utilities
- **Quality gates**: Pre-commit, CI/CD, coverage thresholds

### Tool Stack
- **Ruff**: Fast linting + formatting (replaces black, isort, flake8)
- **Mypy**: Static type checking
- **Pytest**: Testing framework
- **Coverage.py**: Code coverage
- **pyproject.toml**: Centralized tool configuration

---

## 🎯 Use Cases

### ✅ Use This SST When:
- Setting up a new Python project from scratch
- Reorganizing an existing Python project
- Adding AI agent collaboration capabilities
- Standardizing project structure across a team
- Need reference for Python tooling configuration
- Setting up documentation hierarchy
- Implementing session logging and distillation

### ❌ Don't Use When:
- Working on non-Python projects (need different SST)
- Project has strict corporate/framework structure requirements
- Quick prototypes or throwaway code (overkill)
- Single-file scripts (doesn't need full structure)

---

## 📊 Key Innovations

1. **Tiered Context System** - Optimize agent token usage (0: <5KB, 1: 5-20KB, 2: 20KB+, 3: archive)
2. **Session Logging + Distillation** - Continuous learning loop with automation
3. **Three-Tier Documentation** - Explicit separation by lifespan (docs/reports/archive)
4. **Navigate, Don't Duplicate** - Link to SST, prevent content drift
5. **Automation-First Scripts** - Consistent conventions, self-documenting

---

## 🔄 Maintenance

### This SST
- **Review**: Quarterly or when major patterns emerge
- **Update**: Make changes here first, then sync to implementations
- **Version**: Increment version on significant updates

### Implementation Syncs
- **1C4D5 repo**: Syncs from this SST as reference implementation
- **Other projects**: Should reference this SST or sync patterns

---

## 💡 Related Resources

### In Second-Brain
- This is the primary Python project structure resource
- Link to other methodology docs as needed

### In Implementation Repos
- **1C4D5**: `/docs/reference/PYTHON_PROJECT_STRUCTURE_SST.md` (synced copy)
- **1C4D5**: `/docs/reference/PYTHON_PROJECT_SETUP_CHECKLIST.md` (synced copy)

---

## ❓ Questions?

**Q: Why is this in second-brain?**  
A: Second-brain is the SST repository. All canonical knowledge lives here and syncs to implementation repos.

**Q: Can I modify the 1C4D5 copy?**  
A: Yes, but changes should ideally be made here first, then synced. If modified in 1C4D5, sync back here.

**Q: What if patterns evolve?**  
A: Update here first, increment version, then sync to implementation repos.

**Q: How do I use this for my project?**  
A: Read the checklist for quick setup, or the full SST for deep understanding. Copy patterns as needed.

---

**Version**: 1.0.0  
**Status**: ✅ Canonical SST  
**Maintained By**: Project maintainers  
**Last Updated**: 2025-10-21

---

## 📦 Starter Pack (NEW!)

**Location**: `starter_pack/`

### What is it?

A **ready-to-copy template** with all files and directory structure pre-created. Just copy, customize project name, and start coding!

**Contents**:
- Complete directory structure (50+ folders)
- All template files ready to customize
- Working tests and CI/CD configuration
- Scripts for automation
- Agent collaboration files

### Quick Start (2 Minutes)

```bash
# Copy starter pack to your new project
cp -r "/path/to/second-brain/3. Resource/Python Project Structure/starter_pack" /path/to/my-new-project

cd /path/to/my-new-project

# Customize project name
PROJECT_NAME="my_project"
mv src/PROJECT_NAME "src/${PROJECT_NAME}"
find . -type f \( -name "*.md" -o -name "*.toml" -o -name "*.py" \) -exec sed -i "s/PROJECT_NAME/${PROJECT_NAME}/g" {} +

# Initialize and verify
git init
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

### See Also
- **How to Use**: `starter_pack/_internal/docs/starter-pack/HOW_TO_USE.md` - Complete setup guide
- **Manifest**: `starter_pack/_internal/docs/starter-pack/MANIFEST.txt` - List of all included files
- **Contents**: `starter_pack/_internal/docs/starter-pack/STARTER_PACK_CONTENTS.md` - Complete file listing

---

## 🎯 Which One Should I Use?

| If You Want... | Use This | Time |
|----------------|----------|------|
| **Quick project setup** | `starter_pack/` | 2 minutes |
| **Step-by-step guide** | `PYTHON_PROJECT_SETUP_CHECKLIST.md` | 5 minutes |
| **Deep understanding** | `PYTHON_PROJECT_STRUCTURE_SST.md` | 30+ minutes |
| **All of the above** | Use all three! | - |

**Recommended Approach**:
1. **Copy** `starter_pack/` for instant structure
2. **Follow** checklist for verification
3. **Read** SST for understanding rationale

---

## 📈 Version History

- **1.0.0** (2025-10-21)
  - Initial SST document
  - Setup checklist
  - Starter pack with 29 template files
  - Complete directory structure
  - CI/CD configuration
  - Agent collaboration system

