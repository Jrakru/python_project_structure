# Python Project Setup Checklist

> **🔗 SST Authority Notice**
> 
> This is a **synced copy** from the canonical source in second-brain.
> 
> - **Authoritative Source**: `/home/jpw/git/second-brain/3. Resource/Python Project Structure/`
> - **This Copy**: Reference implementation in 1C4D5 project
> - **Golden Rule**: When conflicts arise, second-brain version takes precedence
> - **Updates**: Should be made in second-brain first, then synced here

**Quick Reference**: Step-by-step checklist for setting up new Python projects  
**Companion to**: [`PYTHON_PROJECT_STRUCTURE_SST.md`](./PYTHON_PROJECT_STRUCTURE_SST.md)  
**Version**: 1.0.0  
**Last Updated**: 2025-10-21  
**Status**: Synced Reference Copy

---

## 🚀 Quick Setup (5 Minutes)

### Phase 1: Project Initialization

```bash
# 1. Create project directory
mkdir my-project && cd my-project

# 2. Initialize git
git init

# 3. Create Python version file
echo "3.9" > .python-version

# 4. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
```

**Checklist**:
- [ ] Project directory created
- [ ] Git initialized
- [ ] Python version specified (`.python-version`)
- [ ] Virtual environment created and activated

---

### Phase 2: Directory Structure

```bash
# Create all directories at once
mkdir -p {src/my_package,tests/{unit,integration,e2e,fixtures},docs/{framework,guides/{getting-started,user-guides,developer-guides},reference/{architecture,api,data-models},decisions,investigations,assets/{diagrams,screenshots}},reports/archive,project/{context/{essential,situational,reference,archive},learnings/{raw/sessions,distilled/{weekly,monthly,patterns}},process,planning,backlog,metrics,.distillation,onboarding},scripts,specs,.github/{workflows,ISSUE_TEMPLATE}}
```

**Checklist**:
- [ ] `src/` - Source code directory
- [ ] `tests/` - Test suite structure
- [ ] `docs/` - Documentation hierarchy
- [ ] `reports/` - Transient reports + archive
- [ ] `project/` - AI agent collaboration system
- [ ] `scripts/` - Utility scripts
- [ ] `specs/` - Formal specifications
- [ ] `.github/` - GitHub configuration

---

### Phase 3: Essential Files

```bash
# Create core files
touch {README.md,AGENTS.md,CHANGELOG.md,LICENSE}
touch pyproject.toml .gitignore
touch src/my_package/__init__.py
touch tests/{__init__.py,conftest.py}
touch docs/README.md
touch reports/README.md
touch project/{README.md,AGENT_START_HERE.md}
touch scripts/README.md
touch .github/copilot-instructions.md
```

**Checklist**:
- [ ] `README.md` - Project overview
- [ ] `AGENTS.md` - AI agent quick reference
- [ ] `pyproject.toml` - Project configuration
- [ ] `.gitignore` - Git ignore rules
- [ ] `docs/README.md` - Documentation index
- [ ] `project/AGENT_START_HERE.md` - Agent entry point
- [ ] `.github/copilot-instructions.md` - Comprehensive agent instructions

---

### Phase 4: Configuration Files

**Create `pyproject.toml`**:
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Short description"
requires-python = ">=3.9"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[tool.ruff]
line-length = 88
target-version = "py39"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

**Create `.gitignore`**:
```gitignore
__pycache__/
*.py[cod]
.venv/
dist/
*.egg-info/
.pytest_cache/
.coverage
htmlcov/
.DS_Store
.env
*.log
```

**Checklist**:
- [ ] `pyproject.toml` configured with metadata
- [ ] Development dependencies specified
- [ ] Tool configurations added (ruff, pytest, mypy)
- [ ] `.gitignore` covers Python artifacts

---

## 📝 Documentation Setup

### Core Documentation Files

**`README.md` Template**:
```markdown
# Project Name

Brief description (1-2 sentences)

## Quick Start

```bash
# Installation
pip install my-project

# Basic usage
python -m my_package
```

## Documentation

See [docs/](./docs/) for full documentation.

## Development

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check src/ tests/
```
```

**`AGENTS.md` Template**:
```markdown
# AI Agent Guide

## Quick Start
- Read `project/AGENT_START_HERE.md` first
- Load Tier 0 context from `project/context/essential/`

## Common Commands
- Build: `python -m build`
- Test: `pytest`
- Lint: `ruff check src/`

## Key Conventions
- Test naming: `test_<what>_<condition>_<expected>()`
- Module naming: snake_case
- Class naming: PascalCase

## Critical Gotchas
1. Always activate virtual environment
2. Run tests before committing
3. Update CHANGELOG.md for user-facing changes

## Links
- Full docs: [docs/README.md](./docs/README.md)
- SST: See `.github/copilot-instructions.md`
```

**`project/AGENT_START_HERE.md` Template**:
```markdown
# Agent Start Here (<5KB)

## Project Overview
[2-3 sentence description]

## Essential Context
- **Tech Stack**: Python 3.9+, pytest, ruff
- **Architecture**: [Brief description]
- **Entry Point**: `src/my_package/__main__.py`

## Common Commands
```bash
pytest                    # Run tests
ruff check src/          # Lint
mypy src/               # Type check
```

## Top 5 Gotchas
1. [Critical gotcha #1]
2. [Critical gotcha #2]
3. [Critical gotcha #3]
4. [Critical gotcha #4]
5. [Critical gotcha #5]

## Where to Find More
- Full docs: `docs/README.md`
- Patterns: `project/context/situational/patterns.md`
- Recent work: `project/learnings/distilled/weekly/`
```

**Checklist**:
- [ ] `README.md` created with quick start
- [ ] `AGENTS.md` created with common tasks
- [ ] `project/AGENT_START_HERE.md` created (<5KB)
- [ ] `docs/README.md` created as master index

---

## 🧪 Testing Setup

**`tests/conftest.py` Template**:
```python
"""Pytest configuration and fixtures."""
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value"}
```

**Create first test** (`tests/unit/test_example.py`):
```python
"""Example unit tests."""

def test_example_passes():
    """Example test that always passes."""
    assert True

def test_example_with_fixture(sample_data):
    """Example test using a fixture."""
    assert sample_data["key"] == "value"
```

**Run initial test**:
```bash
pytest -v
```

**Checklist**:
- [ ] `tests/conftest.py` created with basic fixtures
- [ ] Example test created and passing
- [ ] pytest configuration in `pyproject.toml`
- [ ] Test directory structure complete

---

## 🤖 AI Agent Collaboration Setup

### Context Files

**Create `project/context/essential/checklists.md`**:
```markdown
# Essential Checklists (<5KB)

## Pre-Commit
- [ ] Tests pass (`pytest`)
- [ ] Lint passes (`ruff check`)
- [ ] Type check passes (`mypy src/`)

## Before Creating PR
- [ ] All tests pass with coverage
- [ ] CHANGELOG.md updated
- [ ] Documentation updated

## Adding New Feature
- [ ] Spec created in `specs/`
- [ ] Tests written first (TDD)
- [ ] Implementation complete
- [ ] Docs updated
```

**Create `project/context/essential/warnings.md`**:
```markdown
# Critical Warnings (<5KB)

## Common Pitfalls
1. **Virtual environment**: Always activate before installing packages
2. **Import paths**: Use absolute imports from package root
3. **Test isolation**: Don't share mutable state between tests
4. **Type hints**: Required for all public functions

## Anti-Patterns to Avoid
- ❌ Hardcoding file paths
- ❌ Using `print()` for logging (use `logging` module)
- ❌ Catching generic `Exception` without re-raising
- ❌ Modifying mutable default arguments
```

**Create `project/learnings/raw/sessions/template.md`**:
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
- Important decisions made

## Learnings
### What Worked
- Effective patterns

### What Didn't Work
- Anti-patterns to avoid

### Gaps in Context
- Missing context that would have helped

## Artifacts Created
- Files created/modified

## Next Steps
- What should happen next

## Links
- Related docs, PRs, issues
```

**Checklist**:
- [ ] Essential context created (checklists, warnings)
- [ ] Session log template created
- [ ] Context tiers documented
- [ ] Distillation automation planned

---

## 🛠️ Scripts Setup

**Create `scripts/setup.py`**:
```python
#!/usr/bin/env python3
"""Setup development environment."""
import subprocess
import sys

def main():
    """Setup development environment."""
    print("Setting up development environment...")
    
    # Install dependencies
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".[dev]"])
    
    print("✓ Development environment ready!")

if __name__ == "__main__":
    main()
```

**Create `scripts/lint.py`**:
```python
#!/usr/bin/env python3
"""Run linting checks."""
import subprocess
import sys

def main():
    """Run all linting checks."""
    print("Running ruff...")
    result = subprocess.run(["ruff", "check", "src/", "tests/"])
    
    if result.returncode != 0:
        sys.exit(1)
    
    print("✓ Linting passed!")

if __name__ == "__main__":
    main()
```

**Make scripts executable**:
```bash
chmod +x scripts/*.py
```

**Checklist**:
- [ ] `scripts/setup.py` created
- [ ] `scripts/lint.py` created
- [ ] `scripts/test.py` created (optional)
- [ ] Scripts are executable
- [ ] `scripts/README.md` documents all scripts

---

## 🔄 CI/CD Setup

**Create `.github/workflows/ci.yml`**:
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -e ".[dev]"
      - name: Lint
        run: ruff check src/ tests/
      - name: Type check
        run: mypy src/
      - name: Test
        run: pytest --cov=src --cov-report=xml
```

**Checklist**:
- [ ] CI workflow created (`.github/workflows/ci.yml`)
- [ ] Lint step configured
- [ ] Type check step configured
- [ ] Test step with coverage configured

---

## ✅ Final Validation

### Verify Structure
```bash
# Check directory structure exists
ls -la {src,tests,docs,reports,project,scripts,specs}

# Check essential files exist
ls -la README.md AGENTS.md pyproject.toml .gitignore
```

### Verify Installation
```bash
# Install in development mode
pip install -e ".[dev]"

# Verify installation
python -c "import my_package; print('✓ Package imports successfully')"
```

### Verify Quality Gates
```bash
# Run linting
ruff check src/ tests/

# Run type checking
mypy src/

# Run tests
pytest -v

# Check coverage
pytest --cov=src --cov-report=term
```

**Final Checklist**:
- [ ] All directories created
- [ ] All essential files present
- [ ] Package installs successfully
- [ ] Tests run and pass
- [ ] Linting passes
- [ ] Type checking passes
- [ ] CI pipeline configured
- [ ] Documentation index complete
- [ ] Agent context files created
- [ ] Git repository initialized and first commit made

---

## 🎯 Next Steps

After completing this checklist:

1. **Commit Initial Structure**:
   ```bash
   git add .
   git commit -m "Initial project structure"
   ```

2. **Set Up Remote** (optional):
   ```bash
   git remote add origin <repository-url>
   git push -u origin main
   ```

3. **Create First Feature**:
   - Create spec in `specs/001-first-feature/`
   - Write tests in `tests/unit/`
   - Implement in `src/`
   - Update documentation

4. **Start Session Logging**:
   - Use `project/learnings/raw/sessions/template.md`
   - Document significant work sessions

5. **Schedule Distillation**:
   - Set up weekly distillation automation
   - Review and update context files

---

## 📚 Reference Documents

### SST Location
- **Canonical SST**: `/home/jpw/git/second-brain/3. Resource/Python Project Structure/`
- **This Copy**: Synced reference in 1C4D5 project
- **Full SST**: [`PYTHON_PROJECT_STRUCTURE_SST.md`](./PYTHON_PROJECT_STRUCTURE_SST.md)

### Related Docs
- **1C4D5 Example**: See root project structure for reference implementation
- **AGENTS.md**: For AI agent workflows and conventions
- **docs/README.md**: For documentation organization patterns

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-21  
**Status**: Synced Reference Copy  
**Canonical Source**: `/home/jpw/git/second-brain/3. Resource/Python Project Structure/`  
**Maintained By**: Project maintainers