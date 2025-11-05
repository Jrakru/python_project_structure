#!/bin/bash
cd "/home/jpw/git/second-brain/3. Resource/Python Project Structure/starter_pack"

# Create tests/__init__.py
cat > tests/__init__.py << 'EOF'
"""Tests for PROJECT_NAME."""
EOF

# Create tests/conftest.py
cat > tests/conftest.py << 'EOF'
"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value", "number": 42}


@pytest.fixture
def temp_file(tmp_path):
    """Provide a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    return file_path
EOF

# Create tests/unit/test_example.py
cat > tests/unit/test_example.py << 'EOF'
"""Example unit tests for PROJECT_NAME."""

import PROJECT_NAME


def test_version_is_defined():
    """Version should be defined in package."""
    assert hasattr(PROJECT_NAME, "__version__")
    assert isinstance(PROJECT_NAME.__version__, str)


def test_version_format():
    """Version should follow semantic versioning."""
    version = PROJECT_NAME.__version__
    parts = version.split(".")
    assert len(parts) == 3, "Version should have major.minor.patch format"


def test_example_with_fixture(sample_data):
    """Example test using a fixture."""
    assert sample_data["key"] == "value"
    assert sample_data["number"] == 42


def test_temp_file_exists(temp_file):
    """Example test using temp_file fixture."""
    assert temp_file.exists()
    content = temp_file.read_text()
    assert content == "test content"
EOF

# Create tests/integration/.gitkeep
touch tests/integration/.gitkeep

# Create tests/e2e/.gitkeep
touch tests/e2e/.gitkeep

# Create tests/fixtures/.gitkeep
touch tests/fixtures/.gitkeep

echo "✅ Test templates created"
