# Python Project Structure Reference

Complete directory structure documentation for AI agents and developers. This reference explains the purpose, content guidelines, and usage of every directory in the project template.

---

## 📊 Structure Overview

```
project-name/
├── _internal/          # ⚠️  INTERNAL ONLY - Project management & context
├── .github/            # GitHub configuration (workflows + agent instructions)
├── docs/               # ✅ PUBLIC - User-facing documentation
├── scripts/            # ✅ PUBLIC - Utility automation
├── src/                # ✅ PUBLIC - Source code
├── tests/              # ✅ PUBLIC - Test suite
└── [config files]      # ✅ PUBLIC - Standard project configuration
```

**Legend:**
- ✅ PUBLIC - Included in public repository
- ⚠️  INTERNAL - Excluded from public repository (company policy)
- 🔒 RESTRICTED - AI artifacts kept for internal use only

---

## 🔐 Root Level Files

### Configuration Files (PUBLIC)

#### `README.md`
**Purpose**: Project overview and quick start guide
**Audience**: Public users, contributors
**Content**:
- Project description and features
- Installation instructions
- Quick start examples
- Links to documentation
- Contributing guidelines (link to CONTRIBUTING.md if exists)
- License information

**Template Variables**:
- `PROJECT_NAME` - Package/module name
- `PROJECT_DISPLAY_NAME` - Human-readable project name
- `USERNAME` - GitHub username or organization

---

#### `pyproject.toml`
**Purpose**: Python project configuration (PEP 518/621)
**Audience**: Build tools, developers
**Content**:
- Project metadata (name, version, description, authors)
- Dependencies (runtime and development)
- Tool configuration:
  - **Ruff**: Linting and formatting
  - **Mypy**: Type checking
  - **Pytest**: Testing framework
  - **Coverage**: Code coverage settings
- Entry points (CLI commands)

**Key Sections**:
```toml
[project]                    # Metadata
[project.optional-dependencies]  # Dev dependencies
[tool.ruff]                  # Linting config
[tool.mypy]                  # Type checking config
[tool.pytest.ini_options]    # Test configuration
[tool.coverage.run]          # Coverage settings
```

**Customization Required**:
- Project name and description
- Author name and email
- Repository URLs
- Version number
- Dependencies list

---

#### `CHANGELOG.md`
**Purpose**: Version history and release notes
**Audience**: Users, contributors
**Format**: Keep a Changelog format
**Content**:
- Unreleased changes
- Released versions with dates
- Categories: Added, Changed, Deprecated, Removed, Fixed, Security

**Example**:
```markdown
## [Unreleased]

## [1.0.0] - 2025-11-05
### Added
- Initial release
```

---

#### `LICENSE`
**Purpose**: Legal license for the project
**Audience**: Users, legal teams
**Default**: MIT License
**Customization**: Update copyright holder and year

---

#### `.gitignore`
**Purpose**: Specify intentionally untracked files
**Audience**: Git, developers
**Content**:
- Python artifacts (__pycache__, *.pyc, etc.)
- Virtual environments (.venv/, venv/)
- IDE files (.vscode/, .idea/)
- Build artifacts (dist/, build/)
- Test artifacts (.pytest_cache/, .coverage)
- OS files (.DS_Store, Thumbs.db)

**Note**: This is created from `public.gitignore` during export

---

#### `.python-version`
**Purpose**: Specify Python version for version managers
**Audience**: pyenv, asdf, developers
**Content**: Single line with Python version (e.g., `3.9`)
**Usage**: `pyenv install && pyenv local`

---

#### `allowlist.txt`
**Purpose**: Define files for public repository mirroring
**Audience**: git-filter-repo, CI/CD, maintainers
**Format**: One path per line, directories end with `/`
**Policy**: Enforces company policy on AI artifacts and dotfiles

**Critical Rules**:
- Includes: src/, tests/, docs/, scripts/, config files
- Excludes: _internal/, AGENTS.md, .github/copilot-instructions.md
- Only .github/workflows/, .gitignore, .python-version allowed

---

#### `public.gitignore`
**Purpose**: Template .gitignore for public repository
**Audience**: git-filter-repo (renamed to .gitignore during export)
**Note**: Does NOT contain references to internal directories

---

### AI Agent Files (INTERNAL - Root for Discovery)

#### `AGENTS.md` 🔒
**Purpose**: Quick reference for AI agents
**Location**: Root (for automatic discovery by AI tools)
**Audience**: GitHub Copilot, Claude, Cursor, other AI agents
**Status**: ⚠️  INTERNAL ONLY - Excluded from public repo per company policy

**Content**:
- Project overview (1-2 sentences)
- Tech stack summary
- Key directories and their purposes
- Important conventions
- Common gotchas
- Where to find more context (.github/copilot-instructions.md)

**Size Limit**: <5KB (quick reference only)

**Example Structure**:
```markdown
# Project Name - AI Agent Quick Reference

## What This Project Does
[1-2 sentence description]

## Tech Stack
- Python 3.9+
- FastAPI / Django / Flask
- PostgreSQL / SQLite
- [Other major dependencies]

## Directory Guide
- src/PROJECT_NAME/ - Source code
- tests/ - Test suite
- _internal/project/ - Internal PM and context

## Key Conventions
- [Convention 1]
- [Convention 2]

## Common Gotchas
- [Gotcha 1]
- [Gotcha 2]

## More Context
See .github/copilot-instructions.md for comprehensive instructions
See _internal/project/AGENT_START_HERE.md for project-specific context
```

---

## 📁 Root Level Directories

### `_internal/` - Internal Project Management 🔒

**Purpose**: All internal-only content (PM, context, reports, internal docs)
**Visibility**: ⚠️  INTERNAL ONLY - Entire directory excluded from public repo
**Audience**: Internal team, AI agents (internal development)

**Philosophy**:
- Separates project management from deliverables
- Provides structured context for AI agents
- Enables dual-repository workflow
- Contains sensitive/internal-only information

#### `_internal/docs/` - Internal Documentation

**Purpose**: Documentation not suitable for public release
**Content Types**:
- Architecture Decision Records (ADRs)
- Internal investigations and research
- Internal setup guides
- Starter pack documentation

##### `_internal/docs/decisions/` - ADRs

**Purpose**: Architecture Decision Records
**Format**: Markdown files named `NNNN-title.md`
**Template**: Use ADR template (see below)

**Sections**:
- Status: Proposed, Accepted, Deprecated, Superseded
- Context: What is the issue we're addressing
- Decision: What we decided
- Consequences: What becomes easier/harder

**Example Naming**:
- `0001-use-fastapi-framework.md`
- `0002-postgresql-for-persistence.md`

---

##### `_internal/docs/investigations/` - Research & Spikes

**Purpose**: Technical investigation results
**Content**: Research, spike results, proof of concepts
**Format**: Markdown files with findings

**Structure**:
```markdown
# Investigation: [Topic]
**Date**: YYYY-MM-DD
**Investigator**: Name

## Question
What are we trying to learn?

## Approach
How did we investigate?

## Findings
What did we learn?

## Recommendation
What should we do?

## References
- Links
- Resources
```

---

##### `_internal/docs/setup/` - Internal Setup Guides

**Purpose**: Development environment setup (internal-specific)
**Examples**:
- VPN setup
- Internal tool configuration
- Database access setup
- API key management (internal systems)

---

##### `_internal/docs/starter-pack/` - Template Documentation

**Purpose**: Documentation about the starter pack itself
**Files**:
- `HOW_TO_USE.md` - Usage instructions for starter pack
- `MANIFEST.txt` - Complete file listing
- `STARTER_PACK_CONTENTS.md` - Detailed contents documentation

---

#### `_internal/project/` - Project Management & Agent Context

**Purpose**: Project management and AI agent collaboration
**Philosophy**: Tiered context system for efficient AI agent usage

##### `_internal/project/AGENT_START_HERE.md`

**Purpose**: Primary entry point for AI agents
**Size Limit**: <5KB (Tier 0 - always load)
**Audience**: AI agents starting work on project

**Content**:
- Project overview (what it does, why it exists)
- Current status and priorities
- Architecture summary (2-3 paragraphs)
- Key conventions and patterns
- Where to find additional context (tier 1, 2, 3)
- Common tasks quick reference

**Format**:
```markdown
# Agent Start Here - [Project Name]

## Project Overview
[What this project does - 2-3 sentences]

## Current Status
- Phase: [Alpha/Beta/Production]
- Priority: [Current sprint focus]

## Architecture at a Glance
[High-level architecture - 2-3 paragraphs]

## Key Conventions
- [Convention 1]
- [Convention 2]

## Where to Find More
- Tier 1 (Situational): _internal/project/context/situational/
- Tier 2 (Reference): _internal/project/context/reference/
- Decisions: _internal/docs/decisions/

## Common Tasks
- [Task 1]: [Quick how-to]
- [Task 2]: [Quick how-to]
```

---

##### `_internal/project/context/` - Tiered Context System

**Purpose**: Structured context for AI agents, organized by size/frequency
**Philosophy**: Load small, frequently-needed context; lookup larger reference docs

###### `_internal/project/context/essential/` - Tier 0

**Purpose**: Always-load context (<5KB per file)
**Load Strategy**: Load every time agent starts work
**Files**:

- **`checklists.md`** - Essential checklists
  - Definition of Done
  - Code review checklist
  - Pre-deployment checklist
  - Security checklist

- **`warnings.md`** - Critical warnings
  - Common pitfalls
  - Security gotchas
  - Data handling warnings
  - Performance anti-patterns

- **`quick-wins.md`** (optional) - Quick improvements
  - Low-hanging fruit
  - Common optimizations
  - Standard refactorings

**Size Guideline**: Each file <5KB

---

###### `_internal/project/context/situational/` - Tier 1

**Purpose**: Load as needed (5-20KB per file)
**Load Strategy**: Load when working on specific feature/area
**Files**:

- **`patterns.md`** - Approved patterns (summary)
  - Design patterns used
  - Code organization patterns
  - Testing patterns
  - Error handling patterns

- **`antipatterns.md`** - Anti-patterns to avoid (summary)
  - Known bad patterns
  - Why they're problematic
  - Better alternatives

- **`solutions.md`** - Common problem solutions
  - How to implement feature X
  - How to test scenario Y
  - How to debug issue Z

**Size Guideline**: 5-20KB per file, summaries with links to Tier 2

---

###### `_internal/project/context/reference/` - Tier 2

**Purpose**: Lookup only (20KB+)
**Load Strategy**: Load only when Tier 0/1 insufficient
**Files**:

- **`patterns-full.md`** - Complete pattern documentation
  - Detailed examples
  - Full code samples
  - Multiple approaches
  - Edge cases

- **`antipatterns-full.md`** - Complete anti-pattern documentation
  - Detailed explanations
  - Real-world examples
  - Migration strategies

- **`decisions-full.md`** - Aggregated ADR summaries
  - All ADRs in one place
  - Quick reference to decision log

**Size Guideline**: 20KB+ per file, comprehensive reference

---

###### `_internal/project/context/archive/` - Tier 3

**Purpose**: Historical context
**Load Strategy**: Rarely needed, lookup only when context requires
**Content**:
- Deprecated patterns
- Superseded decisions
- Historical context
- Legacy system documentation

---

##### `_internal/project/learnings/` - Knowledge Capture

**Purpose**: Capture and distill learnings from development sessions

###### `_internal/project/learnings/raw/sessions/`

**Purpose**: Individual session logs
**Format**: `YYYY-MM-DD-topic-name.md`
**Template**: See `template.md`

**Session Log Structure**:
```markdown
# Session: [Topic] - YYYY-MM-DD

## Goal
What were we trying to accomplish?

## Approach
How did we approach it?

## What Worked
- Success 1
- Success 2

## What Didn't Work
- Challenge 1
- Challenge 2

## Learnings
- Learning 1
- Learning 2

## Next Steps
- [ ] Task 1
- [ ] Task 2

## Distillation Candidates
- [ ] Pattern: [Name] → situational/patterns.md
- [ ] Gotcha: [Name] → essential/warnings.md
```

---

###### `_internal/project/learnings/distilled/`

**Purpose**: Aggregated summaries and extracted patterns
**Subdirectories**:

- **`weekly/`** - Weekly summaries (YYYY-WW format)
  - Summary of week's work
  - Key learnings
  - Patterns discovered

- **`monthly/`** - Monthly summaries (YYYY-MM format)
  - Month overview
  - Major accomplishments
  - Strategic learnings

- **`patterns/`** - Extracted patterns
  - Patterns discovered during work
  - Before promoting to context/situational/

**Distillation Process**:
1. Write session logs during work
2. Weekly: Summarize sessions → weekly/
3. Monthly: Summarize weeks → monthly/
4. Ongoing: Extract patterns → patterns/
5. Promote: Good patterns → context/situational/

---

##### `_internal/project/planning/` - Planning Documents

**Purpose**: Project planning artifacts
**Content**:
- Roadmap
- Milestones
- Sprint plans
- Project goals

---

##### `_internal/project/backlog/` - Work Backlog

**Purpose**: Work items, features, technical debt
**Format**: Markdown files or links to issue tracker
**Organization**:
- By priority
- By epic/theme
- By technical area

---

##### `_internal/project/metrics/` - Project Metrics

**Purpose**: Track project health
**Content**:
- Test coverage reports
- Performance metrics
- Code quality metrics
- Velocity tracking

---

##### `_internal/project/process/` - Team Processes

**Purpose**: How the team works
**Content**:
- Development workflow
- Code review process
- Deployment process
- Incident response

---

##### `_internal/project/onboarding/` - Team Onboarding

**Purpose**: New team member onboarding
**Content**:
- Getting started guide
- Local development setup
- Team norms
- FAQ

---

##### `_internal/project/.distillation/` - Automation Data

**Purpose**: Data for automated distillation
**Content**: JSON/YAML files tracking distillation state
**Note**: Hidden directory, used by automation scripts

---

#### `_internal/reports/` - Status Reports

**Purpose**: Point-in-time status reporting
**Content**:
- Weekly status reports
- QA reports
- Performance reviews
- Security audits

**Lifecycle**:
- Active reports in root
- Old reports → `archive/`
- `ARCHIVE_SUMMARY.md` explains why archived

---

#### `_internal/scripts/` - Internal Automation

**Purpose**: Internal-only automation scripts
**Content**:
- Development environment setup
- Internal tooling
- Report generation
- Data migration scripts

**Note**: Public utility scripts go in `/scripts/` (root)

---

### `.github/` - GitHub Configuration

**Purpose**: GitHub-specific configuration
**Mixed Visibility**: Some public, some internal

#### `.github/workflows/` - GitHub Actions

##### `.github/workflows/ci.yml` ✅ PUBLIC

**Purpose**: CI/CD pipeline for public repository
**Runs On**: Push to main/develop, pull requests
**Steps**:
1. Checkout code
2. Set up Python (matrix: 3.9-3.12)
3. Install dependencies
4. Run linting (ruff)
5. Run type checking (mypy)
6. Run tests (pytest)
7. Upload coverage (codecov)

**Customization**: Adjust Python versions, add deployment steps

---

#### `.github/copilot-instructions.md` 🔒 INTERNAL

**Purpose**: Comprehensive AI agent instructions
**Audience**: GitHub Copilot, Claude, Cursor, other AI tools
**Status**: ⚠️  INTERNAL ONLY - Excluded from public repo per company policy

**Content** (comprehensive, can be large):
- Detailed project overview
- Full architecture explanation
- All coding conventions
- Testing strategies
- Common patterns and anti-patterns
- Edge cases and gotchas
- Links to all relevant context
- Workflow guidance

**Structure**:
```markdown
# AI Agent Instructions - [Project Name]

## Project Overview
[Detailed description - multiple paragraphs OK]

## Architecture
[Comprehensive architecture documentation]

## Coding Conventions
[All conventions in detail]

## Testing Strategy
[How to write tests for this project]

## Common Patterns
[Detailed pattern documentation]

## Anti-Patterns to Avoid
[What not to do and why]

## Workflow
[How to approach different types of tasks]

## Context Navigation
- Start: AGENTS.md (quick reference)
- Next: _internal/project/AGENT_START_HERE.md
- Detailed: _internal/project/context/ (tiered system)
- Decisions: _internal/docs/decisions/
- Learnings: _internal/project/learnings/

## Common Tasks
[Detailed how-tos for common tasks]
```

**Size**: No limit (comprehensive reference)

---

### `docs/` - Public Documentation ✅

**Purpose**: User-facing documentation
**Audience**: Public users, external contributors
**Visibility**: PUBLIC

**Philosophy**:
- Stable, long-lived documentation
- User-focused (not internal PM)
- Well-organized and navigable

#### `docs/README.md`

**Purpose**: Documentation index
**Content**: Table of contents with links to all doc sections

---

#### `docs/framework/` (if applicable)

**Purpose**: Framework/methodology documentation
**Use When**: Project defines a framework or methodology
**Content**: Framework specifications, concepts, philosophy

---

#### `docs/guides/` - How-To Guides

**Purpose**: Task-oriented documentation
**Subdirectories**:

##### `docs/guides/getting-started/`
- Installation
- First steps
- Quick tutorial
- Basic examples

##### `docs/guides/user-guides/`
- Feature guides
- Use cases
- Workflows
- Best practices

##### `docs/guides/developer-guides/`
- Contributing guidelines
- Development setup (public version)
- Testing guide
- Release process

---

#### `docs/reference/` - Technical Reference

**Purpose**: Information-oriented documentation
**Subdirectories**:

##### `docs/reference/architecture/`
- System architecture (public version)
- Design principles
- Technology choices (public rationale)

##### `docs/reference/api/`
- API documentation
- Endpoint reference
- Request/response examples
- Authentication guide

##### `docs/reference/data-models/`
- Database schema (if public)
- Data structures
- Serialization formats

---

#### `docs/assets/` - Documentation Assets

**Purpose**: Images, diagrams, screenshots
**Subdirectories**:
- `diagrams/` - Architecture diagrams, flowcharts
- `screenshots/` - UI screenshots, examples
- `icons/` - Icons and logos

**Formats**: PNG, SVG (preferred), JPG

---

### `scripts/` - Public Utility Scripts ✅

**Purpose**: Utility automation for public users
**Audience**: Public users, contributors
**Language**: Python (preferred) or Bash
**Visibility**: PUBLIC

**Requirements**:
- Self-documenting (docstrings, comments)
- Error handling
- Help text (--help flag)
- Executable permissions

#### Common Scripts:

##### `scripts/setup.py`
**Purpose**: Development environment setup
**Actions**:
- Create virtual environment
- Install dependencies
- Run initial migrations (if applicable)
- Verify installation

##### `scripts/lint.py`
**Purpose**: Run linting and formatting
**Actions**:
- Run ruff check
- Run ruff format
- Exit with error code if issues found

##### `scripts/test.py`
**Purpose**: Run test suite
**Actions**:
- Run pytest with coverage
- Generate coverage report
- Support filtering (unit, integration, e2e)

##### `scripts/README.md`
**Purpose**: Document available scripts
**Content**: List all scripts with descriptions and usage

---

### `src/` - Source Code ✅

**Purpose**: Application source code
**Visibility**: PUBLIC
**Structure**: Package with modules

#### `src/PROJECT_NAME/` - Main Package

**Pattern**: Namespace package with meaningful modules

##### `src/PROJECT_NAME/__init__.py`
**Purpose**: Package initialization
**Content**:
- Package version (`__version__ = "0.1.0"`)
- Public API exports
- Package-level configuration

##### `src/PROJECT_NAME/__main__.py`
**Purpose**: CLI entry point
**Usage**: Enables `python -m PROJECT_NAME`
**Content**:
- Argument parsing
- Command routing
- Main entry point

**Example**:
```python
def main():
    """CLI entry point."""
    # Parse arguments
    # Route to appropriate function
    # Handle errors

if __name__ == "__main__":
    main()
```

---

##### `src/PROJECT_NAME/core/`
**Purpose**: Core business logic
**Content**: Domain models, business rules, core algorithms
**Guidelines**:
- Framework-agnostic
- Well-tested
- Minimal dependencies

##### `src/PROJECT_NAME/models/`
**Purpose**: Data models
**Content**:
- Database models (if ORM)
- Pydantic models (validation)
- Data classes
- Type definitions

##### `src/PROJECT_NAME/utils/`
**Purpose**: Utility functions
**Content**: Reusable helpers, common functions
**Guidelines**:
- Pure functions when possible
- Well-documented
- Well-tested

**Common Utils**:
- String manipulation
- Date/time handling
- File I/O helpers
- Logging configuration

---

### `tests/` - Test Suite ✅

**Purpose**: Automated testing
**Visibility**: PUBLIC
**Framework**: pytest

#### `tests/conftest.py`
**Purpose**: pytest configuration and fixtures
**Content**:
- Shared fixtures
- pytest hooks
- Test configuration
- Markers definition

**Example**:
```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value"}

# Define markers
pytest_plugins = []
```

---

#### `tests/__init__.py`
**Purpose**: Mark tests as package
**Content**: Usually empty or with test helpers

---

#### `tests/unit/` - Unit Tests

**Purpose**: Test individual functions/classes in isolation
**Guidelines**:
- Fast (<1s per test)
- No external dependencies (mock/stub)
- High coverage
- Clear naming (test_function_scenario_expected)

**Example**: `tests/unit/test_utils.py`
```python
def test_format_name_with_title_case():
    """Should convert name to title case."""
    result = format_name("john doe")
    assert result == "John Doe"
```

---

#### `tests/integration/` - Integration Tests

**Purpose**: Test interactions between components
**Guidelines**:
- Test with real dependencies when possible
- May be slower than unit tests
- Mark with @pytest.mark.integration
- Use fixtures for setup/teardown

**Example**: `tests/integration/test_database.py`

---

#### `tests/e2e/` - End-to-End Tests

**Purpose**: Test complete workflows
**Guidelines**:
- Test user scenarios
- May be slow
- Mark with @pytest.mark.e2e or @pytest.mark.slow
- Use realistic data

**Example**: `tests/e2e/test_user_signup_flow.py`

---

#### `tests/fixtures/` - Test Fixtures

**Purpose**: Test data and fixtures
**Content**:
- Sample data files (JSON, CSV, etc.)
- Mock responses
- Test databases

**Organization**: By feature or data type

---

## 🎯 Usage Guidelines for AI Agents

### When Starting Work

1. **Read** `AGENTS.md` (root) - Quick 30-second orientation
2. **Read** `.github/copilot-instructions.md` - Comprehensive context
3. **Load** `_internal/project/AGENT_START_HERE.md` - Project-specific entry point
4. **Load** Tier 0 context (essential/) - Checklists and warnings
5. **Load** Tier 1 context as needed - Task-specific patterns

### During Work

1. **Reference** Tier 2 context when needed - Detailed specs
2. **Check** ADRs for architecture decisions
3. **Follow** patterns in context/
4. **Avoid** anti-patterns in context/

### After Work

1. **Log** session in `_internal/project/learnings/raw/sessions/`
2. **Note** distillation candidates
3. **Update** context if new patterns emerged

### File Discovery

- **Find** public docs: `docs/`
- **Find** internal docs: `_internal/docs/`
- **Find** context: `_internal/project/context/`
- **Find** decisions: `_internal/docs/decisions/`
- **Find** learnings: `_internal/project/learnings/`

---

## 📏 Size Guidelines Summary

| Location | Size Limit | Purpose |
|----------|-----------|---------|
| `AGENTS.md` | <5KB | Quick reference |
| `_internal/project/AGENT_START_HERE.md` | <5KB | Entry point |
| Tier 0 (essential/) | <5KB each | Always load |
| Tier 1 (situational/) | 5-20KB each | Load as needed |
| Tier 2 (reference/) | 20KB+ | Lookup only |
| Session logs | No limit | Detailed capture |

---

## ✅ Checklist for New Projects

When setting up a new project, customize these locations:

**Required**:
- [ ] `README.md` - Update description, features, usage
- [ ] `pyproject.toml` - Update name, authors, dependencies
- [ ] `LICENSE` - Update copyright holder
- [ ] `AGENTS.md` - Update project-specific info
- [ ] `.github/copilot-instructions.md` - Update comprehensive context
- [ ] `_internal/project/AGENT_START_HERE.md` - Update project context
- [ ] Rename `src/PROJECT_NAME/` to actual package name

**Recommended**:
- [ ] `_internal/project/context/essential/checklists.md` - Project-specific checklists
- [ ] `_internal/project/context/essential/warnings.md` - Project-specific gotchas
- [ ] `docs/README.md` - Update documentation index
- [ ] `.github/workflows/ci.yml` - Adjust Python versions, add deployment

---

**Version**: 1.0.0
**Last Updated**: 2025-11-05
**Maintained By**: Company Engineering Team
