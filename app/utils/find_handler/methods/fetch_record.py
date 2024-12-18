from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any, Dict

from utils.logs_handler import log_info


def fetch_one(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any]
) -> Any:
    log_info("Record fetching started")
    try:
        model_name = Model.__name__

        record = session.query(Model).filter_by(**criteria).first()

        if not record:
            log_info(f'No {model_name} record found where: {criteria}')
            return None

        # Log the ID of the fetched record if it exists
        log_info(f"{model_name} found with ID = {record.id}")
        return record

    except SQLAlchemyError:
        raise
        # data = f"{model_name} with '{criteria}': {e}"
        # msg = f"Error occurred while fetching: {data}."
        # raise SQLAlchemyError(msg)
