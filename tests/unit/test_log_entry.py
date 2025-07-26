import pytest
from datetime import datetime
from core.log_entry import LogEntry


def test_log_entry_creation():
    """Test creating a LogEntry"""
    timestamp = datetime.now()
    log_entry = LogEntry(
        timestamp=timestamp,
        endpoint="/api/test",
        response_time=150.5,
        user_agent="Test Agent",
        status_code=200,
    )

    assert log_entry.timestamp == timestamp
    assert log_entry.endpoint == "/api/test"
    assert log_entry.response_time == 150.5
    assert log_entry.user_agent == "Test Agent"
    assert log_entry.status_code == 200


def test_log_entry_from_dict():
    """Test creating a LogEntry from a dictionary"""
    data = {
        "@timestamp": "2025-06-22T10:00:00",
        "url": "/api/test",
        "response_time": 150,
        "http_user_agent": "Test Agent",
        "status": 200,
    }

    log_entry = LogEntry.from_dict(data)

    assert log_entry.timestamp == datetime.fromisoformat(data.get("@timestamp"))
    assert log_entry.endpoint == data.get("url")
    assert log_entry.response_time == data.get("response_time")
    assert log_entry.user_agent == data.get("http_user_agent")
    assert log_entry.status_code == data.get("status")


def test_log_entry_from_dict_optional_fields():
    """Test creating a LogEntry from a dictionary with optional fields"""
    data = {
        "@timestamp": "2025-06-22T10:00:00",
        "url": "/api/test",
        "response_time": 150,
    }

    log_entry = LogEntry.from_dict(data)

    assert log_entry.timestamp == datetime.fromisoformat(data.get("@timestamp"))
    assert log_entry.endpoint == data.get("url")
    assert log_entry.response_time == data.get("response_time")
    assert log_entry.user_agent is None
    assert log_entry.status_code is None
