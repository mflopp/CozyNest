import logging
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)


def del_record(session, record, entity_name):
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

        session.delete(record)
        session.commit()
        log_message = f"{record.id} successfully deleted in {entity_name}."
        message = f"{entity_name} was deleted!"

        logging.info(log_message)
        return {'message': message, 'id': record.id}, 200
    except Exception as e:
        session.rollback()
        message = f"Failed to delete {record} in {entity_name}"
        logging.error(f'{message}: {str(e)}')
        return {'error': message, 'details': str(e)}, 500


def delete_record(session: Session, record, entity: str):
    """
    Deletes a record from the database and logs the operation.

    Args:
        session (Session): SQLAlchemy session object.
        record (object): SQLAlchemy model instance to delete.
        entity (str): Name of the entity for logging.

    Returns:
        dict: Success or error response with appropriate HTTP status code.
    """
    try:
        if not record:
            error_message = f"Record not found in {entity}"
            logging.error(error_message)
            return {"error": error_message}, 404

        # Attempt to delete the record
        with session.begin_nested():
            session.delete(record)
            session.commit()

            log_message = f"{record.id} successfully deleted from {entity}"
            success_message = f"{entity} was deleted."

            logging.info(log_message)
            return {"message": success_message, "id": record.id}, 200
    except Exception as e:
        error_message = f"Failed to delete record from {entity}"
        logging.error(f"{error_message}: {str(e)}")
        return {"error": error_message, "details": str(e)}, 500
