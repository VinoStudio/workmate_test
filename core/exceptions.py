from dataclasses import dataclass


@dataclass(frozen=True)
class LogParserError(Exception):
    value: str

    @property
    def message(self):
        return f"{self.__class__.__name__}: occurred"


@dataclass(frozen=True)
class ReportError(LogParserError):
    value: str

    @property
    def message(self):
        return f"{self.__class__.__name__}: occurred while building report. Please check if logs possess valid data."


@dataclass(frozen=True)
class ReportNotFoundError(LogParserError):
    value: str

    @property
    def message(self):
        return f"{self.__class__.__name__}: given {self.value!r} report not found"


@dataclass(frozen=True)
class LogFileNotFoundError(LogParserError):
    value: str

    @property
    def message(self):
        return f"{self.__class__.__name__}: given log file {self.value!r} not found"


@dataclass(frozen=True)
class InvalidDateError(LogParserError):
    value: str

    @property
    def message(self):
        return f"{self.__class__.__name__}: given {self.value!r} date is invalid. Try format 'YYYY-DD-MM'"
