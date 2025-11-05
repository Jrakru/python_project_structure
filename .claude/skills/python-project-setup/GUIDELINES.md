# Company Python Development Guidelines

**Version**: 1.0.0
**Last Updated**: 2025-11-05
**Status**: Active

These guidelines govern all Python projects at our company. AI agents and developers must follow these standards.

---

## 🐍 Python Environment Management

### Python Version
- **Minimum**: Python 3.9
- **Recommended**: Python 3.11 or 3.12
- **Specify in**: `.python-version` file at project root

### Virtual Environment Management

#### Use Poetry (Preferred)
**Why**: Deterministic builds, better dependency resolution, modern tooling

```bash
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Create project
poetry new my-project
# or
poetry init

# Install dependencies
poetry install

# Add dependencies
poetry add requests
poetry add --group dev pytest ruff mypy
```

**Configuration** (`pyproject.toml`):
```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@company.com>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
ruff = "^0.1.0"
mypy = "^1.5.0"
```

#### Virtual Environment Location
- **Always use local `.venv`** in project root
- **Why**: Easier to find, IDE integration, consistent location

```bash
# Configure poetry to create .venv in project
poetry config virtualenvs.in-project true

# Verify
poetry config virtualenvs.in-project  # Should show: true
```

#### Alternative: Standard venv (If not using Poetry)
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

pip install -e ".[dev]"
```

---

## 📦 Dependency Management

### Use Pydantic v2 (Required)
**Why**: Better performance, improved validation, modern API

```bash
# Install Pydantic v2
poetry add "pydantic>=2.0"

# or with pip
pip install "pydantic>=2.0"
```

**Migration from v1**:
```python
# v1 (deprecated)
from pydantic import BaseModel, validator

class User(BaseModel):
    name: str

    @validator('name')
    def validate_name(cls, v):
        return v.strip()

# v2 (use this)
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        return v.strip()
```

**Resources**:
- Migration Guide: https://docs.pydantic.dev/latest/migration/
- V2 Documentation: https://docs.pydantic.dev/latest/

### Dependency Pinning
- **Development**: Use exact versions in lock file
- **Library**: Use compatible ranges (^, ~)
- **Application**: Lock all dependencies

**Example** (pyproject.toml):
```toml
[tool.poetry.dependencies]
# Libraries: Use ranges
pydantic = "^2.0"
httpx = "^0.25.0"

# Applications: Can use exact or ranges
# (poetry.lock handles exact versions)
```

---

## 🔧 Tooling Standards

### Linting & Formatting: Ruff (Required)
**Why**: Fast, comprehensive, replaces multiple tools

```toml
[tool.ruff]
target-version = "py39"
line-length = 88

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = []

[tool.ruff.lint.isort]
known-first-party = ["your_package"]
```

**Commands**:
```bash
# Check
ruff check src/

# Format
ruff format src/

# Fix auto-fixable issues
ruff check --fix src/
```

### Type Checking: Mypy (Required)
**Why**: Catch type errors, better IDE support, self-documenting

```toml
[tool.mypy]
python_version = "3.9"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
exclude = ["tests/"]
```

**Commands**:
```bash
mypy src/
```

### Testing: Pytest (Required)
**Why**: Industry standard, great plugins, fixtures

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]

[tool.coverage.run]
source = ["src"]
omit = ["tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
]
```

**Commands**:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific markers
pytest -m "not slow"
pytest -m integration
```

---

## 📁 Project Structure Standards

### Required Directories
- `src/` - Source code (never at root)
- `tests/` - Test suite (mirrors src/ structure)
- `docs/` - Public documentation
- `_internal/` - Internal PM and context (excluded from public)
- `scripts/` - Utility automation

### Forbidden Patterns
❌ Source code at root level
❌ Tests in src/
❌ Mixing internal and public content
❌ AI artifacts in public repo

✅ Use `src/` layout
✅ Separate tests/ directory
✅ Use `_internal/` for all internal content
✅ Follow company structure template

---

## 🤖 AI Agent Standards

### Required Files

#### `AGENTS.md` (Root)
- **Location**: Project root
- **Size**: <5KB
- **Purpose**: Quick reference for AI agents
- **Visibility**: Internal only (excluded from public)
- **Content**: Project overview, tech stack, conventions, gotchas

#### `.github/copilot-instructions.md`
- **Location**: `.github/` directory
- **Size**: No limit
- **Purpose**: Comprehensive AI agent instructions
- **Visibility**: Internal only (excluded from public)
- **Content**: Detailed architecture, patterns, workflows

#### `_internal/project/AGENT_START_HERE.md`
- **Location**: `_internal/project/`
- **Size**: <5KB
- **Purpose**: Project-specific agent entry point
- **Visibility**: Internal only
- **Content**: Current status, priorities, architecture summary

#### `_internal/CONSTITUTION.md`
- **Location**: `_internal/`
- **Size**: <10KB
- **Purpose**: Project governance and principles
- **Visibility**: Internal only
- **Content**: Rules, principles, constraints (see template)

### Context Tier System (Required)
- **Tier 0** (essential): <5KB each, always load
- **Tier 1** (situational): 5-20KB, load as needed
- **Tier 2** (reference): 20KB+, lookup only
- **Tier 3** (archive): Historical, rarely needed

---

## 🔐 Security Standards

### Secrets Management
- **Never commit secrets** to git
- Use `.env` files (in .gitignore)
- Use environment variables for production
- Use company secrets manager (Vault, AWS Secrets Manager, etc.)

### `.env` Pattern
```python
# Use python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
```

### Dependency Security
```bash
# Audit dependencies
poetry audit

# or with pip
pip-audit
```

---

## 📝 Documentation Standards

### README.md (Required)
Sections:
1. Project description
2. Features
3. Installation
4. Quick start
5. Documentation link
6. Contributing
7. License

### Docstrings (Required)
Use Google style:

```python
def process_data(data: list[dict]) -> pd.DataFrame:
    """Process raw data into DataFrame.

    Args:
        data: List of dictionaries containing raw data.

    Returns:
        Processed DataFrame with cleaned data.

    Raises:
        ValueError: If data is empty or malformed.

    Examples:
        >>> data = [{"name": "Alice", "age": 30}]
        >>> df = process_data(data)
        >>> print(df)
           name  age
        0  Alice   30
    """
    if not data:
        raise ValueError("Data cannot be empty")
    return pd.DataFrame(data)
```

### Type Hints (Required)
- All function signatures
- All class attributes
- Use `typing` module for complex types

```python
from typing import Optional, Union
from collections.abc import Sequence

def fetch_users(
    limit: int = 10,
    active_only: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Fetch users from API."""
    ...
```

---

## 🧪 Testing Standards

### Coverage Requirements
- **Minimum**: 80% coverage
- **Target**: 90%+ coverage
- **Exclude**: `__main__.py`, test files themselves

### Test Structure
```
tests/
├── unit/           # Fast, isolated tests
├── integration/    # Tests with dependencies
├── e2e/            # End-to-end tests
├── fixtures/       # Test data
└── conftest.py     # Shared fixtures
```

### Naming Convention
```python
def test_function_scenario_expected():
    """Test should read like a sentence."""
    ...

# Examples:
def test_user_creation_with_valid_data_succeeds():
def test_api_request_with_timeout_raises_error():
def test_data_processing_with_empty_input_returns_empty():
```

---

## 📊 Code Quality Standards

### Line Length
- **Maximum**: 88 characters (Ruff/Black default)
- **Docstrings**: 72 characters

### Import Organization
```python
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import httpx
import pandas as pd
from pydantic import BaseModel

# Local
from my_package import models
from my_package.utils import helpers
```

### Complexity Limits
- **Cyclomatic Complexity**: Max 10 per function
- **Function Length**: Max 50 lines
- **Class Length**: Max 300 lines

---

## 🚀 CI/CD Standards

### Required Checks
1. Linting (ruff)
2. Type checking (mypy)
3. Tests (pytest)
4. Coverage (>80%)

### GitHub Actions Template
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install poetry
        run: pipx install poetry

      - name: Install dependencies
        run: poetry install

      - name: Run linting
        run: poetry run ruff check src/

      - name: Run type checking
        run: poetry run mypy src/

      - name: Run tests
        run: poetry run pytest --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## 🔄 Version Control Standards

### Branch Naming
- `main` or `master` - Production
- `develop` - Development
- `feature/description` - New features
- `fix/description` - Bug fixes
- `refactor/description` - Refactoring

### Commit Messages
Format: `type: description`

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Tests
- `chore:` - Maintenance

Example:
```
feat: add user authentication endpoint
fix: resolve database connection timeout
docs: update API documentation
```

---

## 📋 Checklist for New Projects

### Initial Setup
- [ ] Use Poetry for dependency management
- [ ] Create local `.venv` in project
- [ ] Use Python 3.9+ (specify in `.python-version`)
- [ ] Use Pydantic v2 for validation
- [ ] Configure Ruff for linting/formatting
- [ ] Configure Mypy for type checking
- [ ] Configure Pytest with coverage
- [ ] Set up pre-commit hooks

### Structure
- [ ] Use `src/` layout
- [ ] Create `_internal/` for internal content
- [ ] Add `AGENTS.md` at root
- [ ] Add `.github/copilot-instructions.md`
- [ ] Add `_internal/CONSTITUTION.md`
- [ ] Add `_internal/project/AGENT_START_HERE.md`
- [ ] Configure `allowlist.txt` per company policy

### Documentation
- [ ] Complete README.md
- [ ] Add docstrings to all functions
- [ ] Add type hints to all functions
- [ ] Set up docs/ structure

### CI/CD
- [ ] Configure GitHub Actions
- [ ] Enable branch protection
- [ ] Require status checks
- [ ] Require code review

---

## 🔗 Resources

### Official Documentation
- Python: https://docs.python.org/3/
- Poetry: https://python-poetry.org/docs/
- Pydantic v2: https://docs.pydantic.dev/latest/
- Ruff: https://docs.astral.sh/ruff/
- Mypy: https://mypy.readthedocs.io/
- Pytest: https://docs.pytest.org/

### Company Resources
- Project Template: `.claude/skills/python-project-setup/template/`
- Structure Reference: `.claude/skills/python-project-setup/STRUCTURE_REFERENCE.md`
- File Guide: `.claude/skills/python-project-setup/FILE_GUIDE.md`

---

## 📝 Updates and Changes

### How to Update Guidelines
1. Propose change via PR
2. Get team review
3. Update version number
4. Announce to team
5. Update project templates

### Version History
- **1.0.0** (2025-11-05): Initial guidelines

---

**Questions?** Contact the engineering team or create an issue in the project template repository.
