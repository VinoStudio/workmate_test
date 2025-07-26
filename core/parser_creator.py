import argparse

from core.interfaces.report_manager import BaseReportManager


def create_parser(registered_reports: BaseReportManager) -> argparse.ArgumentParser:
    """
    Create and return a command-line argument parser

    Args:
        registered_reports (BaseReportManager): An instance of the report manager class

    Returns:
        argparse.ArgumentParser: A command-line argument parser
    """
    parser = argparse.ArgumentParser(description="Command-line log processor")
    parser.add_argument(
        "--file",
        required=True,
        nargs="+",
        type=str,
        help="Path to the log file",
    )
    parser.add_argument(
        "--report",
        choices=registered_reports.get_reports(),
        required=True,
        help="Choose type of report to generate",
    )
    parser.add_argument(
        "--date",
        type=str,
        help="Date to filter logs by. Format: YYYY-MM-DD",
    )

    return parser
