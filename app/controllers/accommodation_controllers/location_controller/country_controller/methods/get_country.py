import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from typing import Any

from models import Country

from controllers.controller_utils import fetch_record

from ...utils import set_filter_criteria
from ...validations import validate_id, validate_field, validate_value


def get_country(field: str, value: Any,
                session: Session) -> Country:
    """
    Retrieves a country record from the database by 'id' or 'name'.

    Args:
        field (str): The name of the field to filter by ('id' or 'name').
        value (any): The value of the field to filter by.
        session (Session): The SQLAlchemy session object for DB interaction.

    Returns:
        Country: The retrieved country record.

    Raises:
        400 Bad Request: If the field or value is invalid.
        404 Not Found: If no country is found with the given field and value.
        500 Internal Server Error: For any other errors.
    """
    valid_fields = {'id', 'name'}

    validate_field(field, valid_fields)
    validate_value(value, field)
    validate_id(value, field)

    try:
        # Build filter criteria
        filter_criteria = set_filter_criteria(field, value)

        # Retrieve the record
        country = fetch_record(
            session=session,
            Model=Country,
            criteria=filter_criteria,
            model_name='Countries'
        )

        logging.info(f"Successfully fetched Country by {field}='{value}'.")
        return country

    except SQLAlchemyError as e:
        logging.error(
            {f"DB error occurred while fetching Country by {field}: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while processing the request: {e}"},
            exc_info=True
        )
        raise
