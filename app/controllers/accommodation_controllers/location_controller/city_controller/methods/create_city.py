import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City
from ...region_controller import RegionController
from utils import (
    Validator,
    ValidationError,
    Recorder
)


def create_city(data: dict, session: Session) -> City:
    try:
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name', 'region_id']

            # Validate the input data to ensure it meets the model requirements
            Validator.validate_required_fields(required_fields, data)

            name = data['name']
            region_id = data['region_id']

            Validator.validate_unique_field(session, City, 'name', name)
            Validator.validate_name(name)
            Validator.validate_id(region_id)

            # Fetch the region data
            region = RegionController.get_one_by_id(region_id, session)

            # Create a new City object
            new_city = City(region.id, name)

            # Attempt to add the record
            Recorder.add(session, new_city)

            return new_city

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
