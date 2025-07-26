from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from core.interfaces.log_entry import BaseLogEntry


@dataclass(slots=True, eq=True)
class LogEntry(BaseLogEntry):
    """
    Class representing a log entry

    Attributes:
        timestamp (datetime): Timestamp of the log entry
        endpoint (str): Endpoint of the log entry
        response_time (float): Response time of the log entry
        user_agent (Optional[str]): User agent of the log entry
        status_code (Optional[int]): Status code of the log entry
    """

    timestamp: datetime
    endpoint: str
    response_time: float
    user_agent: Optional[str] = None
    status_code: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            timestamp=datetime.fromisoformat(data["@timestamp"]),
            endpoint=data["url"],
            response_time=float(data["response_time"]),
            user_agent=data.get("http_user_agent"),
            status_code=data.get("status"),
        )
