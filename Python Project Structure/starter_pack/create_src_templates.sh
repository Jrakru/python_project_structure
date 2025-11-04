#!/bin/bash
cd "/home/jpw/git/second-brain/3. Resource/Python Project Structure/starter_pack"

# Create src/PROJECT_NAME/__init__.py
cat > src/PROJECT_NAME/__init__.py << 'EOF'
"""PROJECT_DISPLAY_NAME - Short description."""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Public API exports
__all__ = [
    "__version__",
]
EOF

# Create src/PROJECT_NAME/__main__.py
cat > src/PROJECT_NAME/__main__.py << 'EOF'
"""CLI entry point for PROJECT_NAME."""

import sys


def main() -> int:
    """Main CLI entry point.
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    print("PROJECT_DISPLAY_NAME v0.1.0")
    print("CLI functionality not implemented yet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
EOF

# Create src/PROJECT_NAME/core/__init__.py
mkdir -p src/PROJECT_NAME/core
cat > src/PROJECT_NAME/core/__init__.py << 'EOF'
"""Core business logic for PROJECT_NAME."""

__all__ = []
EOF

# Create src/PROJECT_NAME/models/__init__.py
mkdir -p src/PROJECT_NAME/models
cat > src/PROJECT_NAME/models/__init__.py << 'EOF'
"""Data models for PROJECT_NAME."""

__all__ = []
EOF

# Create src/PROJECT_NAME/utils/__init__.py
mkdir -p src/PROJECT_NAME/utils
cat > src/PROJECT_NAME/utils/__init__.py << 'EOF'
"""Utility functions for PROJECT_NAME."""

__all__ = []
EOF

echo "✅ Source code templates created"
