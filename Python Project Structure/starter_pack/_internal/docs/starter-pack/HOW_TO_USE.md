# Python Project Starter Pack - How to Use

**Purpose**: Ready-to-copy template for new Python projects  
**Version**: 1.0.0  
**Last Updated**: 2025-10-21

---

## 🚀 Quick Start (2 Minutes)

### Step 1: Copy the Starter Pack

```bash
# Copy entire starter_pack to your new project location
cp -r "/path/to/second-brain/3. Resource/Python Project Structure/starter_pack" /path/to/my-new-project

cd /path/to/my-new-project
```

### Step 2: Customize Project Name

```bash
# Replace PROJECT_NAME with your actual project name (use snake_case)
PROJECT_NAME="my_project"

# Rename the package directory
mv src/PROJECT_NAME "src/${PROJECT_NAME}"

# Replace PROJECT_NAME in all template files
find . -type f -name "*.md" -o -name "*.toml" -o -name "*.py" | xargs sed -i "s/PROJECT_NAME/${PROJECT_NAME}/g"

# Replace PROJECT_DISPLAY_NAME with your project display name
PROJECT_DISPLAY="My Project"
find . -type f -name "*.md" | xargs sed -i "s/PROJECT_DISPLAY_NAME/${PROJECT_DISPLAY}/g"
```

### Step 3: Initialize Git

```bash
git init
git add .
git commit -m "Initial project structure from starter pack"
```

### Step 4: Set Up Virtual Environment

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e ".[dev]"
```

### Step 5: Verify Setup

```bash
# Run tests
pytest -v

# Run linting
ruff check src/ tests/

# Run type checking
mypy src/
```

**Done!** Your project is ready to go. 🎉

---

## 📋 What's Included

### Root Files
- `README.md` - Project overview (customize with your project details)
- `AGENTS.md` - AI agent quick reference
- `pyproject.toml` - Project configuration (customize name, description, dependencies)
- `.gitignore` - Python-specific ignore patterns
- `.python-version` - Python version specification
- `CHANGELOG.md` - Version history tracker
- `LICENSE` - License file (MIT template, customize as needed)

### Source Code (`src/PROJECT_NAME/`)
- `__init__.py` - Package initialization with version
- `__main__.py` - CLI entry point template
- `core/` - Core business logic placeholder
- `models/` - Data models placeholder
- `utils/` - Utilities placeholder

### Tests (`tests/`)
- `conftest.py` - Pytest configuration with fixtures
- `unit/test_example.py` - Example unit test
- `integration/` - Integration tests folder
- `e2e/` - End-to-end tests folder
- `fixtures/` - Test data and fixtures

### Documentation (`docs/`)
- `README.md` - Documentation index
- `framework/` - Methodology/framework docs
- `guides/` - How-to guides and tutorials
- `reference/` - Technical references
- `decisions/` - Architecture Decision Records (ADRs)
- `investigations/` - Research and analysis

### Reports (`reports/`)
- `README.md` - Reports index with archival policy
- `archive/` - Completed/historical reports

### Project Management (`project/`)
- `AGENT_START_HERE.md` - AI agent entry point (<5KB)
- `README.md` - Project management overview
- `context/` - Tiered context files (essential/situational/reference/archive)
- `learnings/` - Session logs and distilled summaries
- `process/` - Team processes and workflows
- `planning/` - Roadmap and milestones
- `backlog/` - Work items

### Scripts (`scripts/`)
- `README.md` - Scripts documentation
- `setup.py` - Development environment setup
- `lint.py` - Linting automation
- `test.py` - Test automation

### GitHub (`,.github/`)
- `workflows/ci.yml` - CI/CD pipeline
- `copilot-instructions.md` - Comprehensive AI agent instructions

---

## 🔧 Customization Guide

### 1. Update Project Metadata

**In `pyproject.toml`**:
```toml
[project]
name = "your-project-name"
version = "0.1.0"
description = "Your project description"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
```

### 2. Add Your Dependencies

**In `pyproject.toml`**:
```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
    # Add your dependencies here
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
    # Add dev dependencies here
]
```

### 3. Customize README.md

- Update project name and description
- Add your specific installation instructions
- Add usage examples
- Update feature list
- Add your badges (build status, coverage, etc.)

### 4. Update License

- Review `LICENSE` file
- Change to your preferred license if needed
- Update copyright year and name

### 5. Configure Tools

**Adjust in `pyproject.toml` if needed**:
- Line length (default: 88)
- Python version (default: 3.9+)
- Test markers
- Coverage thresholds

### 6. Add Your Code

- Implement your logic in `src/PROJECT_NAME/`
- Write tests in `tests/`
- Update documentation in `docs/`
- Create ADRs for major decisions in `docs/decisions/`

---

## 📝 File-by-File Customization Checklist

### Must Customize
- [ ] `README.md` - Project name, description, features
- [ ] `pyproject.toml` - Name, version, description, author, dependencies
- [ ] `LICENSE` - Copyright holder and year
- [ ] `src/PROJECT_NAME/` - Rename to your package name
- [ ] `CHANGELOG.md` - Update with your version history
- [ ] `.python-version` - Set your Python version

### Should Customize
- [ ] `AGENTS.md` - Add project-specific gotchas and commands
- [ ] `project/AGENT_START_HERE.md` - Add project-specific context
- [ ] `docs/README.md` - Update with your documentation structure
- [ ] `.github/copilot-instructions.md` - Add project-specific patterns
- [ ] `scripts/` - Add project-specific automation scripts

### Optional Customization
- [ ] `project/context/essential/` - Add your critical gotchas
- [ ] `project/process/` - Add your team processes
- [ ] `docs/framework/` - Add methodology docs if applicable
- [ ] `.github/workflows/` - Customize CI/CD as needed

---

## 🎯 Next Steps After Setup

1. **Add Your First Feature**
   - Create spec in `specs/001-feature-name/`
   - Write tests in `tests/unit/`
   - Implement in `src/PROJECT_NAME/`
   - Update docs

2. **Set Up CI/CD**
   - Push to GitHub
   - Verify GitHub Actions workflow runs
   - Add branch protection rules
   - Set up required status checks

3. **Configure Pre-Commit Hooks** (Optional)
   ```bash
   pip install pre-commit
   pre-commit install
   ```

4. **Start Using Agent Context**
   - Create first session log: `project/learnings/raw/sessions/`
   - Set up weekly distillation schedule
   - Update `AGENT_START_HERE.md` with learnings

5. **Add Documentation**
   - Write getting started guide: `docs/guides/getting-started/`
   - Document architecture: `docs/reference/architecture/`
   - Create ADRs for key decisions: `docs/decisions/`

---

## 💡 Tips

### For Clean Start
```bash
# Remove example files after you've added your own
rm tests/unit/test_example.py
rm src/PROJECT_NAME/__main__.py  # if you don't need CLI
```

### For Multiple Projects
```bash
# Keep starter_pack pristine
# Make a copy for each new project
cp -r starter_pack ../my-project-1
cp -r starter_pack ../my-project-2
```

### For Quick Rename
```bash
# One-liner to rename everything
OLD="PROJECT_NAME" NEW="my_package" && find . -type f -exec sed -i "s/$OLD/$NEW/g" {} +
```

---

## 🆘 Troubleshooting

**Problem**: `pip install -e ".[dev]"` fails  
**Solution**: Ensure you're in the project root with `pyproject.toml`

**Problem**: Tests fail with import errors  
**Solution**: Check `pythonpath` in `pyproject.toml` includes `"src"`

**Problem**: Mypy can't find package  
**Solution**: Ensure package installed: `pip install -e .`

**Problem**: Ruff not finding files  
**Solution**: Check you're running from project root

---

## 📚 References

- **Full SST**: `../PYTHON_PROJECT_STRUCTURE_SST.md`
- **Checklist**: `../PYTHON_PROJECT_SETUP_CHECKLIST.md`
- **README**: `../README.md`

---

**Version**: 1.0.0  
**Maintained By**: Project maintainers  
**Last Updated**: 2025-10-21
