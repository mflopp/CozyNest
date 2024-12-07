import logging
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)

def update_record(session: Session, record, new_data: dict, entity: str):
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

            # Update the fields of the country record
            for field, value in new_data.items():
                if hasattr(record, field):
                    setattr(record, field, value)
                    
            session.flush()

            log_message = f"{record.id} successfully updated from {entity}"
            success_message = f"{entity} was updated."

        logging.info(log_message)
        return {"message": success_message, "id": record.id}, 200
    except Exception as e:
        error_message = f"Failed to update record from {entity}"
        logging.error(f"{error_message}: {str(e)}")
        raise Exception (f"error: {error_message}, details: {str(e)}")
