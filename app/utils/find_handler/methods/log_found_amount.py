import logging
from typing import List, Any
from utils.error_handler import NoRecordsFound


def log_found_amount(records: List[Any]) -> None:
    """
    Logs the number of records found in the database.

    Args:
        records (List[Any]): A list of records retrieved from the database.

    Raises:
        NoRecordsFound: If no records are found in the list.
    """
    records_count = len(records)

    if records_count:
        logging.info(f"{records_count} records found in the database.")
    else:
        logging.info("No records found in the database.")
        raise NoRecordsFound
