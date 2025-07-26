import pytest
from datetime import date, datetime

from core.exceptions import InvalidDateError
from core.filters import DateFilter
from core.log_entry import LogEntry


def test_filter_by_date_success():
    """Test filtering logs by date"""
    target_date = date(2025, 6, 22)

    logs = [
        LogEntry(datetime(2025, 6, 22, 10, 0), "/api/test1", 100),
        LogEntry(datetime(2025, 6, 22, 11, 0), "/api/test2", 200),
        LogEntry(datetime(2025, 6, 23, 10, 0), "/api/test3", 300),
    ]

    filtered_logs = DateFilter.filter_by_date(logs, target_date)

    assert len(filtered_logs) == 2
    assert all(log.timestamp.date() == target_date for log in filtered_logs)


def test_parse_date_success():
    """Test parsing date successfully"""
    parsed_date = DateFilter.parse_date("2025-22-06")
    expected_date = date(2025, 6, 22)

    assert parsed_date == expected_date


def test_parse_date_invalid_format():
    """Test parsing date with invalid format"""
    with pytest.raises(InvalidDateError) as exc_info:
        DateFilter.parse_date("22-06-2025")

    assert "22-06-2025" in str(exc_info.value)


def test_parse_date_invalid_values():
    """Test parsing date with invalid values"""
    with pytest.raises(InvalidDateError) as exc_info:
        DateFilter.parse_date("2025-13-45")

    assert "2025-13-45" in str(exc_info.value)


def test_filter_empty_list():
    """Test filtering an empty list"""
    result = DateFilter.filter_by_date([], date(2025, 6, 22))
    assert result == []


def test_filter_no_matches():
    """Test filtering logs with no matches"""
    logs = [
        LogEntry(datetime(2025, 6, 21, 10, 0), "/api/test", 100),
        LogEntry(datetime(2025, 6, 23, 10, 0), "/api/test", 100),
    ]

    result = DateFilter.filter_by_date(logs, date(2025, 6, 22))
    assert result == []
