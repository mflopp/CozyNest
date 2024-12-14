import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Country
from utils import Validator, Recorder
from utils.error_handler import ValidationError


def create_country(data: Dict, session: Session) -> Country:
    try:
        with session.begin_nested():
            field = 'name'
            Validator.validate_required_field(field, data)

            name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Country,
                criteria={field: name}
            )

            Validator.validate_name(name)

            logging.info('Given country name passed all validations!')

            new_country = Country(name=name)
            if not new_country:
                raise SQLAlchemyError('Country creation error')

            logging.info('Country object succesfully initialized!')

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
