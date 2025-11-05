#!/usr/bin/env python3
"""
Interactive project setup script.

Scaffolds a new Python project from the template with guided customization.
"""

import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text: str) -> None:
    """Print formatted header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{text}{Colors.END}")


def print_success(text: str) -> None:
    """Print success message."""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")


def print_info(text: str) -> None:
    """Print info message."""
    print(f"{Colors.CYAN}→ {text}{Colors.END}")


def print_warning(text: str) -> None:
    """Print warning message."""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")


def print_error(text: str) -> None:
    """Print error message."""
    print(f"{Colors.RED}✗ {text}{Colors.END}")


def get_input(prompt: str, default: Optional[str] = None) -> str:
    """Get user input with optional default."""
    if default:
        prompt_text = f"{prompt} [{default}]: "
    else:
        prompt_text = f"{prompt}: "

    value = input(prompt_text).strip()
    return value if value else (default or "")


def get_yes_no(prompt: str, default: bool = True) -> bool:
    """Get yes/no input."""
    default_str = "Y/n" if default else "y/N"
    response = input(f"{prompt} [{default_str}]: ").strip().lower()

    if not response:
        return default
    return response in ['y', 'yes']


def validate_package_name(name: str) -> bool:
    """Validate Python package name."""
    pattern = r'^[a-z][a-z0-9_]*$'
    return bool(re.match(pattern, name))


def validate_python_version(version: str) -> bool:
    """Validate Python version string."""
    pattern = r'^\d+\.\d+$'
    return bool(re.match(pattern, version))


def find_template_dir() -> Path:
    """Find the template directory."""
    # Try relative to script location
    script_dir = Path(__file__).parent.parent
    template_dir = script_dir / "template"

    if template_dir.exists():
        return template_dir

    # Try relative to current directory
    template_dir = Path(".claude/skills/python-project-setup/template")
    if template_dir.exists():
        return template_dir

    raise FileNotFoundError(
        "Could not find template directory. "
        "Run this script from the repository root or ensure template exists."
    )


def copy_template(template_dir: Path, target_dir: Path) -> None:
    """Copy template to target directory."""
    print_info(f"Copying template from {template_dir}")
    print_info(f"Creating project at {target_dir}")

    if target_dir.exists():
        if not get_yes_no(f"Directory {target_dir} exists. Overwrite?", False):
            print_error("Aborted")
            sys.exit(1)
        shutil.rmtree(target_dir)

    shutil.copytree(template_dir, target_dir)
    print_success(f"Template copied to {target_dir}")


def replace_in_file(file_path: Path, replacements: dict[str, str]) -> None:
    """Replace placeholders in a file."""
    try:
        content = file_path.read_text()

        for old, new in replacements.items():
            content = content.replace(old, new)

        file_path.write_text(content)
    except Exception as e:
        print_warning(f"Could not process {file_path}: {e}")


def customize_project(project_dir: Path, config: dict) -> None:
    """Customize project files with user config."""
    print_header("Customizing project files...")

    replacements = {
        "PROJECT_NAME": config["package_name"],
        "PROJECT_DISPLAY_NAME": config["display_name"],
        "USERNAME": config["github_username"],
        "[fullname]": config["author_name"],
        "[year]": str(datetime.now().year),
        "[DATE]": datetime.now().strftime("%Y-%m-%d"),
        "you@company.com": config["author_email"],
    }

    # Rename src/PROJECT_NAME to src/package_name
    src_dir = project_dir / "src" / "PROJECT_NAME"
    if src_dir.exists():
        new_src_dir = project_dir / "src" / config["package_name"]
        src_dir.rename(new_src_dir)
        print_success(f"Renamed src/PROJECT_NAME to src/{config['package_name']}")

    # Replace placeholders in files
    file_patterns = [
        "*.md",
        "*.toml",
        "*.py",
        "*.yml",
        "*.yaml",
        "*.txt",
    ]

    files_to_process = []
    for pattern in file_patterns:
        files_to_process.extend(project_dir.rglob(pattern))

    for file_path in files_to_process:
        if file_path.is_file():
            replace_in_file(file_path, replacements)

    # Update .python-version if specified
    if config.get("python_version"):
        python_version_file = project_dir / ".python-version"
        python_version_file.write_text(f"{config['python_version']}\n")
        print_success(f"Set Python version to {config['python_version']}")

    print_success("Project customization complete")


def initialize_git(project_dir: Path) -> None:
    """Initialize git repository."""
    print_header("Initializing Git repository...")

    try:
        subprocess.run(
            ["git", "init"],
            cwd=project_dir,
            check=True,
            capture_output=True
        )
        print_success("Git repository initialized")

        # Initial commit
        subprocess.run(
            ["git", "add", "."],
            cwd=project_dir,
            check=True,
            capture_output=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit from template"],
            cwd=project_dir,
            check=True,
            capture_output=True
        )
        print_success("Initial commit created")

    except subprocess.CalledProcessError as e:
        print_error(f"Git initialization failed: {e}")
    except FileNotFoundError:
        print_warning("Git not found. Skipping repository initialization")


def setup_venv(project_dir: Path, use_poetry: bool) -> None:
    """Set up virtual environment."""
    print_header("Setting up virtual environment...")

    if use_poetry:
        print_info("Using Poetry for environment management")
        try:
            # Check if poetry is installed
            subprocess.run(
                ["poetry", "--version"],
                check=True,
                capture_output=True
            )

            # Initialize poetry project
            subprocess.run(
                ["poetry", "install"],
                cwd=project_dir,
                check=True
            )
            print_success("Poetry environment created and dependencies installed")

        except FileNotFoundError:
            print_error("Poetry not found. Install with: curl -sSL https://install.python-poetry.org | python3 -")
            print_info("Falling back to standard venv")
            use_poetry = False
        except subprocess.CalledProcessError as e:
            print_error(f"Poetry setup failed: {e}")
            return

    if not use_poetry:
        print_info("Using standard venv")
        try:
            venv_dir = project_dir / ".venv"
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_dir)],
                check=True
            )
            print_success("Virtual environment created at .venv")

            # Install in editable mode
            if sys.platform == "win32":
                pip_path = venv_dir / "Scripts" / "pip"
            else:
                pip_path = venv_dir / "bin" / "pip"

            subprocess.run(
                [str(pip_path), "install", "-e", ".[dev]"],
                cwd=project_dir,
                check=True
            )
            print_success("Dependencies installed")

        except subprocess.CalledProcessError as e:
            print_error(f"venv setup failed: {e}")


def run_tests(project_dir: Path) -> None:
    """Run initial tests to verify setup."""
    print_header("Running initial tests...")

    try:
        # Try to run pytest
        result = subprocess.run(
            ["pytest", "-v"],
            cwd=project_dir,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print_success("All tests passed!")
        else:
            print_warning("Some tests failed. Check pytest output.")

    except FileNotFoundError:
        print_warning("pytest not found. Skipping tests.")


def print_next_steps(project_dir: Path, config: dict) -> None:
    """Print next steps for user."""
    print_header("Setup Complete! 🎉")
    print()
    print("Next steps:")
    print()
    print(f"1. Navigate to your project:")
    print(f"   cd {project_dir}")
    print()
    print(f"2. Activate virtual environment:")
    if config.get("use_poetry"):
        print(f"   poetry shell")
    else:
        if sys.platform == "win32":
            print(f"   .venv\\Scripts\\activate")
        else:
            print(f"   source .venv/bin/activate")
    print()
    print(f"3. Review and customize:")
    print(f"   - README.md - Update project description")
    print(f"   - AGENTS.md - Update project-specific info")
    print(f"   - .github/copilot-instructions.md - Update comprehensive context")
    print(f"   - _internal/CONSTITUTION.md - Update project rules")
    print(f"   - _internal/project/AGENT_START_HERE.md - Update current status")
    print()
    print(f"4. Start developing:")
    print(f"   - Add code to src/{config['package_name']}/")
    print(f"   - Add tests to tests/")
    print(f"   - Run tests: pytest")
    print(f"   - Run linting: ruff check src/")
    print(f"   - Run type checking: mypy src/")
    print()
    print("For more information, see:")
    print("  - FILE_GUIDE.md (in skill directory)")
    print("  - STRUCTURE_REFERENCE.md (in skill directory)")
    print("  - GUIDELINES.md (in skill directory)")


def main():
    """Main entry point."""
    print_header("Python Project Setup")
    print()
    print("This script will create a new Python project from the template.")
    print()

    # Find template directory
    try:
        template_dir = find_template_dir()
    except FileNotFoundError as e:
        print_error(str(e))
        sys.exit(1)

    # Gather configuration
    print_header("Project Configuration")

    config = {}

    # Package name
    while True:
        package_name = get_input(
            "Package name (lowercase, underscores OK)",
            "my_package"
        )
        if validate_package_name(package_name):
            config["package_name"] = package_name
            break
        print_error("Invalid package name. Use lowercase letters, numbers, underscores only.")

    # Display name
    config["display_name"] = get_input(
        "Display name (human-readable)",
        config["package_name"].replace("_", " ").title()
    )

    # Author info
    config["author_name"] = get_input("Author name", "Your Name")
    config["author_email"] = get_input("Author email", "you@company.com")
    config["github_username"] = get_input("GitHub username", "your-username")

    # Python version
    while True:
        python_version = get_input("Python version", "3.9")
        if validate_python_version(python_version):
            config["python_version"] = python_version
            break
        print_error("Invalid version format. Use X.Y (e.g., 3.9, 3.11)")

    # Target directory
    default_target = Path.cwd() / config["package_name"]
    target_dir_str = get_input(
        "Target directory",
        str(default_target)
    )
    target_dir = Path(target_dir_str).expanduser().resolve()

    # Options
    init_git = get_yes_no("Initialize Git repository?", True)
    config["use_poetry"] = get_yes_no("Use Poetry for environment management?", True)
    setup_env = get_yes_no("Set up virtual environment now?", True)
    run_initial_tests = get_yes_no("Run initial tests?", True)

    # Confirmation
    print()
    print_header("Configuration Summary")
    print(f"Package name:     {config['package_name']}")
    print(f"Display name:     {config['display_name']}")
    print(f"Author:           {config['author_name']} <{config['author_email']}>")
    print(f"GitHub username:  {config['github_username']}")
    print(f"Python version:   {config['python_version']}")
    print(f"Target directory: {target_dir}")
    print(f"Use Poetry:       {'Yes' if config['use_poetry'] else 'No'}")
    print()

    if not get_yes_no("Proceed with setup?", True):
        print_error("Aborted")
        sys.exit(0)

    # Execute setup
    try:
        copy_template(template_dir, target_dir)
        customize_project(target_dir, config)

        if init_git:
            initialize_git(target_dir)

        if setup_env:
            setup_venv(target_dir, config["use_poetry"])

        if run_initial_tests:
            run_tests(target_dir)

        print_next_steps(target_dir, config)

    except Exception as e:
        print_error(f"Setup failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
