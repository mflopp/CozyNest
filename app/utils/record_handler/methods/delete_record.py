import logging
from sqlalchemy.orm import Session
from typing import Type, Any


def delete_record(session: Session, record: Type[Any]):
    try:
        entity = record.__tablename__
        logging.info(f'Deletion {record} started!')
        # Attempt to delete the record
        with session.begin_nested():
            session.delete(record)
            session.flush()

        logging.info(f"{record.id} successfully deleted from {entity}")

    except Exception as e:
        error_message = f"Failed to delete record from {entity}"
        logging.error(f"{error_message}: {str(e)}")
        raise
