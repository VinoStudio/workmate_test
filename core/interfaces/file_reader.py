from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseFileReader(ABC):

    @staticmethod
    @abstractmethod
    def read_files(files: list[str], file_path: str | None):
        """
        Base class for file readers

        Args:
            files (list[str]): List of files to read
            file_path (str): Absolute path to file
        """
        raise NotImplemented
