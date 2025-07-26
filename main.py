import asyncio
from tabulate import tabulate

from core.exceptions import LogFileNotFoundError, ReportNotFoundError, InvalidDateError
from core.log_processor import LogProcessor
from core.log_reader import LogFileReader
from core.parser_creator import create_parser
from core.report_manager_creator import create_report_manager
from log_examples.file_path import FILE_PATH


async def main():
    try:
        # register reports and create parser
        report_builders = create_report_manager()
        parser = create_parser(report_builders)
        args = parser.parse_args()

        # create log reader and read logs
        log_reader = LogFileReader()
        logs_generator = log_reader.read_files(files=args.file, file_path=FILE_PATH)
        logs = [log async for log in logs_generator]

        # create log processor to filter logs
        processor = LogProcessor()
        processed_logs = processor.process_logs(logs, args.date)

        # build report
        report_class = report_builders.get_report(args.report)
        report = report_class()
        report_data = report.build(processed_logs)

        # print report
        if report_data:
            print(tabulate(report_data, headers="keys", tablefmt="grid"))
        else:
            print("Нет данных для отчета")

    except LogFileNotFoundError as e:
        print(e.message)

    except ReportNotFoundError as e:
        print(e.message)

    except InvalidDateError as e:
        print(e.message)


if __name__ == "__main__":
    asyncio.run(main())
