import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.addresses import Address
from controllers.controller_utils import fetch_record
from ...utils import throw_error, set_filter_criteria
from ...validations import validate_id, validate_field, validate_value


def get_address(field: str, value: any, session: Session) -> Address:
    """
    Retrieves a address record from the database by 'id' or 'name'.

    Args:
        field (str): The name of the field to filter by ('id' or 'name').
        value (any): The value of the field to filter by.
        session (Session): The SQLAlchemy session object for DB interaction.

    Returns:
        Address: The retrieved address record.

    Raises:
        400 Bad Request: If the field or value is invalid.
        404 Not Found: If no address is found with the given field and value.
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
        address = fetch_record(
            session=session,
            Model=Address,
            criteria=filter_criteria,
            model_name='Address'
        )

        return address

    except SQLAlchemyError as e:
        throw_error(
            500,
            f"DB error occurred while querying address by {field}: {e}"
        )

    except Exception as e:
        throw_error(
            500,
            f"Unexpected error while processing the request: {e}"
        )
