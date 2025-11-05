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
