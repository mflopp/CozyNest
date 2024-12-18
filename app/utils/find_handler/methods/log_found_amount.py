from typing import List, Any
from utils.error_handler import NoRecordsFound
from utils.logs_handler import log_info, log_err


def log_found_amount(records: List[Any]) -> None:
    records_count = len(records)

    if records_count:
        log_info(f"{records_count} records found in the database.")
    else:
        log_err("No records found in the database.")
        raise NoRecordsFound
