from collections import defaultdict
from typing import Any

from core.interfaces.log_entry import BaseLogEntry
from core.interfaces.report_builder import BaseReportBuilder
from core.exceptions import ReportError


class AverageResponseTimeReport(BaseReportBuilder):
    """
    Report builder for average response time calculations by endpoint
    """

    @staticmethod
    def report_name() -> str:
        return "average"

    def build(self, logs: list[BaseLogEntry]) -> list[dict[str, Any]]:
        """
        Entry point for report builders

        Args:
            logs (list[BaseLogEntry]): List of LogEntry's

        Returns:
            list: List of sorted reports by total count and average response time(less time higher)
        """
        try:
            endpoint_stats = defaultdict(lambda: {"count": 0, "total_time": 0.0})

            for log in logs:
                endpoint_stats[log.endpoint]["count"] += 1
                endpoint_stats[log.endpoint]["total_time"] += log.response_time

            result = []
            for endpoint, stats in endpoint_stats.items():
                avg_time = stats["total_time"] / stats["count"]
                result.append(
                    {
                        "handler": endpoint,
                        "total": stats["count"],
                        "avg_response_time": round(avg_time, 3),
                    }
                )

            return sorted(
                result,
                key=lambda x: (x["total"], -x["avg_response_time"]),
                reverse=True,
            )
        except (TypeError, KeyError, ZeroDivisionError, ValueError, AttributeError):
            raise ReportError("")
