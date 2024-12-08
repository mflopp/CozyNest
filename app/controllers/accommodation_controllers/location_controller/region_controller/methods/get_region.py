import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from typing import Any

from models import Region

from controllers.controller_utils import fetch_record

from ...utils import set_filter_criteria
from ...validations import validate_id, validate_field, validate_value


def get_region(field: str, value: Any, session: Session) -> Region:
    """
    Fetch a single Region record by a specified field and value.

    Args:
        field (str): The field to filter by (e.g., 'id' or 'name').
        value (Any): The value to match for the specified field.
        session (Session): The SQLAlchemy session to use for querying.

    Returns:
        Region: The retrieved Region record.

    Raises:
        SQLAlchemyError: If a database error occurs during the query.
        Exception: For any unexpected errors.
    """
    valid_fields = {'id', 'name'}

    validate_field(field, valid_fields)
    validate_value(value, field)
    validate_id(value, field)

    try:
        # Build filter criteria
        filter_criteria = set_filter_criteria(field, value)

        # Retrieve the record
        region = fetch_record(
            session=session,
            Model=Region,
            criteria=filter_criteria,
            model_name='Region'
        )

        logging.info(f"Successfully fetched Region by {field}='{value}'.")
        return region

    except SQLAlchemyError as e:
        logging.error(
            {f"DB error occurred while fetching Region by {field}: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while processing the request: {e}"},
            exc_info=True
        )
        raise
