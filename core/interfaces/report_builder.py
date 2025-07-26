from dataclasses import dataclass
from abc import ABC, abstractmethod
from core.interfaces.log_entry import BaseLogEntry


@dataclass
class BaseReportBuilder(ABC):
    """
    Interface for report builders

    Provides methods for building reports
    """

    @abstractmethod
    def build(self, log_entries: list[BaseLogEntry]) -> list:
        """
        Entry point for report builders

        Args:
            log_entries (list[BaseLogEntry]): List of log entries

        Returns:
            list: List of reports
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def report_name() -> str:
        """
        Returns the name of the report

        Returns:
            str: Name of the report
        """
        raise NotImplemented