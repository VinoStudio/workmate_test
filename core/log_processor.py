from core.interfaces.log_entry import BaseLogEntry
from core.log_entry import LogEntry
from core.filters import DateFilter


class LogProcessor:
    """
    Processes logs entrypoint.
    """

    @staticmethod
    def process_logs(
        logs: list[BaseLogEntry], date_filter: str = None
    ) -> list[BaseLogEntry]:
        """
        Filters logs by received date

        Args:
            logs (List[LogEntry]): List of logs
            date_filter (str): Date to filter by

        Returns:
            List[LogEntry]: List of filtered logs
        """
        processed_logs = logs

        if date_filter:
            target_date = DateFilter.parse_date(date_filter)
            processed_logs = DateFilter.filter_by_date(processed_logs, target_date)

        return processed_logs
