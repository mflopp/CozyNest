import logging
from sqlalchemy.orm import Session
from typing import Type, Any, Dict


def update_record(session: Session, record: Type[Any], new_data: Dict):
    try:
        logging.info("Record updating started!")
        entity = record.__tablename__

        # Attempt to delete the record
        with session.begin_nested():

            # Update the fields of the country record
            for field, value in new_data.items():
                if hasattr(record, field):
                    setattr(record, field, value)

            session.flush()

            message = f"Record with ID = {record.id} successfully updated"

        logging.info(message)

    except Exception as e:
        error_message = f"Failed to update record from {entity}"
        logging.error(f"{error_message}: {str(e)}")

        raise Exception(f"{error_message}: {str(e)}")
