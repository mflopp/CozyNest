import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Country
from utils import Validator, Recorder
from utils.error_handler import ValidationError


def create_country(data: Dict, session: Session) -> Country:
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Validate the input data to ensure it meets the model requirements
            field = 'name'
            Validator.validate_required_field(field, data)

            name = data.get(field)

            Validator.validate_unique_field(session, Country, field, name)
            Validator.validate_name(name)

            logging.info('All validations succesfully passed!')

            # Create a new Country object using the validated data
            new_country = Country(name=name)
            logging.info('Country object succesfully initialized!')

            # Attempt to add the record
            Recorder.add(session, new_country)

        return new_country

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while creating: {e}"},
            exc_info=True
        )
        raise

    except ValueError as e:
        logging.error(
            f"Value Error occured while creating: {e}",
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
