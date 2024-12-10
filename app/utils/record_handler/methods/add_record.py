import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any

from .save_record import save_record


def add_record(session: Session, record: Type[Any]):
    """
    Adds a record to the database session and commits the transaction.

    Args:
        session (Session): The database session.
        record: The record to be added (must have an 'id' attribute).
        entity (str): The name of the entity (e.g., 'User', 'Order').

    Returns:
        dict: A dictionary containing the status message and record ID
        or error message.
    """
    try:
        # Get entityname from Model arguments
        entity = record.__tablename__

        with session.begin_nested():
            logging.info('Starting saving data')
            save_record(session, record)

        message = f"Record successfully created in {entity}: {record.id}"
        logging.info(message)

        # return {'message': message, 'id': record.id}, 200
    except SQLAlchemyError as e:
        error_message = f"Failed to create {record} in {entity}"
        logging.error(f'{error_message}: {str(e)}')

        raise Exception(f"error: {error_message}, details: {str(e)}")
