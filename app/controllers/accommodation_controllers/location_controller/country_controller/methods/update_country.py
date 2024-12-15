import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Country
from .get_country import get_country

from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound


def update_country(country_id: int, data: dict, session: Session) -> Country:
    try:
        logging.info(f"Country with ID {country_id} updating started.")
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            Validator.validate_id(country_id)

            # Validate the input data to ensure it meets the model requirements
            field = 'name'
            Validator.validate_required_field(field, data)

            new_name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Country,
                criteria={field: new_name}
            )

            Validator.validate_name(new_name)

            # Fetch the existing record
            country = get_country(country_id, session)
            # Attempt to update the record
            Recorder.update(session, country, {field: new_name})

        logging.info(f"Country with ID {country_id} successfully updated.")
        return country

    except NoRecordsFound as e:
        logging.error(
            {f"No records found for updating: {e}"},
            exc_info=True
        )
        raise

    except ValidationError as e:
        logging.error(
            f"Validation Error occured while updating: {e}",
            exc_info=True
        )
        raise

    except ValueError as e:
        logging.error(
            f"Value Error occured while updating: {e}",
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while updating: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected error occured while updating: {e}",
            exc_info=True
        )
        raise
