#!/usr/bin/env python3
"""
Validate project structure against company standards.

Checks if a project follows the required structure, naming conventions,
and company guidelines.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple

# Color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed: List[str] = []

    def add_error(self, msg: str):
        self.errors.append(msg)

    def add_warning(self, msg: str):
        self.warnings.append(msg)

    def add_pass(self, msg: str):
        self.passed.append(msg)

    def print_report(self):
        """Print validation report."""
        print(f"\n{Colors.BOLD}Validation Report{Colors.END}")
        print("=" * 60)

        if self.passed:
            print(f"\n{Colors.GREEN}✓ Passed ({len(self.passed)}):{Colors.END}")
            for msg in self.passed:
                print(f"  ✓ {msg}")

        if self.warnings:
            print(f"\n{Colors.YELLOW}⚠ Warnings ({len(self.warnings)}):{Colors.END}")
            for msg in self.warnings:
                print(f"  ⚠ {msg}")

        if self.errors:
            print(f"\n{Colors.RED}✗ Errors ({len(self.errors)}):{Colors.END}")
            for msg in self.errors:
                print(f"  ✗ {msg}")

        print("\n" + "=" * 60)

        if self.errors:
            print(f"{Colors.RED}FAILED{Colors.END}: {len(self.errors)} error(s)")
            return False
        elif self.warnings:
            print(f"{Colors.YELLOW}PASSED with warnings{Colors.END}: {len(self.warnings)} warning(s)")
            return True
        else:
            print(f"{Colors.GREEN}PASSED{Colors.END}: All checks passed!")
            return True


def validate_required_files(project_dir: Path, result: ValidationResult):
    """Check for required files."""
    required_files = [
        "README.md",
        "pyproject.toml",
        ".gitignore",
        ".python-version",
        "LICENSE",
        "CHANGELOG.md",
    ]

    for file_name in required_files:
        file_path = project_dir / file_name
        if file_path.exists():
            result.add_pass(f"Required file exists: {file_name}")
        else:
            result.add_error(f"Missing required file: {file_name}")


def validate_required_directories(project_dir: Path, result: ValidationResult):
    """Check for required directories."""
    required_dirs = [
        "src",
        "tests",
        "docs",
        "scripts",
        "_internal",
        ".github",
    ]

    for dir_name in required_dirs:
        dir_path = project_dir / dir_name
        if dir_path.exists() and dir_path.is_dir():
            result.add_pass(f"Required directory exists: {dir_name}/")
        else:
            result.add_error(f"Missing required directory: {dir_name}/")


def validate_src_layout(project_dir: Path, result: ValidationResult):
    """Validate src/ layout."""
    src_dir = project_dir / "src"

    if not src_dir.exists():
        result.add_error("src/ directory not found")
        return

    # Check that there's at least one package
    packages = [d for d in src_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

    if not packages:
        result.add_error("No package found in src/ (should have src/package_name/)")
        return

    if len(packages) > 1:
        result.add_warning(f"Multiple packages in src/: {[p.name for p in packages]}")

    # Check first package has __init__.py
    package = packages[0]
    init_file = package / "__init__.py"

    if init_file.exists():
        result.add_pass(f"Package {package.name} has __init__.py")
    else:
        result.add_error(f"Package {package.name} missing __init__.py")


def validate_test_structure(project_dir: Path, result: ValidationResult):
    """Validate tests/ structure."""
    tests_dir = project_dir / "tests"

    if not tests_dir.exists():
        result.add_error("tests/ directory not found")
        return

    # Check for conftest.py
    conftest = tests_dir / "conftest.py"
    if conftest.exists():
        result.add_pass("tests/conftest.py exists")
    else:
        result.add_warning("tests/conftest.py not found (recommended)")

    # Check for test subdirectories
    test_subdirs = ["unit", "integration", "e2e"]
    for subdir in test_subdirs:
        subdir_path = tests_dir / subdir
        if subdir_path.exists():
            result.add_pass(f"Test directory exists: tests/{subdir}/")
        else:
            result.add_warning(f"Test directory not found: tests/{subdir}/ (recommended)")


def validate_internal_structure(project_dir: Path, result: ValidationResult):
    """Validate _internal/ structure."""
    internal_dir = project_dir / "_internal"

    if not internal_dir.exists():
        result.add_error("_internal/ directory not found")
        return

    # Check required subdirectories
    required_internal_dirs = [
        "docs",
        "project",
        "reports",
    ]

    for dir_name in required_internal_dirs:
        dir_path = internal_dir / dir_name
        if dir_path.exists():
            result.add_pass(f"Internal directory exists: _internal/{dir_name}/")
        else:
            result.add_error(f"Missing internal directory: _internal/{dir_name}/")

    # Check for important files
    important_files = [
        "_internal/README.md",
        "_internal/CONSTITUTION.md",
        "_internal/project/AGENT_START_HERE.md",
        "_internal/project/context/essential/checklists.md",
        "_internal/project/context/essential/warnings.md",
    ]

    for file_path_str in important_files:
        file_path = project_dir / file_path_str
        if file_path.exists():
            result.add_pass(f"File exists: {file_path_str}")
        else:
            result.add_warning(f"File not found: {file_path_str} (recommended)")


def validate_agent_files(project_dir: Path, result: ValidationResult):
    """Validate AI agent instruction files."""
    agent_files = [
        "AGENTS.md",
        ".github/copilot-instructions.md",
    ]

    for file_path_str in agent_files:
        file_path = project_dir / file_path_str
        if file_path.exists():
            result.add_pass(f"Agent file exists: {file_path_str}")

            # Check file size (AGENTS.md should be <5KB)
            if file_path.name == "AGENTS.md":
                size_kb = file_path.stat().st_size / 1024
                if size_kb > 5:
                    result.add_warning(f"AGENTS.md is {size_kb:.1f}KB (recommended <5KB)")
        else:
            result.add_warning(f"Agent file not found: {file_path_str} (recommended)")


def validate_pyproject_toml(project_dir: Path, result: ValidationResult):
    """Validate pyproject.toml configuration."""
    pyproject_path = project_dir / "pyproject.toml"

    if not pyproject_path.exists():
        result.add_error("pyproject.toml not found")
        return

    try:
        content = pyproject_path.read_text()

        # Check for required sections
        required_sections = [
            "[project]",
            "[tool.ruff]",
            "[tool.mypy]",
            "[tool.pytest",
        ]

        for section in required_sections:
            if section in content:
                result.add_pass(f"pyproject.toml has {section}")
            else:
                result.add_warning(f"pyproject.toml missing {section} (recommended)")

        # Check for Pydantic v2
        if "pydantic" in content:
            if 'pydantic = "^2' in content or 'pydantic>=2' in content:
                result.add_pass("Uses Pydantic v2")
            else:
                result.add_warning("Pydantic version not v2 (company guideline)")

    except Exception as e:
        result.add_error(f"Error reading pyproject.toml: {e}")


def validate_gitignore(project_dir: Path, result: ValidationResult):
    """Validate .gitignore."""
    gitignore_path = project_dir / ".gitignore"

    if not gitignore_path.exists():
        result.add_error(".gitignore not found")
        return

    try:
        content = gitignore_path.read_text()

        # Check for important patterns
        important_patterns = [
            "__pycache__",
            ".venv",
            ".pytest_cache",
            ".mypy_cache",
            ".coverage",
        ]

        for pattern in important_patterns:
            if pattern in content:
                result.add_pass(f".gitignore includes {pattern}")
            else:
                result.add_warning(f".gitignore missing {pattern} (recommended)")

    except Exception as e:
        result.add_error(f"Error reading .gitignore: {e}")


def validate_placeholder_text(project_dir: Path, result: ValidationResult):
    """Check for unreplaced placeholder text."""
    placeholders = [
        "PROJECT_NAME",
        "PROJECT_DISPLAY_NAME",
        "USERNAME",
        "[fullname]",
        "[year]",
        "[DATE]",
    ]

    # Files to check
    files_to_check = [
        "README.md",
        "pyproject.toml",
        "LICENSE",
        "AGENTS.md",
    ]

    found_placeholders = []

    for file_name in files_to_check:
        file_path = project_dir / file_name
        if file_path.exists():
            try:
                content = file_path.read_text()
                for placeholder in placeholders:
                    if placeholder in content:
                        found_placeholders.append(f"{file_name}: {placeholder}")
            except Exception:
                pass

    if found_placeholders:
        result.add_warning("Found unreplaced placeholders:")
        for item in found_placeholders:
            result.add_warning(f"  - {item}")
    else:
        result.add_pass("No unreplaced placeholders found")


def validate_github_ci(project_dir: Path, result: ValidationResult):
    """Validate GitHub CI configuration."""
    ci_path = project_dir / ".github" / "workflows" / "ci.yml"

    if ci_path.exists():
        result.add_pass("GitHub CI workflow exists")

        try:
            content = ci_path.read_text()

            # Check for important steps
            if "ruff" in content:
                result.add_pass("CI includes ruff (linting)")
            else:
                result.add_warning("CI doesn't include ruff (recommended)")

            if "mypy" in content:
                result.add_pass("CI includes mypy (type checking)")
            else:
                result.add_warning("CI doesn't include mypy (recommended)")

            if "pytest" in content:
                result.add_pass("CI includes pytest (testing)")
            else:
                result.add_warning("CI doesn't include pytest (recommended)")

        except Exception as e:
            result.add_error(f"Error reading CI workflow: {e}")
    else:
        result.add_warning(".github/workflows/ci.yml not found (recommended)")


def validate_company_guidelines(project_dir: Path, result: ValidationResult):
    """Check compliance with company guidelines."""
    # Check for .venv directory
    venv_dir = project_dir / ".venv"
    if venv_dir.exists():
        result.add_pass("Uses local .venv (company guideline)")
    else:
        result.add_warning("No local .venv found (company guideline recommends local .venv)")

    # Check Python version
    python_version_file = project_dir / ".python-version"
    if python_version_file.exists():
        try:
            version = python_version_file.read_text().strip()
            major, minor = map(int, version.split('.')[:2])
            if major == 3 and minor >= 9:
                result.add_pass(f"Python version {version} >= 3.9 (company guideline)")
            else:
                result.add_warning(f"Python version {version} < 3.9 (company guideline requires 3.9+)")
        except Exception:
            result.add_warning("Could not parse .python-version")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate project structure against company standards"
    )
    parser.add_argument(
        "project_dir",
        nargs="?",
        default=".",
        help="Project directory to validate (default: current directory)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )

    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()

    if not project_dir.exists():
        print(f"{Colors.RED}✗ Directory not found: {project_dir}{Colors.END}")
        sys.exit(1)

    if not project_dir.is_dir():
        print(f"{Colors.RED}✗ Not a directory: {project_dir}{Colors.END}")
        sys.exit(1)

    print(f"Validating project: {project_dir}")

    result = ValidationResult()

    # Run all validations
    validate_required_files(project_dir, result)
    validate_required_directories(project_dir, result)
    validate_src_layout(project_dir, result)
    validate_test_structure(project_dir, result)
    validate_internal_structure(project_dir, result)
    validate_agent_files(project_dir, result)
    validate_pyproject_toml(project_dir, result)
    validate_gitignore(project_dir, result)
    validate_placeholder_text(project_dir, result)
    validate_github_ci(project_dir, result)
    validate_company_guidelines(project_dir, result)

    # Print report
    passed = result.print_report()

    # Exit code
    if not passed:
        sys.exit(1)
    if args.strict and result.warnings:
        print(f"\n{Colors.YELLOW}--strict mode: Treating warnings as errors{Colors.END}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
