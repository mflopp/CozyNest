import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(level=logging.INFO)


def save_record(session: Session, record: object) -> None:
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


def add_record(session: Session, record, entity: str):
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
        with session.begin_nested():
            save_record(session, record)

            message = f"Record successfully created in {entity}: {record.id}"
            logging.info(message)

        return {'message': message, 'id': record.id}, 200
    except SQLAlchemyError as e:
        error_message = f"Failed to create {record} in {entity}"
        logging.error(f'{error_message}: {str(e)}')
        return {'error': error_message, 'details': str(e)}, 500
