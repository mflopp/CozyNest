import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City


def get_city(field: str, value: any, session: Session) -> City:
    """
    Retrieves a city record from the database by 'id' or 'name'.

    Args:
        field (str): The name of the field to filter by ('id' or 'name').
        value (any): The value of the field to filter by.
        session (Session): The SQLAlchemy session object for DB interaction.

    Returns:
        City: The retrieved city record.

    Raises:
        400 Bad Request: If the field or value is invalid.
        404 Not Found: If no city is found with the given field and value.
        500 Internal Server Error: For any other errors.
    """
    validate_field(field)
    validate_value(value, field)
    validate_id(value, field)

    try:
        # Build filter criteria
        filter_criteria = set_filter_criteria(field, value)
        logging.debug(f"Filter criteria created: {filter_criteria}")

        # Retrieve the record
        city = fetch_record(
            session=session,
            Model=City,
            criteria=filter_criteria,
            model_name='City'
        )

        return city

    except SQLAlchemyError as e:
        throw_error(
            500,
            f"DB error occurred while querying city by {field}: {e}"
        )

    except Exception as e:
        throw_error(
            500,
            f"Unexpected error while processing the request: {e}"
        )
