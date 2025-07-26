import pytest

from core.exceptions import ReportError
from core.reports.average_report import AverageResponseTimeReport
from core.log_entry import LogEntry
from datetime import datetime


def test_average_report_name():
    """Test report name"""
    report = AverageResponseTimeReport()
    assert report.report_name() == "average"


def test_average_report_generate_success():
    """Test generating a report"""
    logs = [
        LogEntry(datetime(2025, 6, 22, 10, 0), "/api/users", 100),
        LogEntry(datetime(2025, 6, 22, 10, 1), "/api/users", 200),
        LogEntry(datetime(2025, 6, 22, 10, 2), "/api/products", 50),
    ]

    report = AverageResponseTimeReport()
    result = report.build(logs)

    expected = [
        {"handler": "/api/users", "total": 2, "avg_response_time": 150.0},
        {"handler": "/api/products", "total": 1, "avg_response_time": 50.0},
    ]

    assert result == expected


def test_average_report_empty_logs():
    """Test generating a report with empty logs"""
    report = AverageResponseTimeReport()
    result = report.build([])

    assert result == []


def test_average_report_with_none_response_time():
    """Test generating a report with None response time"""
    logs = [
        LogEntry(datetime(2025, 6, 22, 10, 0), "/api/test", 100),
        LogEntry(datetime(2025, 6, 22, 10, 1), "/api/test", None),  # None время ответа
        LogEntry(datetime(2025, 6, 22, 10, 2), "/api/test2", 200),
    ]

    report = AverageResponseTimeReport()
    with pytest.raises(ReportError):
        report.build(logs)

    logs[1].response_time = 200
    result = report.build(logs)

    expected = [
        {"handler": "/api/test", "total": 2, "avg_response_time": 150.0},
        {"handler": "/api/test2", "total": 1, "avg_response_time": 200.0},
    ]

    assert result == expected


def test_average_report_sorted_output():
    """Тест сортировки результата по endpoint'ам"""
    logs = [
        LogEntry(datetime(2025, 6, 22, 10, 0), "/api/zebra", 100),
        LogEntry(datetime(2025, 6, 22, 10, 1), "/api/apple", 200),
        LogEntry(datetime(2025, 6, 22, 10, 2), "/api/banana", 50),
    ]

    report = AverageResponseTimeReport()
    result = report.build(logs)

    # Проверяем сортировку
    endpoints = [item["handler"] for item in result]
    assert endpoints == ["/api/banana", "/api/zebra", "/api/apple"]
