from sqlalchemy.orm import Session
from typing import Type, Any, Dict

from utils.logs_handler import log_info, log_err


def update_record(session: Session, record: Type[Any], new_data: Dict):
    log_info("Record updating started!")
    try:
        # Attempt to delete the record
        with session.begin_nested():

            # Update the fields of the country record
            for field, value in new_data.items():
                if hasattr(record, field):
                    setattr(record, field, value)

            session.flush()

        log_info("Record successfully updated")

    except Exception as e:
        log_err(f"Failed to update record: {str(e)}")
        raise
