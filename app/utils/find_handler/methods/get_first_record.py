from sqlalchemy.orm import Session
from typing import Any, Optional, Type, Dict
import logging

from sqlalchemy.exc import SQLAlchemyError


def get_first_record_by_criteria(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any]
) -> Optional[Any]:
    try:
        # Get the name of the model for logging purposes
        model_name = Model.__name__

        record = session.query(Model).filter_by(**criteria).first()
        if not record:
            logging.warning(f'Record not found: {criteria}')
        return record

    except SQLAlchemyError as e:
        logging.error(
            f"Unexpected database error while querying {model_name}: {e}"
        )
        return None
