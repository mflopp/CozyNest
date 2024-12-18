import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Country
from .get_country import get_country

from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while updating Country record"
TRACEBACK = True


def update_country(country_id: int, data: dict, session: Session) -> Country:
    try:
        logging.info(f"Country with ID {country_id} updating started.")
        with session.begin_nested():
            Validator.validate_id(country_id)

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
            country: Country = get_country(country_id, session, True)
            # Attempt to update the record
            Recorder.update(session, country, {field: new_name})

        logging.info(f"Country with ID {country_id} successfully updated.")
        return country

    except NoRecordsFound as e:
        logging.error(f"{ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except ValidationError as e:
        logging.error(f"Validation {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except ValueError as e:
        logging.error(f"Value {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except SQLAlchemyError as e:
        logging.error(f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except Exception as e:
        logging.error(f"Unexpected {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise
