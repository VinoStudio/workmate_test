from dataclasses import dataclass, field
from core.interfaces.report_builder import BaseReportBuilder
from core.interfaces.report_manager import BaseReportManager
from core.exceptions import ReportNotFoundError


@dataclass
class ReportManager(BaseReportManager):
    """
    Class that stores, registers and retrieves report builders

    Attributes:
        _report_builders (dict[str, type[BaseReportBuilder]]): Dictionary of report builders.
        with key - report name
        value - report builder type
    """

    _report_builders: dict[str, type[BaseReportBuilder]] = field(default_factory=dict)

    def add_report(
        self, report_name: str, report_builder: type[BaseReportBuilder]
    ) -> None:
        self._report_builders.update({report_name: report_builder})

    def get_report(self, report_name: str):
        report = self._report_builders.get(report_name)

        if report is None:
            raise ReportNotFoundError(report_name)

        return report

    def get_reports(self):
        return self._report_builders
