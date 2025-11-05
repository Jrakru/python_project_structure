#!/bin/bash
# Script to create all template files for starter pack

PACK_DIR="/home/jpw/git/second-brain/3. Resource/Python Project Structure/starter_pack"
cd "$PACK_DIR"

# Create README.md
cat > README.md << 'EOF'
# PROJECT_DISPLAY_NAME

Brief description of your project (1-2 sentences).

[![CI](https://github.com/USERNAME/PROJECT_NAME/workflows/CI/badge.svg)](https://github.com/USERNAME/PROJECT_NAME/actions)
[![Coverage](https://codecov.io/gh/USERNAME/PROJECT_NAME/branch/main/graph/badge.svg)](https://codecov.io/gh/USERNAME/PROJECT_NAME)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Features

- ✨ Feature 1
- 🚀 Feature 2
- 📦 Feature 3

## Quick Start

### Installation

```bash
pip install PROJECT_NAME
```

### Basic Usage

```python
import PROJECT_NAME

# Your example here
```

## Documentation

See [docs/](./docs/) for full documentation.

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/USERNAME/PROJECT_NAME.git
cd PROJECT_NAME

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Lint

```bash
ruff check src/ tests/
```

### Type Check

```bash
mypy src/
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) for details.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.
EOF

# Create AGENTS.md
cat > AGENTS.md << 'EOF'
# AI Agent Guide for PROJECT_DISPLAY_NAME

**Purpose**: Quick reference for AI agents working on this project  
**Last Updated**: 2025-10-21

---

## 🎯 Quick Start

### What is This Project?

PROJECT_DISPLAY_NAME is [brief description].

**Tech Stack**: Python 3.9+, pytest, ruff, mypy

---

## 📂 Project Structure

```
PROJECT_NAME/
├── src/PROJECT_NAME/     # Source code
├── tests/                # Test suite
├── docs/                 # Documentation
├── reports/              # Transient status reports
├── project/              # AI agent collaboration
└── scripts/              # Utility automation
```

---

## ⚡ Common Commands

```bash
# Run tests
pytest                    # All tests
pytest tests/unit/        # Unit tests only
pytest -v                 # Verbose output
pytest --cov=src          # With coverage

# Lint and format
ruff check src/ tests/    # Check code
ruff check --fix src/     # Auto-fix issues
ruff format src/ tests/   # Format code

# Type checking
mypy src/                 # Type check source

# Run application
python -m PROJECT_NAME    # If CLI entry point exists
```

---

## 🎯 Key Conventions

### Code Style
- Line length: 88 characters
- Test naming: `test_<what>_<condition>_<expected>()`
- Module naming: snake_case
- Class naming: PascalCase
- Function naming: snake_case

### Testing
- Write tests FIRST (TDD approach)
- 100% coverage goal for core modules
- Use fixtures for reusable test data
- Keep tests fast and isolated

### Documentation
- Update docs/ when adding features
- Create ADRs for architectural decisions
- Keep CHANGELOG.md updated

---

## 🚨 Critical Gotchas

1. **Virtual Environment**: Always activate before installing packages
2. **Import Paths**: Use absolute imports from package root
3. **Test Isolation**: Don't share mutable state between tests
4. **Type Hints**: Required for all public functions

---

## 📖 Common Tasks

### Adding a New Feature

1. Create spec in `specs/`
2. Write tests in `tests/unit/`
3. Implement in `src/PROJECT_NAME/`
4. Update `docs/`
5. Update `CHANGELOG.md`

### Fixing a Bug

1. Write failing test that reproduces bug
2. Fix the bug
3. Verify test passes
4. Update `CHANGELOG.md`

### Adding Documentation

1. Determine category (guide/reference/decision)
2. Create file in appropriate `docs/` subfolder
3. Update `docs/README.md` index
4. Cross-reference related docs

---

## 🔗 Key Files

- **Full instructions**: `.github/copilot-instructions.md`
- **Agent entry point**: `project/AGENT_START_HERE.md`
- **Documentation index**: `docs/README.md`
- **Quality report**: `reports/QA_REPORT.md` (if exists)

---

## 💡 Pro Tips

- Read `project/AGENT_START_HERE.md` first (<5KB)
- Check `project/context/essential/` for critical warnings
- Use `scripts/` for common automations
- Create session logs after significant work

---

**For comprehensive instructions, see**: `.github/copilot-instructions.md`
EOF

# Create pyproject.toml
cat > pyproject.toml << 'EOF'
[project]
name = "PROJECT_NAME"
version = "0.1.0"
description = "Short description of your project"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["keyword1", "keyword2"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]

[project.urls]
Homepage = "https://github.com/USERNAME/PROJECT_NAME"
Documentation = "https://github.com/USERNAME/PROJECT_NAME/blob/main/docs/README.md"
Repository = "https://github.com/USERNAME/PROJECT_NAME"
Issues = "https://github.com/USERNAME/PROJECT_NAME/issues"

[project.scripts]
PROJECT_NAME = "PROJECT_NAME.__main__:main"

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

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
"tests/**/*.py" = ["B008"]  # function calls in test arguments

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
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
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
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
]
fail_under = 80
EOF

# Create .gitignore
cat > .gitignore << 'EOF'
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

# Project-specific
.env
.env.local
*.log
*.db
*.sqlite

# Documentation
docs/_build/
docs/.doctrees/

# Jupyter
.ipynb_checkpoints/
*.ipynb

# OS
Thumbs.db
EOF

# Create .python-version
echo "3.9" > .python-version

# Create CHANGELOG.md
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure from Python Project Structure SST starter pack

## [0.1.0] - 2025-10-21

### Added
- Initial release
- Basic project structure

[Unreleased]: https://github.com/USERNAME/PROJECT_NAME/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/USERNAME/PROJECT_NAME/releases/tag/v0.1.0
EOF

# Create LICENSE (MIT)
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

echo "✅ Root files created"
