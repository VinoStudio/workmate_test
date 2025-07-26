import pytest
import tempfile
import orjson

from tests import parametrize_data as data
from pathlib import Path


@pytest.fixture(scope="session")
def temp_log_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log") as f:
        for log in data.example_logs:
            json_line = orjson.dumps(log).decode("utf-8")
            f.write(json_line + "\n")
        log_file_path = f.name

    yield log_file_path

    Path(log_file_path).unlink()


@pytest.fixture(scope="session")
def temp_log_file_with_errors():
    """Fixture to create a temporary log file with errors""" ""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        for log in data.invalid_log:
            json_line = orjson.dumps(log).decode("utf-8")
            f.write(json_line + "\n")
        temp_path = f.name

    yield temp_path

    Path(temp_path).unlink()


@pytest.fixture
def empty_log_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        log_file_path = f.name

    yield log_file_path

    Path(log_file_path).unlink()
