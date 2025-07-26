from core.interfaces.report_manager import BaseReportManager
from core.reports.report_registry import ReportManager
from core.reports.average_report import AverageResponseTimeReport
from core.reports.endpoint_report import EndpointCountReport


def create_report_manager() -> BaseReportManager:
    report_manager = ReportManager()
    report_manager.add_report("average", AverageResponseTimeReport)
    report_manager.add_report("endpoint_count", EndpointCountReport)

    return report_manager