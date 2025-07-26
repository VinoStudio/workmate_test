from typing import List
from datetime import datetime, date

from core.interfaces.log_entry import BaseLogEntry
from core.log_entry import LogEntry
from core.exceptions import InvalidDateError


class DateFilter:
    """
    Filters logs by date
    """

    @staticmethod
    def filter_by_date(
        logs: list[BaseLogEntry], target_date: date
    ) -> list[BaseLogEntry]:
        """
        Filters logs by date

        Args:
            logs (List[LogEntry]): List of logs
            target_date (date): Date to filter by

        Returns:
            List[LogEntry]: List of filtered logs
        """
        return [log for log in logs if log.timestamp.date() == target_date]

    @staticmethod
    def parse_date(date_str: str) -> date:
        """
        Parses a date string into a date object

        Args:
            date_str (str): Date string to parse

        Returns:
            date: Parsed date
        """
        try:
            return datetime.strptime(date_str, "%Y-%d-%m").date()
        except ValueError:
            raise InvalidDateError(date_str)
