#!/usr/bin/env python3
"""
Show project structure information.

Displays what each file and folder is supposed to do by parsing
the STRUCTURE_REFERENCE.md and FILE_GUIDE.md documentation.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def find_skill_dir() -> Path:
    """Find the skill directory."""
    # Try multiple locations
    candidates = [
        Path(__file__).parent.parent,  # Relative to script
        Path(".claude/skills/python-project-setup"),  # From repo root
    ]

    for candidate in candidates:
        if (candidate / "STRUCTURE_REFERENCE.md").exists():
            return candidate

    raise FileNotFoundError("Could not find skill directory with STRUCTURE_REFERENCE.md")


def parse_structure_reference(skill_dir: Path) -> dict[str, dict]:
    """Parse STRUCTURE_REFERENCE.md to extract directory information."""
    ref_file = skill_dir / "STRUCTURE_REFERENCE.md"

    if not ref_file.exists():
        raise FileNotFoundError(f"STRUCTURE_REFERENCE.md not found at {ref_file}")

    content = ref_file.read_text()
    directories = {}

    # Parse markdown sections
    # Look for headers like ### `dir_name/` or #### `dir_name/`
    pattern = r'####+\s+`([^`]+)`\s*.*?\n\n\*\*Purpose\*\*:\s*(.+?)(?=\n\n|\n###)'

    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        dir_name = match.group(1).strip()
        purpose = match.group(2).strip()

        # Extract additional info
        section_content = content[match.start():match.end() + 500]

        # Extract audience
        audience_match = re.search(r'\*\*Audience\*\*:\s*(.+)', section_content)
        audience = audience_match.group(1).strip() if audience_match else ""

        # Extract content types
        content_match = re.search(r'\*\*Content\*\*:\s*(.+?)(?=\n\n|\n\*\*)', section_content, re.DOTALL)
        content_types = content_match.group(1).strip() if content_match else ""

        directories[dir_name] = {
            "purpose": purpose,
            "audience": audience,
            "content": content_types,
        }

    return directories


def parse_file_guide(skill_dir: Path) -> dict[str, dict]:
    """Parse FILE_GUIDE.md to extract file information."""
    guide_file = skill_dir / "FILE_GUIDE.md"

    if not guide_file.exists():
        raise FileNotFoundError(f"FILE_GUIDE.md not found at {guide_file}")

    content = guide_file.read_text()
    files = {}

    # Look for file sections
    pattern = r'####\s+`([^`]+)`\s+([✅🔒🔧]+\s+\w+)?\n\n\*\*(?:Location|Purpose)\*\*:\s*(.+?)(?=\n\n|\n####)'

    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        file_name = match.group(1).strip()
        visibility = match.group(2).strip() if match.group(2) else ""
        section_content = match.group(3)

        # Extract purpose
        purpose_match = re.search(r'\*\*Purpose\*\*:\s*(.+)', section_content)
        purpose = purpose_match.group(1).strip() if purpose_match else section_content[:200]

        # Extract must edit
        must_edit = "Yes" if "**Must Edit**: Yes" in section_content else "Optional"

        files[file_name] = {
            "purpose": purpose,
            "visibility": visibility,
            "must_edit": must_edit,
        }

    return files


def search_item(item_path: str, directories: dict, files: dict) -> Optional[dict]:
    """Search for an item in directories or files."""
    # Normalize path
    item_path = item_path.strip().rstrip('/')

    # Try exact match
    if item_path in directories:
        return {"type": "directory", **directories[item_path]}
    if item_path in files:
        return {"type": "file", **files[item_path]}

    # Try fuzzy match
    item_lower = item_path.lower()

    for dir_path, info in directories.items():
        if item_lower in dir_path.lower():
            return {"type": "directory", "path": dir_path, **info}

    for file_path, info in files.items():
        if item_lower in file_path.lower():
            return {"type": "file", "path": file_path, **info}

    return None


def print_item_info(item: dict, full: bool = False) -> None:
    """Print information about an item."""
    item_type = item.get("type", "unknown")
    path = item.get("path", "")

    if item_type == "directory":
        print(f"{Colors.HEADER}{Colors.BOLD}Directory:{Colors.END} {Colors.CYAN}{path}{Colors.END}")
        print()
        print(f"{Colors.BOLD}Purpose:{Colors.END}")
        print(f"  {item.get('purpose', 'N/A')}")
        print()

        if item.get("audience"):
            print(f"{Colors.BOLD}Audience:{Colors.END}")
            print(f"  {item['audience']}")
            print()

        if full and item.get("content"):
            print(f"{Colors.BOLD}Content:{Colors.END}")
            print(f"  {item['content']}")
            print()

    elif item_type == "file":
        print(f"{Colors.HEADER}{Colors.BOLD}File:{Colors.END} {Colors.CYAN}{path}{Colors.END}")
        print()

        if item.get("visibility"):
            print(f"{Colors.BOLD}Visibility:{Colors.END} {item['visibility']}")
            print()

        print(f"{Colors.BOLD}Purpose:{Colors.END}")
        print(f"  {item.get('purpose', 'N/A')}")
        print()

        if item.get("must_edit"):
            must_edit_color = Colors.RED if item["must_edit"] == "Yes" else Colors.GREEN
            print(f"{Colors.BOLD}Must Edit:{Colors.END} {must_edit_color}{item['must_edit']}{Colors.END}")
            print()


def list_all_directories(directories: dict) -> None:
    """List all directories."""
    print(f"{Colors.HEADER}{Colors.BOLD}All Directories:{Colors.END}")
    print()

    for dir_path in sorted(directories.keys()):
        purpose = directories[dir_path]["purpose"]
        # Truncate if too long
        if len(purpose) > 80:
            purpose = purpose[:77] + "..."
        print(f"  {Colors.CYAN}{dir_path:<40}{Colors.END} {purpose}")


def list_all_files(files: dict) -> None:
    """List all files."""
    print(f"{Colors.HEADER}{Colors.BOLD}All Files:{Colors.END}")
    print()

    for file_path in sorted(files.keys()):
        purpose = files[file_path]["purpose"]
        # Truncate if too long
        if len(purpose) > 60:
            purpose = purpose[:57] + "..."
        visibility = files[file_path].get("visibility", "")
        print(f"  {Colors.CYAN}{file_path:<30}{Colors.END} {visibility:<15} {purpose}")


def show_quick_reference() -> None:
    """Show quick reference table."""
    print(f"{Colors.HEADER}{Colors.BOLD}Quick Reference:{Colors.END}")
    print()

    quick_ref = [
        ("Project config", "pyproject.toml"),
        ("Quick agent ref", "AGENTS.md"),
        ("Detailed agent instructions", ".github/copilot-instructions.md"),
        ("Project constitution", "_internal/CONSTITUTION.md"),
        ("Agent entry point", "_internal/project/AGENT_START_HERE.md"),
        ("Checklists", "_internal/project/context/essential/checklists.md"),
        ("Warnings/gotchas", "_internal/project/context/essential/warnings.md"),
        ("Session log template", "_internal/project/learnings/raw/sessions/template.md"),
        ("CI/CD pipeline", ".github/workflows/ci.yml"),
        ("Public docs", "docs/README.md"),
        ("Dev setup script", "scripts/setup.py"),
        ("Linting script", "scripts/lint.py"),
        ("Test script", "scripts/test.py"),
        ("Package init", "src/PROJECT_NAME/__init__.py"),
        ("CLI entry", "src/PROJECT_NAME/__main__.py"),
        ("Test config", "tests/conftest.py"),
    ]

    for need, location in quick_ref:
        print(f"  {need:<35} → {Colors.CYAN}{location}{Colors.END}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Show project structure information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show info about a specific directory
  %(prog)s _internal/project/

  # Show info about a specific file
  %(prog)s pyproject.toml

  # List all directories
  %(prog)s --list-dirs

  # List all files
  %(prog)s --list-files

  # Show quick reference
  %(prog)s --quick-ref

  # Full details for an item
  %(prog)s _internal/ --full
        """
    )

    parser.add_argument(
        "path",
        nargs="?",
        help="Path to file or directory to show info about"
    )
    parser.add_argument(
        "--list-dirs",
        action="store_true",
        help="List all directories"
    )
    parser.add_argument(
        "--list-files",
        action="store_true",
        help="List all files"
    )
    parser.add_argument(
        "--quick-ref",
        action="store_true",
        help="Show quick reference table"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Show full details"
    )

    args = parser.parse_args()

    try:
        skill_dir = find_skill_dir()
        directories = parse_structure_reference(skill_dir)
        files = parse_file_guide(skill_dir)

        if args.list_dirs:
            list_all_directories(directories)

        elif args.list_files:
            list_all_files(files)

        elif args.quick_ref:
            show_quick_reference()

        elif args.path:
            item = search_item(args.path, directories, files)
            if item:
                print_item_info(item, args.full)
            else:
                print(f"{Colors.RED}✗ Not found: {args.path}{Colors.END}")
                print()
                print("Try one of:")
                print("  --list-dirs    List all directories")
                print("  --list-files   List all files")
                print("  --quick-ref    Show quick reference")
                sys.exit(1)

        else:
            # No args, show quick reference
            show_quick_reference()

    except FileNotFoundError as e:
        print(f"{Colors.RED}✗ Error: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}✗ Unexpected error: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
