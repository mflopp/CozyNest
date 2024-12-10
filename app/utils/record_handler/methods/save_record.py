import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any


def save_record(session: Session, record: Type[Any]) -> None:
    """
    Saves a record to the database session and commits the transaction.

    Args:
        session (Session): The database session to use for the operation.
        record (object): The record to save.

    Raises:
        SQLAlchemyError: If an error occurs while saving the record.
    """
    try:
        with session.begin_nested():
            session.add(record)
            session.flush()

        logging.info("Record saved to database session successfully.")
    except SQLAlchemyError as e:
        logging.error(f"Failed to save record: {str(e)}")
        raise e
