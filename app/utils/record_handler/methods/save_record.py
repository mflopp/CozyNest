from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any

from utils.logs_handler import log_info, log_err


def save_record(session: Session, record: Type[Any]) -> None:
    log_info('Saving record started')
    try:
        with session.begin_nested():
            session.add(record)
            session.flush()

        log_info("Record saved to database session successfully.")
    except SQLAlchemyError as e:
        log_err(f"Failed to save record: {str(e)}")
        raise e
