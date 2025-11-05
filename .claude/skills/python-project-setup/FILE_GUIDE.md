# Python Project Template - File Guide

Complete reference for every file in the project template. Use this guide to understand what each file does and how to customize it.

---

## 📋 File Inventory

**Total Files**: 29+ template files
**Total Directories**: 50+ directories

---

## 🔐 Root Level Files

### Configuration & Documentation

#### `README.md` ✅ PUBLIC
**Location**: `/`
**Purpose**: Project overview and getting started guide
**Customize**:
- Replace `PROJECT_NAME` with your package name
- Replace `PROJECT_DISPLAY_NAME` with human-readable name
- Update description and features list
- Update installation instructions
- Add your specific usage examples
**Size**: ~500-2000 lines typical
**Format**: Markdown
**Must Edit**: Yes

---

#### `pyproject.toml` ✅ PUBLIC
**Location**: `/`
**Purpose**: Python project configuration (PEP 518/621 standard)
**Customize**:
- `[project]` section: name, version, description, authors
- `authors`: Update name and email
- `dependencies`: Add your runtime dependencies
- `[project.optional-dependencies]` dev: Add your dev tools
- `[project.urls]`: Update repository and homepage URLs
- `[tool.ruff]` target-version: Adjust Python version if needed
**Contains**:
- Project metadata
- Dependencies (runtime + dev)
- Ruff configuration (linting + formatting)
- Mypy configuration (type checking)
- Pytest configuration
- Coverage settings
**Size**: ~100-200 lines
**Format**: TOML
**Must Edit**: Yes

**Key Sections to Review**:
```toml
[project]
name = "PROJECT_NAME"              # ← Change this
version = "0.1.0"                  # ← Version your project
description = "..."                 # ← Your description
authors = [{name = "...", email = "..."}]  # ← Your info

dependencies = []                   # ← Add runtime deps

[project.optional-dependencies]
dev = [                            # ← Add dev tools
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    # ... more
]

[project.urls]
Homepage = "..."                    # ← Your URLs
Repository = "..."
```

---

#### `CHANGELOG.md` ✅ PUBLIC
**Location**: `/`
**Purpose**: Version history and release notes
**Customize**:
- Update Unreleased section as you develop
- Add released versions with dates
- Follow Keep a Changelog format
**Format**: Markdown (Keep a Changelog standard)
**Must Edit**: No (but maintain as you release)

**Categories**:
- Added - New features
- Changed - Changes in existing functionality
- Deprecated - Soon-to-be removed features
- Removed - Removed features
- Fixed - Bug fixes
- Security - Security improvements

---

#### `LICENSE` ✅ PUBLIC
**Location**: `/`
**Purpose**: Software license
**Default**: MIT License
**Customize**:
- Update `[year]` to current year
- Update `[fullname]` to copyright holder
- Change license type if needed (consult legal team)
**Size**: 1 page
**Must Edit**: Yes (copyright info)

---

#### `.gitignore` ✅ PUBLIC
**Location**: `/`
**Purpose**: Tell git which files to ignore
**Source**: Created from `public.gitignore` during public repo export
**Content**:
- Python artifacts (__pycache__, *.pyc, *.pyo, *.pyd)
- Virtual environments (.venv/, venv/, ENV/)
- IDE files (.vscode/, .idea/, *.swp)
- Build artifacts (dist/, build/, *.egg-info/)
- Testing (.pytest_cache/, .coverage, htmlcov/)
- Type checking (.mypy_cache/, .pytype/)
- OS files (.DS_Store, Thumbs.db)
**Customize**: Add project-specific ignores if needed
**Must Edit**: Rarely

**Note**: In the starter pack, this is the internal .gitignore. The public repo uses `public.gitignore` → `.gitignore`

---

#### `.python-version` ✅ PUBLIC
**Location**: `/`
**Purpose**: Specify Python version for version managers (pyenv, asdf)
**Content**: Single line with Python version
**Default**: `3.9`
**Customize**: Change to your target Python version (3.9, 3.10, 3.11, 3.12)
**Usage**: `pyenv install && pyenv local`
**Must Edit**: Optional (if targeting different Python version)

---

#### `allowlist.txt` 🔧 TEMPLATE
**Location**: `/`
**Purpose**: Define which files go to public repository
**Usage**: Used by git-filter-repo for mirroring
**Format**: One path per line, directories end with `/`
**Company Policy**: Enforces AI artifact and dotfile exclusions
**Customize**: Rarely (add new public directories/files if needed)
**Must Edit**: No (unless adding new public paths)

**Key Rules**:
- Includes: `src/`, `tests/`, `docs/`, `scripts/`, config files
- Excludes: `_internal/`, `AGENTS.md`, `.github/copilot-instructions.md`
- Dotfiles: Only `.github/`, `.gitignore`, `.python-version`

---

#### `public.gitignore` 🔧 TEMPLATE
**Location**: `/`
**Purpose**: Template .gitignore for public repository
**Becomes**: `.gitignore` in public repo (renamed during export)
**Difference from root .gitignore**: No references to internal directories
**Content**: Standard Python .gitignore
**Customize**: Rarely
**Must Edit**: No

**Why Separate?**:
- Root `.gitignore`: Used in private repo, may reference `_internal/`
- `public.gitignore`: Used in public repo, no internal references

---

### AI Agent Files (Internal Use)

#### `AGENTS.md` 🔒 INTERNAL
**Location**: `/` (root for AI agent discovery)
**Purpose**: Quick reference for AI agents (GitHub Copilot, Claude, Cursor)
**Visibility**: ⚠️  INTERNAL ONLY - Excluded from public repo
**Customize**:
- Update project description
- Update tech stack list
- Update directory explanations
- Add project-specific conventions
- Add project-specific gotchas
**Size Limit**: <5KB (keep it quick)
**Format**: Markdown
**Must Edit**: Yes

**Template Structure**:
```markdown
# [Project Name] - AI Agent Quick Reference

## What This Project Does
[1-2 sentences]

## Tech Stack
- Python 3.X
- [Framework]
- [Database]
- [Key libraries]

## Directory Guide
[Quick overview]

## Key Conventions
[Project conventions]

## Common Gotchas
[Things to watch out for]

## More Context
See .github/copilot-instructions.md
See _internal/project/AGENT_START_HERE.md
```

---

### Scripts (Utility Automation)

#### `create_templates.sh` 🔧 INTERNAL
**Location**: `/`
**Purpose**: Script to create all directory structure
**Language**: Bash
**Usage**: `./create_templates.sh`
**Customize**: Usually don't need to change
**Must Edit**: No

---

#### `create_src_templates.sh` 🔧 INTERNAL
**Location**: `/`
**Purpose**: Create src/ directory structure
**Language**: Bash
**Usage**: Called by create_templates.sh or standalone
**Must Edit**: No

---

#### `create_test_templates.sh` 🔧 INTERNAL
**Location**: `/`
**Purpose**: Create tests/ directory structure
**Language**: Bash
**Usage**: Called by create_templates.sh or standalone
**Must Edit**: No

---

## 📁 `.github/` - GitHub Configuration

### `.github/workflows/ci.yml` ✅ PUBLIC
**Location**: `.github/workflows/`
**Purpose**: CI/CD pipeline using GitHub Actions
**Runs On**: Push to main/develop, pull requests
**Customize**:
- `python-version` matrix: Adjust versions to test
- Add deployment steps if needed
- Adjust coverage upload if not using Codecov
**Format**: YAML
**Must Edit**: Optional (works out of box)

**Steps**:
1. Checkout code
2. Setup Python (matrix: 3.9, 3.10, 3.11, 3.12)
3. Install dependencies
4. Run ruff (linting + formatting check)
5. Run mypy (type checking)
6. Run pytest (tests + coverage)
7. Upload coverage to Codecov

---

### `.github/copilot-instructions.md` 🔒 INTERNAL
**Location**: `.github/`
**Purpose**: Comprehensive AI agent instructions
**Visibility**: ⚠️  INTERNAL ONLY - Excluded from public repo
**Customize**:
- Update all project-specific information
- Add detailed architecture documentation
- Document all conventions in depth
- Add comprehensive pattern documentation
- Include detailed workflow guidance
**Size**: No limit (can be comprehensive)
**Format**: Markdown
**Must Edit**: Yes

**Contains**:
- Detailed project overview
- Complete architecture documentation
- All coding conventions
- Testing strategies
- Pattern catalog
- Anti-pattern warnings
- Workflow guidance
- Context navigation map

---

## 📂 `_internal/` - Internal Content

### `_internal/README.md` 🔒 INTERNAL
**Location**: `_internal/`
**Purpose**: Explain what _internal/ contains
**Customize**: Update if adding new subdirectories
**Size**: <1 page
**Must Edit**: No

---

### Internal Documentation

#### `_internal/docs/starter-pack/HOW_TO_USE.md` 🔧 TEMPLATE
**Location**: `_internal/docs/starter-pack/`
**Purpose**: How to use the starter pack
**Audience**: Developers using this template
**Customize**: Update if template changes
**Must Edit**: No

---

#### `_internal/docs/starter-pack/MANIFEST.txt` 🔧 TEMPLATE
**Location**: `_internal/docs/starter-pack/`
**Purpose**: Complete file listing
**Format**: Plain text, file list
**Customize**: Auto-generated, rarely edit manually
**Must Edit**: No

---

#### `_internal/docs/starter-pack/STARTER_PACK_CONTENTS.md` 🔧 TEMPLATE
**Location**: `_internal/docs/starter-pack/`
**Purpose**: Detailed template contents documentation
**Content**: File counts, directory structure, statistics
**Customize**: Update if template structure changes
**Must Edit**: No

---

### Project Management

#### `_internal/project/README.md` 🔒 INTERNAL
**Location**: `_internal/project/`
**Purpose**: Overview of project management structure
**Customize**: Update with project-specific PM info
**Must Edit**: Optional

---

#### `_internal/project/AGENT_START_HERE.md` 🔒 INTERNAL
**Location**: `_internal/project/`
**Purpose**: Primary entry point for AI agents (Tier 0 context)
**Size Limit**: <5KB
**Customize**: MUST customize with:
- Project overview
- Current status and priorities
- Architecture summary
- Key conventions
- Common task quick reference
**Format**: Markdown
**Must Edit**: Yes (critical)

**Template**:
```markdown
# Agent Start Here - [Project Name]

## Project Overview
What this project does and why it exists

## Current Status
- Phase: [Alpha/Beta/Production]
- Priority: [Current focus]
- Version: X.Y.Z

## Architecture at a Glance
[2-3 paragraph high-level overview]

## Key Conventions
- Convention 1
- Convention 2

## Where to Find More
[Context navigation]

## Common Tasks
[Quick how-tos]
```

---

#### `_internal/project/context/essential/checklists.md` 🔒 INTERNAL
**Location**: `_internal/project/context/essential/`
**Purpose**: Essential checklists (Tier 0 context)
**Size Limit**: <5KB
**Customize**: Add project-specific checklists:
- Definition of Done
- Code review checklist
- Pre-deployment checklist
- Security checklist
**Must Edit**: Yes (add project checklists)

**Template**:
```markdown
# Essential Checklists

## Definition of Done
- [ ] Tests written and passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] [Project-specific items]

## Code Review Checklist
- [ ] Follows coding standards
- [ ] Has tests
- [ ] [Project-specific items]
```

---

#### `_internal/project/context/essential/warnings.md` 🔒 INTERNAL
**Location**: `_internal/project/context/essential/`
**Purpose**: Critical warnings and gotchas (Tier 0 context)
**Size Limit**: <5KB
**Customize**: Add project-specific warnings:
- Common pitfalls
- Security gotchas
- Performance issues
- Data handling warnings
**Must Edit**: Yes (add project gotchas)

**Template**:
```markdown
# Essential Warnings

## Common Pitfalls
- [Pitfall 1]: [Why and how to avoid]
- [Pitfall 2]: [Why and how to avoid]

## Security
- [Security concern 1]
- [Security concern 2]

## Performance
- [Performance issue 1]
- [Performance issue 2]
```

---

#### `_internal/project/learnings/raw/sessions/template.md` 🔧 TEMPLATE
**Location**: `_internal/project/learnings/raw/sessions/`
**Purpose**: Template for session logs
**Usage**: Copy and rename to `YYYY-MM-DD-topic.md`
**Must Edit**: No (it's a template)

**Use For**: Logging development sessions
**Format**:
```markdown
# Session: [Topic] - YYYY-MM-DD

## Goal
What were we trying to accomplish?

## Approach
How did we approach it?

## What Worked
- Success 1

## What Didn't Work
- Challenge 1

## Learnings
- Learning 1

## Next Steps
- [ ] Task 1

## Distillation Candidates
- [ ] Pattern: [Name] → situational/patterns.md
- [ ] Gotcha: [Name] → essential/warnings.md
```

---

### Reports

#### `_internal/reports/README.md` 🔒 INTERNAL
**Location**: `_internal/reports/`
**Purpose**: Explain reports structure and archival policy
**Content**: How to use reports/, when to archive
**Must Edit**: No

---

## 📚 `docs/` - Public Documentation

### `docs/README.md` ✅ PUBLIC
**Location**: `docs/`
**Purpose**: Documentation table of contents
**Customize**:
- Add links to your documentation sections
- Update structure as docs grow
**Format**: Markdown
**Must Edit**: Yes (as you add docs)

**Template**:
```markdown
# Documentation

## Getting Started
- [Installation](guides/getting-started/installation.md)
- [Quick Start](guides/getting-started/quick-start.md)

## Guides
- [User Guide](guides/user-guides/README.md)
- [Developer Guide](guides/developer-guides/README.md)

## Reference
- [API Reference](reference/api/README.md)
- [Architecture](reference/architecture/README.md)
```

---

## 🔧 `scripts/` - Public Utility Scripts

### `scripts/README.md` ✅ PUBLIC
**Location**: `scripts/`
**Purpose**: Document available utility scripts
**Customize**: Add description for each script you add
**Must Edit**: Yes (as you add scripts)

---

### `scripts/setup.py` ✅ PUBLIC
**Location**: `scripts/`
**Purpose**: Development environment setup automation
**Language**: Python
**Customize**: Add project-specific setup steps
**Permissions**: Executable (`chmod +x`)
**Must Edit**: Optional

**Actions**:
1. Create virtual environment
2. Install dependencies
3. Run migrations (if applicable)
4. Verify installation

**Usage**: `./scripts/setup.py` or `python scripts/setup.py`

---

### `scripts/lint.py` ✅ PUBLIC
**Location**: `scripts/`
**Purpose**: Run linting and formatting
**Language**: Python
**Customize**: Add additional linting tools if needed
**Permissions**: Executable
**Must Edit**: Optional

**Actions**:
1. Run `ruff check`
2. Run `ruff format --check`
3. Exit with error code if issues

**Usage**: `./scripts/lint.py` or `python scripts/lint.py`

---

### `scripts/test.py` ✅ PUBLIC
**Location**: `scripts/`
**Purpose**: Run test suite
**Language**: Python
**Customize**: Add test filtering, additional test commands
**Permissions**: Executable
**Must Edit**: Optional

**Actions**:
1. Run pytest with coverage
2. Generate coverage report
3. Support test type filtering (--unit, --integration, --e2e)

**Usage**: `./scripts/test.py` or `python scripts/test.py --unit`

---

## 💻 `src/` - Source Code

### `src/PROJECT_NAME/__init__.py` ✅ PUBLIC
**Location**: `src/PROJECT_NAME/`
**Purpose**: Package initialization
**Customize**:
- Update `__version__` as you release
- Export public API
**Must Edit**: Rename directory from PROJECT_NAME to your package

**Template**:
```python
"""PROJECT_NAME package."""

__version__ = "0.1.0"

# Export public API
__all__ = []
```

---

### `src/PROJECT_NAME/__main__.py` ✅ PUBLIC
**Location**: `src/PROJECT_NAME/`
**Purpose**: CLI entry point
**Usage**: Enables `python -m PROJECT_NAME`
**Customize**: Add CLI commands for your project
**Must Edit**: Yes (implement your CLI)

**Template**:
```python
"""CLI entry point."""

def main():
    """Main CLI function."""
    print("Hello from PROJECT_NAME!")

if __name__ == "__main__":
    main()
```

---

### `src/PROJECT_NAME/core/__init__.py` ✅ PUBLIC
**Location**: `src/PROJECT_NAME/core/`
**Purpose**: Core business logic module
**Content**: Placeholder, add your core logic
**Must Edit**: Yes (add implementation)

---

### `src/PROJECT_NAME/models/__init__.py` ✅ PUBLIC
**Location**: `src/PROJECT_NAME/models/`
**Purpose**: Data models module
**Content**: Placeholder, add your models
**Must Edit**: Yes (add implementation)

**Examples**:
- Database models (SQLAlchemy, Django ORM)
- Pydantic models (validation)
- Dataclasses
- Type definitions

---

### `src/PROJECT_NAME/utils/__init__.py` ✅ PUBLIC
**Location**: `src/PROJECT_NAME/utils/`
**Purpose**: Utility functions module
**Content**: Placeholder, add utilities
**Must Edit**: Yes (add utilities as needed)

**Examples**:
- String formatting
- Date/time helpers
- File I/O helpers
- Logging configuration

---

## 🧪 `tests/` - Test Suite

### `tests/__init__.py` ✅ PUBLIC
**Location**: `tests/`
**Purpose**: Mark tests as package
**Content**: Usually empty or with test helpers
**Must Edit**: No

---

### `tests/conftest.py` ✅ PUBLIC
**Location**: `tests/`
**Purpose**: pytest configuration and shared fixtures
**Customize**: Add project-specific fixtures
**Must Edit**: Yes (add fixtures as needed)

**Template**:
```python
"""Pytest configuration and fixtures."""
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value"}

# Define custom markers
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
```

---

### `tests/unit/test_example.py` ✅ PUBLIC
**Location**: `tests/unit/`
**Purpose**: Example unit test
**Customize**: Replace with real tests
**Must Edit**: Yes (replace example)

**Template**:
```python
"""Example unit tests."""

def test_example():
    """Example test - replace with real tests."""
    assert 1 + 1 == 2

def test_another_example():
    """Another example - replace with real tests."""
    assert True
```

**Naming Convention**: `test_[function]_[scenario]_[expected]`

---

### Empty Directories with `.gitkeep`

The following directories are created with `.gitkeep` files to preserve directory structure in git:

#### `tests/integration/.gitkeep`
**Purpose**: Preserve integration tests directory
**Delete**: After adding first integration test

#### `tests/e2e/.gitkeep`
**Purpose**: Preserve e2e tests directory
**Delete**: After adding first e2e test

#### `tests/fixtures/.gitkeep`
**Purpose**: Preserve test fixtures directory
**Delete**: After adding first fixture file

---

## 📊 File Counts Summary

| Category | Count | Visibility |
|----------|-------|------------|
| Root config files | 7 | Public |
| Root AI files | 1 | Internal |
| GitHub workflows | 1 | Public |
| GitHub AI files | 1 | Internal |
| Internal PM files | 5 | Internal |
| Internal docs | 3 | Internal |
| Public docs | 1 | Public |
| Public scripts | 4 | Public |
| Source files | 5 | Public |
| Test files | 2 + fixtures | Public |
| **Total Template Files** | **30+** | Mixed |

---

## 🎯 Customization Priority

### Must Customize (High Priority)

1. ✅ **Rename** `src/PROJECT_NAME/` → `src/your_package/`
2. ✅ **Update** `pyproject.toml` (name, authors, description, dependencies)
3. ✅ **Update** `README.md` (description, features, usage)
4. ✅ **Update** `LICENSE` (copyright holder and year)
5. ✅ **Update** `AGENTS.md` (project-specific info)
6. ✅ **Update** `.github/copilot-instructions.md` (comprehensive context)
7. ✅ **Update** `_internal/project/AGENT_START_HERE.md` (entry point)

### Should Customize (Medium Priority)

8. **Update** `_internal/project/context/essential/checklists.md`
9. **Update** `_internal/project/context/essential/warnings.md`
10. **Replace** `tests/unit/test_example.py` with real tests
11. **Implement** `src/PROJECT_NAME/__main__.py` (CLI)
12. **Update** `docs/README.md` (doc index)

### Can Customize (Low Priority)

13. **Adjust** `.github/workflows/ci.yml` (Python versions, add deployment)
14. **Adjust** `.python-version` (if targeting different version)
15. **Add to** `scripts/` (project-specific automation)
16. **Update** `CHANGELOG.md` (as you develop)

---

## 🔍 Quick File Finder

**Need to find a file?** Use this reference:

| What I need | File Location |
|-------------|---------------|
| Project config | `pyproject.toml` |
| Quick agent ref | `AGENTS.md` |
| Detailed agent instructions | `.github/copilot-instructions.md` |
| Agent entry point | `_internal/project/AGENT_START_HERE.md` |
| Checklists | `_internal/project/context/essential/checklists.md` |
| Warnings/gotchas | `_internal/project/context/essential/warnings.md` |
| Session log template | `_internal/project/learnings/raw/sessions/template.md` |
| CI/CD pipeline | `.github/workflows/ci.yml` |
| Public docs | `docs/README.md` |
| Dev setup script | `scripts/setup.py` |
| Linting script | `scripts/lint.py` |
| Test script | `scripts/test.py` |
| Package init | `src/PROJECT_NAME/__init__.py` |
| CLI entry | `src/PROJECT_NAME/__main__.py` |
| Test config | `tests/conftest.py` |
| Example tests | `tests/unit/test_example.py` |

---

**Version**: 1.0.0
**Last Updated**: 2025-11-05
**Maintained By**: Company Engineering Team
