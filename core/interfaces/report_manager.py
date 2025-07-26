from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.interfaces.report_builder import BaseReportBuilder


@dataclass
class BaseReportManager(ABC):

    @abstractmethod
    def add_report(self, report_name: str, report_builder: type[BaseReportBuilder]) -> None:
        raise NotImplemented

    @abstractmethod
    def get_reports(self):
        raise NotImplemented

    @abstractmethod
    def get_report(self, report_name: str):
        raise NotImplemented