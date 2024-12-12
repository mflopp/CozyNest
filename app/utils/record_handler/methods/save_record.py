import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any


def save_record(session: Session, record: Type[Any]) -> None:
    try:
        with session.begin_nested():
            session.add(record)
            session.flush()

        logging.info("Record saved to database session successfully.")
    except SQLAlchemyError as e:
        logging.error(f"Failed to save record: {str(e)}")
        raise e
