from typing import Iterable, Self
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseLogEntry(ABC):

    @abstractmethod
    def from_dict(self, data: Iterable) -> Self:
        raise NotImplemented