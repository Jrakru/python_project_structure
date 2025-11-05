#!/usr/bin/env python3
"""Run test suite for PROJECT_NAME."""

import argparse
import subprocess
import sys


def main():
    """Run tests with various options."""
    parser = argparse.ArgumentParser(description="Run test suite")
    parser.add_argument("--fast", action="store_true", help="Skip slow tests")
    parser.add_argument("--coverage", action="store_true", help="Generate coverage report")
    parser.add_argument("--watch", action="store_true", help="Watch mode (not implemented)")
    args = parser.parse_args()
    
    cmd = ["pytest", "-v"]
    
    if args.fast:
        cmd.extend(["-m", "not slow"])
    
    if args.coverage:
        cmd.extend(["--cov=src", "--cov-report=term", "--cov-report=html"])
    
    print(f"🧪 Running tests: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("❌ Tests failed")
        return 1
    
    print("✅ Tests passed!")
    if args.coverage:
        print("\n📊 Coverage report generated in htmlcov/")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
