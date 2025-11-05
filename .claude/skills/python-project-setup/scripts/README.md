# Skill Automation Scripts

These scripts automate common tasks for Python project setup and maintenance.

---

## 📜 Available Scripts

### `setup_project.py`
**Purpose**: Interactive project scaffolding from template

**Usage**:
```bash
python scripts/setup_project.py
# or
./scripts/setup_project.py
```

**Features**:
- Interactive prompts for project configuration
- Validates inputs (package names, Python versions)
- Copies and customizes template
- Replaces all placeholders (PROJECT_NAME, etc.)
- Optionally initializes Git repository
- Optionally sets up virtual environment (Poetry or venv)
- Optionally runs initial tests
- Provides next steps guidance

**Configuration Prompts**:
- Package name (validates Python naming rules)
- Display name (human-readable)
- Author name and email
- GitHub username
- Python version (validates format)
- Target directory
- Use Poetry? (yes/no)
- Initialize Git? (yes/no)
- Set up virtual environment? (yes/no)
- Run initial tests? (yes/no)

**Example**:
```bash
$ python scripts/setup_project.py

Python Project Setup

Project Configuration
Package name (lowercase, underscores OK) [my_package]: my_api
Display name (human-readable) [My Api]: My API
Author name [Your Name]: John Doe
Author email [you@company.com]: john@company.com
GitHub username [your-username]: johndoe
Python version [3.9]: 3.11
Target directory [/home/user/my_api]: /home/user/projects/my_api
Initialize Git repository? [Y/n]: y
Use Poetry for environment management? [Y/n]: y
Set up virtual environment now? [Y/n]: y
Run initial tests? [Y/n]: y

Configuration Summary
Package name:     my_api
Display name:     My API
Author:           John Doe <john@company.com>
GitHub username:  johndoe
Python version:   3.11
Target directory: /home/user/projects/my_api
Use Poetry:       Yes

Proceed with setup? [Y/n]: y

✓ Template copied to /home/user/projects/my_api
✓ Project customization complete
✓ Git repository initialized
✓ Poetry environment created and dependencies installed
✓ All tests passed!

Setup Complete! 🎉
```

---

### `show_structure.py`
**Purpose**: Display information about project files and directories

**Usage**:
```bash
# Show quick reference table
python scripts/show_structure.py

# Show info about specific file/directory
python scripts/show_structure.py pyproject.toml
python scripts/show_structure.py _internal/project/

# List all directories
python scripts/show_structure.py --list-dirs

# List all files
python scripts/show_structure.py --list-files

# Show full details
python scripts/show_structure.py _internal/ --full
```

**Features**:
- Parses STRUCTURE_REFERENCE.md and FILE_GUIDE.md
- Shows purpose, audience, content guidelines for directories
- Shows purpose, visibility, must-edit status for files
- Quick reference table for common items
- Fuzzy search support
- Color-coded output

**Examples**:
```bash
# What does _internal/project/ do?
$ python scripts/show_structure.py _internal/project/

Directory: _internal/project/

Purpose:
  Project management and AI agent collaboration

Audience:
  Internal team, AI agents (internal development)

# What are all the required directories?
$ python scripts/show_structure.py --list-dirs

All Directories:

  _internal/                               Internal project management content
  _internal/docs/                          Documentation not suitable for public
  _internal/docs/decisions/                Architecture Decision Records
  ...

# Quick reference for common files
$ python scripts/show_structure.py --quick-ref

Quick Reference:

  Project config                  → pyproject.toml
  Quick agent ref                 → AGENTS.md
  Detailed agent instructions     → .github/copilot-instructions.md
  ...
```

---

### `validate_structure.py`
**Purpose**: Validate project structure against company standards

**Usage**:
```bash
# Validate current directory
python scripts/validate_structure.py

# Validate specific directory
python scripts/validate_structure.py /path/to/project

# Strict mode (treat warnings as errors)
python scripts/validate_structure.py --strict
```

**Features**:
- Checks for required files and directories
- Validates src/ layout (package structure)
- Validates tests/ structure
- Validates _internal/ structure
- Validates AI agent files
- Validates pyproject.toml configuration
- Validates .gitignore patterns
- Checks for unreplaced placeholders
- Validates GitHub CI configuration
- Checks company guideline compliance
- Color-coded report (errors, warnings, passed)

**Validation Checks**:
1. **Required Files**: README.md, pyproject.toml, LICENSE, etc.
2. **Required Directories**: src/, tests/, docs/, _internal/, etc.
3. **Src Layout**: Package has __init__.py
4. **Test Structure**: conftest.py, unit/, integration/, e2e/
5. **Internal Structure**: Required subdirectories and files
6. **Agent Files**: AGENTS.md, copilot-instructions.md, AGENT_START_HERE.md
7. **pyproject.toml**: Required sections ([project], [tool.ruff], etc.)
8. **Pydantic v2**: Checks for Pydantic ^2.0
9. **.gitignore**: Common patterns (__pycache__, .venv, etc.)
10. **Placeholders**: Checks for unreplaced template variables
11. **GitHub CI**: Workflow exists with ruff, mypy, pytest
12. **Company Guidelines**: Local .venv, Python 3.9+

**Example Output**:
```bash
$ python scripts/validate_structure.py

Validating project: /home/user/my_project

Validation Report
============================================================

✓ Passed (25):
  ✓ Required file exists: README.md
  ✓ Required file exists: pyproject.toml
  ✓ Required directory exists: src/
  ✓ Package my_api has __init__.py
  ✓ uses Pydantic v2
  ...

⚠ Warnings (3):
  ⚠ tests/conftest.py not found (recommended)
  ⚠ Test directory not found: tests/e2e/ (recommended)
  ⚠ No local .venv found (company guideline recommends local .venv)

✗ Errors (0):

============================================================
PASSED with warnings: 3 warning(s)
```

---

## 🔧 Script Dependencies

All scripts are standalone Python 3.9+ scripts with no external dependencies. They only use Python standard library:

- `pathlib` - Path handling
- `argparse` - CLI argument parsing
- `re` - Regular expressions
- `shutil` - File operations
- `subprocess` - Running external commands

---

## 🎯 Workflow Examples

### New Project Setup

```bash
# 1. Run interactive setup
python scripts/setup_project.py

# 2. Validate structure
python scripts/validate_structure.py /path/to/new/project

# 3. Check specific files if needed
python scripts/show_structure.py pyproject.toml
```

### Learning the Structure

```bash
# 1. See quick reference
python scripts/show_structure.py --quick-ref

# 2. List all directories
python scripts/show_structure.py --list-dirs

# 3. Get details on specific items
python scripts/show_structure.py _internal/
python scripts/show_structure.py AGENTS.md --full
```

### Project Maintenance

```bash
# 1. Validate after changes
python scripts/validate_structure.py

# 2. Strict validation (for CI)
python scripts/validate_structure.py --strict

# 3. Check what a file/folder should contain
python scripts/show_structure.py tests/
```

---

## 📋 Adding New Scripts

If you create additional useful scripts:

1. Add to this directory (`.claude/skills/python-project-setup/scripts/`)
2. Make executable: `chmod +x script_name.py`
3. Add shebang: `#!/usr/bin/env python3`
4. Document in this README
5. Follow naming convention: `verb_noun.py`

---

## 🤝 Contributing

Suggestions for new scripts:
- `update_from_template.py` - Sync existing project with template updates
- `generate_docs.py` - Generate documentation from code
- `check_coverage.py` - Coverage report and enforcement
- `profile_imports.py` - Check import times
- `audit_dependencies.py` - Security audit of dependencies

---

**Questions?** See main skill documentation or create an issue.
