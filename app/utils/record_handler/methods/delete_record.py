from sqlalchemy.orm import Session
from typing import Type, Any
from utils.logs_handler import log_err, log_info


def delete_record(session: Session, record: Type[Any]):
    log_info('Deletion record started.')
    try:
        entity = record.__tablename__
        with session.begin_nested():
            session.delete(record)
            session.flush()

        log_info(f"{record.id} successfully deleted from {entity}")

    except Exception as e:
        msg = f"Failed to delete record with ID = {record.id} from {entity}"
        log_err(f"delete_record(): {msg} - {str(e)}")
        raise
