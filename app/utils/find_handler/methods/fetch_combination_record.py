import logging
from sqlalchemy.orm import Session
from typing import Any, Type, Dict

from sqlalchemy.exc import SQLAlchemyError


def fetch_combination_record(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any]
) -> Any:
    try:
        # Get the name of the model for logging purposes
        model_name = Model.__name__

        record = session.query(Model).filter_by(**criteria).first()
        if not record:
            logging.warning(f'No {model_name} record found where: {criteria}')
            return None

        # Log the ID of the fetched record if it exists
        logging.info(f"{model_name} found with ID {record.id}")
        return record

    except SQLAlchemyError as e:
        # Improved logging with detailed database context
        data = f"{model_name} with '{criteria}': {e}"
        msg = f"Error occurred while fetching: {data}."
        # Raise exception to handle upstream
        raise SQLAlchemyError(msg)
