import logging
from sqlalchemy.orm import Session
from typing import Any, Type

from sqlalchemy.exc import SQLAlchemyError
from .filter_handler import set_filter_criteria
from .get_first_record import get_first_record_by_criteria


def fetch_record(session: Session, Model: Type[Any],
                 field: str, value: Any) -> Any:
    try:
        # Get the name of the model for logging purposes
        model_name = Model.__name__

        # Set dynamic filter criteria based on the given field and value
        criteria = set_filter_criteria(field, value)
        if criteria:
            logging.warning(f'Criteria: {criteria}')

        # Fetch the first matching record
        record = get_first_record_by_criteria(session, Model, criteria)

        # Log if no record is found
        if not record:
            logging.info(
                f"No {model_name} record found where '{field}'='{value}'"
            )
            return None

        # Log the ID of the fetched record if it exists
        logging.info(f"{model_name} found with ID {record.id}")
        return record

    except SQLAlchemyError as e:
        # Improved logging with detailed database context
        data = f"{model_name} with '{field}'='{value}': {e}"
        logging.error(
            f"Error occurred while fetching {data}"
        )
        # Raise exception to handle upstream
        raise
