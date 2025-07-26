from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.interfaces.report_builder import BaseReportBuilder


@dataclass
class BaseReportManager(ABC):
    """
    Interface for report manager
    """

    @abstractmethod
    def add_report(
        self, report_name: str, report_builder: type[BaseReportBuilder]
    ) -> None:
        """
        Store report builder by report name in report manager

        Args:
            report_name (str): Report name
            report_builder (type[BaseReportBuilder]): Report builder

        """
        raise NotImplemented

    @abstractmethod
    def get_reports(self):
        """
        Retrieve all report builders from report manager

        Returns:
            list[type[BaseReportBuilder]]: List of report builders
        """
        raise NotImplemented

    @abstractmethod
    def get_report(self, report_name: str):
        """
        Retrieve report builder by report name from report manager

        Args:
            report_name (str): Report name

        Returns:
            type[BaseReportBuilder]: Report builder
        """
        raise NotImplemented
