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
