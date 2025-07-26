from core.interfaces.report_manager import BaseReportManager
from core.reports.report_registry import ReportManager
from core.reports.average_report import AverageResponseTimeReport
from core.reports.endpoint_report import EndpointCountReport


def create_report_manager() -> BaseReportManager:
    """
    Handler for creating report manager and adding reports in it
    """
    report_manager = ReportManager()

    report_manager.add_report(
        AverageResponseTimeReport.report_name(), AverageResponseTimeReport
    )
    report_manager.add_report(EndpointCountReport.report_name(), EndpointCountReport)

    return report_manager
