import logging
from typing import List, Any
from utils.error_handler import NoRecordsFound


def log_found_amount(records: List[Any]) -> None:
    records_count = len(records)

    if records_count:
        logging.info(f"{records_count} records found in the database.")
    else:
        logging.info("No records found in the database.")
        raise NoRecordsFound
