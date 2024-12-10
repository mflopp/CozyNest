import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region
from ...country_controller import CountryController
from utils import (
    Validator,
    ValidationError,
    Recorder
)


def create_region(data: dict, session: Session) -> Region:
    try:
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name', 'country_id']

            # Validate the input data to ensure it meets the model requirements
            Validator.validate_required_fields(required_fields, data)

            name = data['name']

            Validator.validate_unique_field(session, Region, 'name', name)
            Validator.validate_name(name)

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
            Recorder.add(session, new_region)

            return new_region

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while creating: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while creating: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while creating: {e}"},
            exc_info=True
        )
        raise
