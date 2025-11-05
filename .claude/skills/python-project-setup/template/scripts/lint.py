#!/usr/bin/env python3
"""Run linting checks for PROJECT_NAME."""

import argparse
import subprocess
import sys


def main():
    """Run all linting checks."""
    parser = argparse.ArgumentParser(description="Run linting checks")
    parser.add_argument("--fix", action="store_true", help="Auto-fix issues")
    args = parser.parse_args()
    
    print("🔍 Running ruff...")
    cmd = ["ruff", "check", "src/", "tests/"]
    if args.fix:
        cmd.append("--fix")
    
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("❌ Linting failed")
        return 1
    
    print("✅ Linting passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
