import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region, Country
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from .get_country import get_country

ERR_MSG = "Error occurred while deleting Country record"
TRACEBACK = True


def delete_country(id: int, session: Session):
    logging.info(f"Country with ID {id} updating started.")
    try:
        Validator.validate_id(id)
        with session.begin_nested():
            country: Country = get_country(id, session, True)
            if not country:
                logging.info('No Country to delete')
                raise NoRecordsFound

            if Recorder.has_child(country, Region):
                raise HasChildError

            Recorder.delete(session, country)

    except HasChildError as e:
        logging.error(e, exc_info=TRACEBACK)
        raise

    except NoRecordsFound as e:
        logging.error(f"{ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except ValidationError as e:
        logging.error(f"Validation {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except SQLAlchemyError as e:
        logging.error(f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise

    except Exception as e:
        logging.error(f"Unexpected {ERR_MSG}: {e}", exc_info=TRACEBACK)
        raise
