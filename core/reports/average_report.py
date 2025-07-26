from collections import defaultdict
from typing import Any

from core.interfaces.log_entry import BaseLogEntry
from core.interfaces.report_builder import BaseReportBuilder


class AverageResponseTimeReport(BaseReportBuilder):
    """Отчет по среднему времени ответа по endpoint'ам"""

    @property
    def report_name(self) -> str:
        return "average_report"

    def build(self, logs: list[BaseLogEntry]) -> list[dict[str, Any]]:
        endpoint_stats = defaultdict(lambda: {'count': 0, 'total_time': 0.0})

        for log in logs:
            endpoint_stats[log.endpoint]['count'] += 1
            endpoint_stats[log.endpoint]['total_time'] += log.response_time

        result = []
        for endpoint, stats in endpoint_stats.items():
            avg_time = stats['total_time'] / stats['count']
            result.append({
                'Endpoint': endpoint,
                'Requests': stats['count'],
                'Avg Time': round(avg_time, 2)
            })

        return sorted(result, key=lambda x: x['Endpoint'])