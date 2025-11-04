# Python Project Structure - Single Source of Truth (SST)

> **🔗 SST Authority Notice**
> 
> This is a **synced copy** from the canonical source in second-brain.
> 
> - **Authoritative Source**: `/home/jpw/git/second-brain/3. Resource/Python Project Structure/`
> - **This Copy**: Reference implementation in 1C4D5 project
> - **Golden Rule**: When conflicts arise, second-brain version takes precedence
> - **Updates**: Should be made in second-brain first, then synced here

**Version**: 1.0.0  
**Last Updated**: 2025-10-21  
**Status**: Synced Reference Copy  
**Purpose**: Standard structure for Python projects with AI agent collaboration

---

## 🎯 Overview

This document defines the canonical project structure for Python projects, incorporating lessons learned from the 1C4D5 project. It balances human readability with AI agent effectiveness, ensuring clear separation between stable knowledge, transient status, and collaborative context.

**Key Principles**:
- **Separation of Concerns**: Stable docs vs. transient reports vs. collaborative context
- **SST Compliance**: Single source of truth for all authoritative content
- **Agent-Friendly**: Tiered context system for efficient AI collaboration
- **Automation-First**: Scripts for common tasks, deterministic workflows
- **Quality Gates**: Linting, testing, and validation built-in

---

## 📁 Canonical Directory Structure

```
project-name/
│
├── .github/                      # GitHub-specific configuration
│   ├── workflows/                # CI/CD pipelines (lint, test, deploy)
│   ├── copilot-instructions.md   # AI agent comprehensive instructions
│   └── ISSUE_TEMPLATE/           # Issue templates
│
├── docs/                         # Stable Knowledge (Lifespan: 6+ months)
│   ├── README.md                 # Documentation master index
│   ├── framework/                # Methodology/framework specs (if applicable)
│   │   ├── README.md
│   │   └── *.md                  # Framework specifications
│   ├── guides/                   # How-to guides & tutorials
│   │   ├── README.md
│   │   ├── getting-started/      # Onboarding materials
│   │   ├── user-guides/          # End-user documentation
│   │   └── developer-guides/     # Contributing & development
│   ├── reference/                # Technical references
│   │   ├── README.md
│   │   ├── architecture/         # Design decisions & patterns
│   │   ├── api/                  # API documentation
│   │   └── data-models/          # Schema & data model docs
│   ├── decisions/                # Architecture Decision Records (ADRs)
│   │   ├── README.md             # ADR index & template
│   │   └── NNNN-title.md         # Individual ADRs
│   ├── investigations/           # Research & spike results
│   │   ├── README.md
│   │   └── *.md                  # Investigation reports
│   └── assets/                   # Binary resources
│       ├── diagrams/
│       ├── screenshots/
│       └── icons/
│
├── reports/                      # Transient Knowledge (Point-in-time status)
│   ├── README.md                 # Reports index & archival policy
│   ├── *.md                      # Active reports (QA, status, reviews)
│   └── archive/                  # Completed/historical reports
│       ├── ARCHIVE_SUMMARY.md    # Why each report was archived
│       └── YYYY-MM-DD_*.md       # Archived reports with timestamps
│
├── project/                      # AI Agent Collaboration System
│   ├── README.md                 # Project management overview
│   ├── AGENT_START_HERE.md       # Agent entry point (<5KB)
│   ├── context/                  # Tiered context files
│   │   ├── essential/            # Tier 0: Always load (<5KB each)
│   │   │   ├── checklists.md
│   │   │   ├── warnings.md
│   │   │   └── quick-wins.md
│   │   ├── situational/          # Tier 1: Load as needed (5-20KB)
│   │   │   ├── patterns.md
│   │   │   ├── antipatterns.md
│   │   │   └── solutions.md
│   │   ├── reference/            # Tier 2: Lookup only (20KB+)
│   │   │   ├── patterns-full.md
│   │   │   ├── antipatterns-full.md
│   │   │   └── decisions-full.md
│   │   └── archive/              # Tier 3: Historical context
│   ├── learnings/                # Knowledge capture & distillation
│   │   ├── raw/                  # Raw session logs
│   │   │   └── sessions/         # Individual session logs
│   │   │       └── template.md   # Session log template
│   │   └── distilled/            # Aggregated summaries
│   │       ├── weekly/           # Weekly digests
│   │       ├── monthly/          # Monthly summaries
│   │       └── patterns/         # Extracted patterns
│   ├── process/                  # Team processes & workflows
│   │   ├── development-standards.md
│   │   ├── definition-of-done.md
│   │   ├── code-review.md
│   │   └── release-process.md
│   ├── planning/                 # Roadmap & milestones
│   │   ├── roadmap.md
│   │   ├── milestones.md
│   │   └── iterations/
│   ├── backlog/                  # Work items
│   │   ├── active-tasks.md
│   │   ├── backlog.md
│   │   └── ideas.md
│   ├── metrics/                  # Effectiveness tracking
│   │   ├── velocity.md
│   │   └── quality-metrics.md
│   ├── .distillation/            # Automation for context improvement
│   │   ├── distill-agent.py      # Distillation automation script
│   │   └── prompts/              # LLM prompts for distillation
│   └── onboarding/               # New team member resources
│       ├── humans.md
│       └── agents.md
│
├── scripts/                      # Utility scripts
│   ├── README.md                 # Scripts documentation
│   ├── setup.py                  # Development environment setup
│   ├── lint.py                   # Linting automation
│   ├── test.py                   # Test automation
│   └── *.py                      # Other utility scripts
│
├── specs/                        # Formal specifications
│   ├── NNN-feature-name/         # Numbered spec folders
│   │   ├── spec.md               # User stories, FR/NFR
│   │   ├── data-model.md         # Entity schemas, relationships
│   │   └── acceptance.md         # Acceptance criteria
│   └── README.md                 # Spec index
│
├── src/                          # Source code (or package-name/)
│   ├── __init__.py
│   ├── core/                     # Core business logic
│   ├── models/                   # Data models
│   ├── services/                 # Service layer
│   ├── utils/                    # Utilities
│   └── cli/                      # CLI entry points (if applicable)
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   ├── e2e/                      # End-to-end tests
│   ├── fixtures/                 # Test fixtures & data
│   └── conftest.py               # Pytest configuration
│
├── .vscode/                      # VS Code configuration (optional)
│   ├── settings.json
│   ├── extensions.json
│   └── launch.json
│
├── .gitignore                    # Git ignore rules
├── .python-version               # Python version (pyenv)
├── pyproject.toml                # Project metadata, deps, tool config
├── requirements.txt              # Production dependencies (or use pyproject.toml)
├── requirements-dev.txt          # Development dependencies
├── README.md                     # Project overview & quick start
├── AGENTS.md                     # AI agent quick reference
├── CHANGELOG.md                  # Version history
├── LICENSE                       # License file
└── Makefile or justfile          # Task automation (optional)
```

---

## 📖 Directory Purposes & Guidelines

### Root Level Files

#### `README.md` - Project Overview
**Purpose**: First impression, quick start, essential links  
**Contents**:
- Project description (1-2 paragraphs)
- Quick start instructions (< 5 minutes to first success)
- Installation steps
- Basic usage examples
- Link to full documentation
- Badges (build status, coverage, version)

#### `AGENTS.md` - AI Agent Quick Reference
**Purpose**: Compact guide for AI agents (< 10KB)  
**Contents**:
- Project structure overview
- Common commands
- Key conventions
- Critical gotchas
- Common tasks with examples
- Links to detailed docs

#### `pyproject.toml` - Project Configuration
**Purpose**: Central configuration for Python tooling  
**Contents**:
- Package metadata (name, version, description, authors)
- Dependencies (using PEP 621 format)
- Build system configuration
- Tool configurations (pytest, ruff, mypy, black, etc.)

**Example**:
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Short description"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.ruff]
line-length = 88
target-version = "py39"

[tool.mypy]
python_version = "3.9"
strict = true
```

---

### `docs/` - Stable Knowledge

**Lifespan**: 6+ months  
**Audience**: Anyone who needs to understand the project deeply  
**Archival Policy**: Never archive; update in place or deprecate explicitly

#### `docs/README.md` - Documentation Index
**Purpose**: Master navigation hub for all documentation  
**Must Include**:
- Clear hierarchy of all docs
- Quick answers to common questions
- Learning paths for different audiences
- "Find by topic" index
- Document relationship diagram

#### `docs/framework/` - Methodology Specifications
**When to Use**: Project implements or extends a methodology/framework  
**Examples**:
- D5 Framework specification
- Custom methodology definitions
- Canonical design patterns

**Don't Use For**: Implementation-specific architecture (goes in `reference/architecture/`)

#### `docs/guides/` - How-To Documentation
**Structure**:
- `getting-started/` - Onboarding (installation, first steps, tutorials)
- `user-guides/` - End-user documentation (features, usage patterns)
- `developer-guides/` - Contributing, extending, testing

**Guideline**: Each guide should be **actionable** - readers should be able to complete a task after reading.

#### `docs/reference/` - Technical References
**Structure**:
- `architecture/` - Design decisions, patterns, system design
- `api/` - API documentation (auto-generated or manual)
- `data-models/` - Schemas, entity relationships

**Guideline**: Reference docs are for **lookup**, not learning. Optimize for findability.

#### `docs/decisions/` - Architecture Decision Records
**Format**: Use ADR template  
**Naming**: `NNNN-title-in-kebab-case.md` (e.g., `0001-use-postgresql.md`)  
**Structure**:
```markdown
# NNNN. Title

Date: YYYY-MM-DD
Status: [Proposed | Accepted | Deprecated | Superseded by XXXX]

## Context
What is the issue we're facing?

## Decision
What decision did we make?

## Consequences
What are the positive and negative outcomes?

## Alternatives Considered
What other options did we evaluate?
```

#### `docs/investigations/` - Research & Spikes
**Purpose**: Document exploratory work, proof-of-concepts, deep-dive analysis  
**When to Archive**: When investigation is complete AND decision is made (create ADR, move investigation to archive)

---

### `reports/` - Transient Knowledge

**Lifespan**: Weeks to months (point-in-time)  
**Audience**: Current team members tracking status  
**Archival Policy**: Archive when obsolete (completed, superseded, no longer relevant)

#### Common Report Types
- `QA_REPORT.md` - Test coverage, quality metrics, known issues
- `STATUS_REPORT.md` - Current project status
- `*_REVIEW.md` - Code reviews, documentation reviews
- `*_INVESTIGATION_RESULTS.md` - Completed investigations (before moving to decisions/)
- `*_IMPLEMENTATION.md` - Implementation summaries for completed features

#### Archival Process
1. Move to `reports/archive/` with timestamp prefix: `YYYY-MM-DD_ORIGINAL_NAME.md`
2. Update `reports/archive/ARCHIVE_SUMMARY.md` with reason and date
3. Optional: Add redirect in original location if frequently referenced

**Archive When**:
- Report is completed and no longer being updated
- Report is superseded by newer information
- Report content has been incorporated into stable docs

---

### `project/` - AI Agent Collaboration System

**Purpose**: Structured context and knowledge management for AI agents  
**Key Innovation**: Tiered context system optimizes token usage and agent effectiveness

#### Context Tiers

| Tier | Size | When to Load | Examples | Update Frequency |
|------|------|--------------|----------|------------------|
| 0 - Essential | <5KB | Always | Checklists, warnings, critical gotchas | Weekly |
| 1 - Situational | 5-20KB | When relevant | Patterns, anti-patterns, common solutions | Monthly |
| 2 - Reference | 20KB+ | Lookup only | Full catalogs, complete histories | Quarterly |
| 3 - Archive | Unlimited | Rarely | Old sessions, deprecated patterns | Never (read-only) |

#### `project/AGENT_START_HERE.md`
**Critical**: Must be < 5KB  
**Contents**:
- Project overview (2-3 sentences)
- Essential context pointers
- Common commands
- Top 5 gotchas
- Where to find detailed info

#### `project/learnings/` - Knowledge Capture
**Structure**:
- `raw/sessions/` - Individual agent session logs (use template)
- `distilled/weekly/` - Weekly aggregated summaries
- `distilled/monthly/` - Monthly trend analysis
- `distilled/patterns/` - Extracted recurring patterns

**Session Log Template**:
```markdown
# Session Log - YYYY-MM-DD - Brief Description

**Date**: YYYY-MM-DD
**Agent**: [Claude/GPT-4/etc.]
**Duration**: ~X hours
**Outcome**: [Success/Partial/Blocked]

## Context
What was the goal?

## Work Completed
- Bullet list of what was done

## Key Decisions
- Important decisions made during session

## Learnings
### What Worked
- Patterns that were effective

### What Didn't Work
- Anti-patterns to avoid

### Gaps in Context
- What context was missing that would have helped?

## Artifacts Created
- Files created/modified
- Reports generated

## Next Steps
- What should happen next?

## Links
- Related docs, PRs, issues
```

#### `project/.distillation/` - Automation
**`distill-agent.py`** - Automated distillation script  
**Usage**:
```bash
# Weekly distillation (aggregate last 7 days of sessions)
python project/.distillation/distill-agent.py --weekly

# Monthly distillation
python project/.distillation/distill-agent.py --monthly

# Extract patterns
python project/.distillation/distill-agent.py --extract-patterns
```

---

### `scripts/` - Utility Scripts

**Purpose**: Automation for common development tasks  
**Guideline**: Every script must have help text and examples

#### Essential Scripts

**`scripts/setup.py`** - Development Environment Setup
```python
#!/usr/bin/env python3
"""
Setup development environment.

Usage:
    python scripts/setup.py [--full]
    
Options:
    --full    Install all optional dependencies
"""
# Install deps, create .env, setup hooks, etc.
```

**`scripts/lint.py`** - Linting Automation
```python
#!/usr/bin/env python3
"""
Run all linting checks.

Usage:
    python scripts/lint.py [--fix]
    
Options:
    --fix    Auto-fix issues where possible
"""
# Run ruff, mypy, black, etc.
```

**`scripts/test.py`** - Test Automation
```python
#!/usr/bin/env python3
"""
Run test suite with common options.

Usage:
    python scripts/test.py [--fast|--coverage|--watch]
    
Options:
    --fast       Skip slow tests
    --coverage   Generate coverage report
    --watch      Watch mode (re-run on changes)
"""
# Run pytest with appropriate flags
```

#### Script Conventions
- **Shebang**: `#!/usr/bin/env python3`
- **Docstring**: Module docstring with usage examples
- **Help flag**: Support `--help` or `-h`
- **Exit codes**: 0 = success, non-zero = error
- **Verbose output**: Print what's happening
- **Error handling**: Clear error messages

---

### `specs/` - Formal Specifications

**Purpose**: Detailed requirements and acceptance criteria  
**Structure**: One folder per major feature/component

#### Spec Folder Contents
- `spec.md` - User stories, functional/non-functional requirements
- `data-model.md` - Entity schemas, relationships, validation rules
- `acceptance.md` - Acceptance criteria, test scenarios
- `diagrams/` - Supporting diagrams

**When to Create**: Before implementing significant features  
**When to Update**: When requirements change (maintain history via git)

---

### `src/` - Source Code

**Purpose**: Production code  
**Alternative**: Use package name instead (e.g., `my_package/`)

#### Recommended Structure
```
src/
├── __init__.py              # Package root
├── core/                    # Core business logic
│   ├── __init__.py
│   └── *.py
├── models/                  # Data models, schemas
│   ├── __init__.py
│   └── *.py
├── services/                # Service layer (business operations)
│   ├── __init__.py
│   └── *.py
├── repositories/            # Data access layer (if applicable)
│   ├── __init__.py
│   └── *.py
├── utils/                   # Utilities, helpers
│   ├── __init__.py
│   └── *.py
├── cli/                     # CLI entry points
│   ├── __init__.py
│   └── *.py
└── api/                     # API/web layer (if applicable)
    ├── __init__.py
    └── *.py
```

**Conventions**:
- One class per file (usually)
- File name matches primary class name (snake_case)
- Public interface in `__init__.py`
- Avoid circular imports

---

### `tests/` - Test Suite

**Purpose**: Automated testing at all levels  
**Structure**:
```
tests/
├── __init__.py
├── unit/                    # Fast, isolated tests
│   ├── test_core.py
│   └── test_utils.py
├── integration/             # Tests with dependencies
│   └── test_database.py
├── e2e/                     # End-to-end tests
│   └── test_workflows.py
├── fixtures/                # Test data, sample files
│   ├── sample_data.json
│   └── valid_config.yaml
└── conftest.py              # Pytest configuration, fixtures
```

**Naming Conventions**:
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_<what>_<condition>_<expected>()`
- Test classes: `Test<ClassName>`

**Example Test**:
```python
def test_parser_with_valid_input_returns_parsed_data():
    """Parser should successfully parse valid input."""
    input_data = "valid data"
    result = parse(input_data)
    assert result.is_valid
    assert result.data == expected_output
```

---

## 🔧 Tool Configuration

### `pyproject.toml` - Centralized Configuration

**Recommended Tools**:
- **Ruff**: Fast linter & formatter (replaces black, isort, flake8)
- **Mypy**: Static type checking
- **Pytest**: Testing framework
- **Coverage.py**: Code coverage

**Example Configuration**:
```toml
[tool.ruff]
line-length = 88
target-version = "py39"
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["B008"]  # function calls in arguments

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
exclude = ["tests/"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "-ra",
]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]

[tool.coverage.run]
source = ["src"]
omit = ["tests/*", "scripts/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]
```

---

## 🚀 Quick Start Template

### Minimal Python Project Setup

```bash
# Create directory structure
mkdir -p my-project/{src/my_package,tests/{unit,integration,fixtures},docs/{guides,reference,decisions},scripts,specs,reports/archive,project/{context/{essential,situational,reference,archive},learnings/{raw/sessions,distilled/{weekly,monthly,patterns}},process,planning,backlog,metrics,.distillation}}

# Create essential files
touch my-project/{README.md,AGENTS.md,pyproject.toml,.gitignore,.python-version}
touch my-project/src/my_package/__init__.py
touch my-project/tests/{__init__.py,conftest.py}
touch my-project/docs/README.md
touch my-project/reports/README.md
touch my-project/project/{README.md,AGENT_START_HERE.md}
touch my-project/scripts/README.md

# Initialize git
cd my-project
git init

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows

# Install dev dependencies
pip install -e ".[dev]"
```

### Essential `.gitignore`
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

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project-specific
.env
*.log
```

---

## 📋 Agent Workflows

### Workflow 1: Starting a Session
1. Read `project/AGENT_START_HERE.md` (< 30 seconds)
2. Load Tier 0 context from `project/context/essential/`
3. Review relevant Tier 1 context based on task
4. Check active reports in `reports/`
5. Begin work

### Workflow 2: Completing a Session
1. Create session log using `project/learnings/raw/sessions/template.md`
2. Document key decisions, learnings, gaps
3. Update relevant context files if patterns emerged
4. Create/update reports if status changed
5. Commit session log

### Workflow 3: Weekly Distillation
1. Run `python project/.distillation/distill-agent.py --weekly`
2. Review generated weekly digest
3. Update situational context with new patterns
4. Archive obsolete context to Tier 3
5. Update `AGENT_START_HERE.md` if essentials changed

### Workflow 4: Adding Documentation
1. Determine category: framework/guide/reference/decision/investigation
2. Create file in appropriate `docs/` subfolder
3. Update `docs/README.md` index
4. Add cross-references to related docs
5. Update `AGENTS.md` if affects common tasks

### Workflow 5: Archiving Reports
1. Confirm report is obsolete (completed/superseded/no longer relevant)
2. Move to `reports/archive/` with timestamp: `YYYY-MM-DD_ORIGINAL_NAME.md`
3. Update `reports/archive/ARCHIVE_SUMMARY.md` with reason
4. Remove from active reports index in `reports/README.md`
5. Add redirect comment in original location if needed

---

## 🎯 Quality Gates

### Pre-Commit Checks
```bash
# Lint
ruff check src/ tests/

# Type check
mypy src/

# Format check
ruff format --check src/ tests/

# Test
pytest tests/unit/  # Fast tests only for pre-commit
```

### CI Pipeline Checks
```bash
# Full lint
ruff check src/ tests/ scripts/

# Type check
mypy src/

# Format check
ruff format --check .

# Test with coverage
pytest --cov=src --cov-report=term --cov-report=html

# Coverage threshold
coverage report --fail-under=80
```

### Documentation Checks
```bash
# Check for broken links (add custom script)
python scripts/check-links.py docs/

# Check Tier 0 context size
python scripts/check-context-size.py project/context/essential/

# Validate session logs
python scripts/validate-session-logs.py project/learnings/raw/sessions/
```

---

## 🏆 Best Practices

### For Humans

**DO**:
- ✅ Keep `AGENT_START_HERE.md` under 5KB
- ✅ Update docs when making significant changes
- ✅ Create session logs after substantial work
- ✅ Run distillation weekly
- ✅ Archive reports promptly when obsolete
- ✅ Use ADRs for architectural decisions
- ✅ Keep README.md focused on quick start

**DON'T**:
- ❌ Duplicate content between docs/ and project/context/
- ❌ Let reports/ grow unbounded without archiving
- ❌ Skip session logs ("I'll remember this")
- ❌ Put transient status in stable docs/
- ❌ Create docs without updating the index
- ❌ Hardcode secrets in scripts

### For AI Agents

**DO**:
- ✅ Always read `AGENT_START_HERE.md` first
- ✅ Load context by tier (0 always, 1 as needed, 2 lookup only)
- ✅ Create session logs after significant work
- ✅ Document gaps in context (helps improve future sessions)
- ✅ Link to SST docs rather than duplicating
- ✅ Check reports/ for current status before starting
- ✅ Use scripts for repetitive tasks

**DON'T**:
- ❌ Load all context indiscriminately (token waste)
- ❌ Duplicate SST content in summaries
- ❌ Skip reading essential/ context files
- ❌ Create new patterns without checking existing ones
- ❌ Modify stable docs without verification
- ❌ Generate random/non-deterministic identifiers

---

## 🔄 Maintenance Schedules

### Weekly
- Run distillation automation
- Archive completed reports
- Review and update Tier 1 context

### Monthly
- Review Tier 2 context for updates
- Update roadmap and milestones
- Generate monthly learning summary

### Quarterly
- Major documentation review
- Archive old session logs to Tier 3
- Update development standards
- Review and prune dependencies

### As Needed
- Create ADRs for major decisions
- Update guides when features change
- Add investigations for research spikes
- Create new Tier 0 warnings for critical gotchas

---

## 📚 References

### SST Location
- **Canonical SST**: `/home/jpw/git/second-brain/3. Resource/Python Project Structure/`
- **This Copy**: Synced reference implementation in 1C4D5 project
- **Sync Protocol**: Updates made in second-brain, synced to implementations

### Internal (1C4D5 Project)
- **This SST is based on**: 1C4D5 project structure and learnings
- **Key influence docs**:
  - `1C4D5/AGENTS.md` - Agent workflows and conventions
  - `1C4D5/project/README.md` - Context tier system
  - `1C4D5/docs/README.md` - Documentation organization
  - `1C4D5/.github/copilot-instructions.md` - Comprehensive patterns

### External Resources
- **PEP 621**: Dependency specification in `pyproject.toml`
- **ADR**: Architecture Decision Records (adr.github.io)
- **Ruff**: Fast Python linter (docs.astral.sh/ruff)
- **Pytest**: Testing framework (docs.pytest.org)

---

## 🆘 Common Questions

**Q: Where do I put X?**
- **Stable methodology/framework spec** → `docs/framework/`
- **How-to guide** → `docs/guides/`
- **Technical reference** → `docs/reference/`
- **Design decision** → `docs/decisions/`
- **Research/spike** → `docs/investigations/`
- **Current status/review** → `reports/`
- **Agent context** → `project/context/` (by tier)
- **Session notes** → `project/learnings/raw/sessions/`

**Q: When should I archive a report?**
- When completed and no longer being updated
- When superseded by newer information
- When content incorporated into stable docs
- When no longer relevant to current work

**Q: How do I know which context tier?**
- **Tier 0**: Would an agent fail without this? (checklists, warnings)
- **Tier 1**: Would an agent struggle without this? (patterns, solutions)
- **Tier 2**: Is this lookup-only reference? (full catalogs, complete history)
- **Tier 3**: Is this historical only? (old sessions, deprecated patterns)

**Q: Should I use Makefile or justfile?**
- Either is fine for task automation
- Ensure `make help` or `just --list` shows available commands
- Document in README.md and scripts/README.md

**Q: Where do configuration files go?**
- **Project config** → `pyproject.toml` (preferred)
- **Tool-specific** → Root level (`.ruff.toml`, `.mypy.ini`) if can't use pyproject.toml
- **Editor-specific** → `.vscode/`, `.idea/` (gitignore or commit based on team preference)

**Q: How big should session logs be?**
- 1-3 pages typical (500-1500 words)
- Focus on decisions, learnings, and gaps
- Link to artifacts rather than duplicating content

---

**Version History**:
- **1.0.0** (2025-10-21): Initial SST based on 1C4D5 project learnings

**Maintained By**: Project maintainers  
**Feedback**: Submit issues or contact maintainers