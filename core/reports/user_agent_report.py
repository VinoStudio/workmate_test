from typing import Any

from core.interfaces.log_entry import BaseLogEntry
from core.interfaces.report_builder import BaseReportBuilder


class UserAgentReport(BaseReportBuilder):
    @staticmethod
    def report_name() -> str:
        return "user_agent"

    def build(self, logs: list[BaseLogEntry]) -> list[dict[str, Any]]:
        pass
