import aiofiles
import orjson
from typing import AsyncGenerator

from core.interfaces.file_reader import BaseFileReader
from core.interfaces.log_entry import BaseLogEntry
from core.log_entry import LogEntry
from core.exceptions import LogFileNotFoundError


class LogFileReader(BaseFileReader):

    @staticmethod
    async def read_files(files, file_path=None) -> AsyncGenerator[BaseLogEntry, None]:
        for file in files:
            try:
                async with aiofiles.open(
                    file if len(file_path) < 0 else file_path + file, "r"
                ) as f:
                    async for line in f:
                        try:
                            log_entry = orjson.loads(line.strip())
                            yield LogEntry.from_dict(log_entry)
                        except (orjson.JSONDecodeError, KeyError, ValueError):
                            continue
            except FileNotFoundError:
                raise LogFileNotFoundError(file)
