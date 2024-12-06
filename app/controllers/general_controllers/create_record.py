import logging
from sqlalchemy.orm import Session

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
    session.add(record)
    session.commit()


def add_record(session, record, entity_name):
    """
    Adds a record to the database session and commits the transaction.

    Args:
        session (Session): The database session.
        record: The record to be added (must have an 'id' attribute).
        entity_name (str): The name of the entity (e.g., 'User', 'Product').

    Returns:
        dict: A dictionary containing the status message and record ID
        or error message.
    """
    try:
        save_record(session, record)

        log_message = f"{record.id} successfully created in {entity_name}."
        message = f"{entity_name} was created!"

        logging.info(log_message)
        return {'message': message, 'id': record.id}, 200
    except Exception as e:
        session.rollback()
        message = f"Failed to create {record} in {entity_name}"
        logging.error(f'{message}: {str(e)}')
        return {'error': message, 'details': str(e)}, 500
