import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from .get_region import get_region

ERR_MSG = "Error occurred while deleting"
TRACEBACK = True


def delete_region(id: int, session: Session):
    try:
        Validator.validate_id(id)

        with session.begin_nested():
            region = get_region(id, session)
            if not region:
                logging.info('No Region to delete')
                raise NoRecordsFound

            if Recorder.has_child(region, City):
                raise HasChildError

            Recorder.delete(session, region)

    except HasChildError as e:
        logging.error(e, exc_info=TRACEBACK)
        raise

    except NoRecordsFound as e:
        logging.error(
            f"No records found for deleting: {e}", exc_info=TRACEBACK
        )
        raise

    except ValidationError as e:
        logging.error(
            f"Validation {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise
