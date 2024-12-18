from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any

from utils.logs_handler import log_info, log_err
from .save_record import save_record


def add_record(session: Session, record: Type[Any]):
    log_info("Adding record started")
    try:
        if not record:
            msg = 'No record to save'
            log_err(msg)
            raise ValueError(msg)

        # Get entityname from Model arguments
        entity = record.__tablename__
        if not entity:
            msg = 'Record has no tablename'
            log_err(msg)
            raise ValueError(msg)

        with session.begin_nested():
            save_record(session, record)

        message = f"Record successfully created in {entity}: {record.id}"
        log_info(message)

    except SQLAlchemyError:
        raise
