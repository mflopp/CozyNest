import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any

from .save_record import save_record


def add_record(session: Session, record: Type[Any]):
    try:
        if not record:
            raise ValueError('There is no record to save')

        # Get entityname from Model arguments
        entity = record.__tablename__
        if not entity:
            raise ValueError('Record has no tablename')

        with session.begin_nested():
            logging.info('Starting saving data')
            save_record(session, record)

        message = f"Record successfully created in {entity}: {record.id}"
        logging.info(message)

    except SQLAlchemyError as e:
        error_message = f"Failed to create {record} in {entity}"
        logging.error(f'{error_message}: {str(e)}')
        raise
