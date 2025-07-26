from collections import Counter
from typing import Any

from core.exceptions import ReportError
from core.interfaces.log_entry import BaseLogEntry
from core.interfaces.report_builder import BaseReportBuilder


class EndpointCountReport(BaseReportBuilder):
    """
    Report builder for endpoint count
    """

    @staticmethod
    def report_name() -> str:
        return "endpoint_count"

    def build(self, logs: list[BaseLogEntry]) -> list[dict[str, Any]]:
        try:
            counter = Counter(log.endpoint for log in logs)

            result = [
                {"Endpoint": endpoint, "Count": count}
                for endpoint, count in counter.items()
            ]

            return sorted(result, key=lambda x: x["Count"], reverse=True)

        except (TypeError, KeyError, ZeroDivisionError, ValueError, AttributeError):
            raise ReportError("")
