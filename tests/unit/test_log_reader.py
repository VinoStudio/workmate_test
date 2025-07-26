import pytest
import os
from core.log_reader import LogFileReader
from core.exceptions import LogFileNotFoundError

@pytest.mark.asyncio
async def test_read_files_success(temp_log_file, sample_log_data):
    """Тест успешного чтения файлов"""
    reader = LogFileReader()
    logs = [log async for log in reader.read_files([temp_log_file])]

    assert len(logs) == len(sample_log_data)

    # Проверяем первую запись
    first_log = logs[0]
    expected_first = sample_log_data[0]
    assert first_log.endpoint == expected_first["endpoint"]
    assert first_log.response_time == expected_first["response_time"]


# def test_read_files_with_errors(temp_log_file_with_errors):
#     """Тест чтения файлов с ошибками"""
#     reader = LogFileReader()
#     logs = list(reader.read_files([temp_log_file_with_errors]))
#
#     # Должна быть только одна корректная запись
#     assert len(logs) == 1
#     assert logs[0].endpoint == "/api/test"
#
#
# def test_read_empty_file(empty_log_file):
#     """Тест чтения пустого файла"""
#     reader = LogFileReader()
#     logs = list(reader.read_files([empty_log_file]))
#
#     assert len(logs) == 0
#
#
# def test_read_nonexistent_file():
#     """Тест чтения несуществующего файла"""
#     reader = LogFileReader()
#
#     with pytest.raises(LogFileError) as exc_info:
#         list(reader.read_files(["/nonexistent/file.log"]))
#
#     assert "Файл не найден" in str(exc_info.value)
#
#
# def test_read_file_without_permissions(temp_log_file):
#     """Тест чтения файла без прав доступа (частичный тест)"""
#     reader = LogFileReader()
#
#     # Этот тест может не работать на всех системах
#     # Пока просто проверим, что нет исключений при нормальном доступе
#     logs = list(reader.read_files([temp_log_file]))
#     assert isinstance(logs, list)
#
#
# def test_read_multiple_files(temp_log_file, sample_log_data):
#     """Тест чтения нескольких файлов"""
#     reader = LogFileReader()
#     logs = list(reader.read_files([temp_log_file, temp_log_file]))
#
#     # Должно быть в 2 раза больше записей
#     assert len(logs) == len(sample_log_data) * 2
