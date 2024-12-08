import logging
from sqlalchemy.orm import Session
from typing import Dict

from models import Region

from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import add_record
from controllers import CountryController
from utils.api_error import ValidationError


def create_region(data: Dict, session: Session) -> Region:
    """
    Creates a new region in the database after validating the input data.

    Args:
        data (dict): A dictionary containing region details
        (e.g., name, country_id).
        session (Session): SQLAlchemy database session.

    Returns:
        Region: The newly created Region object.

    Raises:
        ValidationError: If the input data is invalid.
        Exception: For unexpected errors during region creation.
    """
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name', 'country_id']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Region,
                data=data,
                required_fields=required_fields,
                unique_fields=["name"]
            )

            # Fetch the country data
            country = CountryController.get_one_by_id(
                country_id=data['country_id'],
                session=session
            )

            # Create a new Region object
            new_region = Region(
                country_id=country.id,
                name=data['name']
            )

            # Attempt to add the record
            add_record(
                session=session,
                record=new_region,
                entity="Region"
            )

            return new_region
    except ValidationError as e:
        logging.warning(f"Validation error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during region creation: {e}")
        raise
