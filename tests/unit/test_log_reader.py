import pytest
import os

from tests import parametrize_data as test_data
from core.log_reader import LogFileReader
from core.exceptions import LogFileNotFoundError


@pytest.mark.asyncio
async def test_read_files_success(temp_log_file):
    """Test reading log files successfully"""
    reader = LogFileReader()

    logs = [log async for log in reader.read_files([temp_log_file])]

    assert len(logs) == len(test_data.example_logs)

    first_log = logs[0]
    expected_first = test_data.example_logs[0]
    assert first_log.endpoint == expected_first["url"]
    assert first_log.response_time == expected_first["response_time"]


@pytest.mark.asyncio
async def test_read_files_with_errors(temp_log_file_with_errors):
    """Test reading log files with errors"""
    reader = LogFileReader()
    logs = [log async for log in reader.read_files([temp_log_file_with_errors])]

    assert len(logs) == 1
    assert logs[0].endpoint == "/api/test"


@pytest.mark.asyncio
async def test_read_empty_file(empty_log_file):
    """Test reading an empty log file"""
    reader = LogFileReader()
    logs = [log async for log in reader.read_files([empty_log_file])]

    assert len(logs) == 0


@pytest.mark.asyncio
async def test_read_nonexistent_file():
    """Test reading a non-existent log file"""
    reader = LogFileReader()

    with pytest.raises(LogFileNotFoundError) as exc_info:
        logs = [log async for log in reader.read_files(["/nonexistent/file.log"])]

    assert "/nonexistent/file.log" in str(exc_info.value)


@pytest.mark.asyncio
async def test_read_multiple_files(temp_log_file, temp_log_file_with_errors):
    """Test reading multiple log files"""
    reader = LogFileReader()
    logs = [
        log
        async for log in reader.read_files([temp_log_file_with_errors, temp_log_file])
    ]

    assert len(logs) == len(test_data.example_logs) + 1
