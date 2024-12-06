import logging

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
