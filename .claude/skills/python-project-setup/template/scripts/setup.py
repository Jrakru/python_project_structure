#!/usr/bin/env python3
"""Setup development environment for PROJECT_NAME."""

import subprocess
import sys
from pathlib import Path


def main():
    """Setup development environment."""
    print("🔧 Setting up development environment for PROJECT_NAME...")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required")
        return 1
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", ".[dev]"],
            check=True
        )
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return 1
    
    print("\n✅ Development environment ready!")
    print("\nNext steps:")
    print("  - Run tests: pytest")
    print("  - Run linting: ruff check src/")
    print("  - Start coding!")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
