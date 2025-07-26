import aiofiles
import orjson
from typing import AsyncGenerator
from core.interfaces.log_entry import BaseLogEntry
from core.log_entry import LogEntry

class LogFileReader:

    @staticmethod
    async def read_file(file_path) -> AsyncGenerator[BaseLogEntry]:
        async with aiofiles.open(file_path, 'r') as f:
            async for line in f:
                try:
                    log_entry = orjson.loads(line.strip())
                    yield LogEntry.from_dict(log_entry)
                except (orjson.JSONDecodeError, KeyError, ValueError):
                    continue