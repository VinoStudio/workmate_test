# Тестовое задание для [work-mate](https://work-mate.ru/)

## Выполнить скрипт можно следующими способами:

### Создав свою виртуальную среду:

1. Клонировать репозиторий:
```bash
git clone https://github.com/VinoStudio/workmate_test.git
```
```bash
cd [repo-directory]
```

2. Создать виртуальную среду:
```bash
python -m venv .venv
```

3. Активировать виртуальную среду:
```bash
source .venv/bin/activate
```

4. Установить зависимости:
```bash
pip install uv && uv sync
```

5. Запустить скрипт в виртуальной среде:
```bash
python main.py --file log_examples/example1.log log_examples/example2.log --report average
```

5. Запустить тесты в виртуальной среде:
```bash
pytest
```

### Использовать образ с Docker:

- Быстрый вариант:
###### Создаёт образ с python, устанавливает зависимости, запускает скрипт, удаляет образ и контейнер:
```bash
make all
```

- Вручную:

1. Запустить скрипт:
```bash
make run_script
```

2. Запустить тесты:
```bash
make test
```

3. Очистить образ и контейнер:
```bash
make clean
```

### Либо можно запустить файлы через bash в docker контейнере:
```bash
make shell
```
- Внутри shell:
```bash
python main.py --file log_examples/example1.log log_examples/example2.log --report average
```


## Особенности:

- Если понадобится добавить новый тип отчета, то следует создать его в директории reports/ и зарегистрировать в `report_manager_creator.py`
- Для расширения функционала скрипта можно добавить новый тип анализа в `parser_creator.py`. Саму фильтрацию можно реализовать в `core/filters.py`
- Если потребуется добавить путь до папки с логами, то нужно передать абсолютный путь в log_examples/file_path.py. 
Для работы с несколькими деректориями, потребуется самостоятельно прописывать пути под флагом `--file` для каждого лог-файла.
- Скрипт поддерживает флаги:
    - `--file` - путь к лог-файлу
    - `--report`: 'average' - среднее значение, 'endpoint_report' - отчет по точкам
    - `--date` [%Y-%d-%m] - фильтрация по дате
