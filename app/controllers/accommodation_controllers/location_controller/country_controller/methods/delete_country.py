import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from .get_country import get_country


def delete_country(id: int, session: Session):
    try:
        Validator.validate_id(id)

        with session.begin_nested():
            # Attempt to fetch the country
            country = get_country(field='id', value=id, session=session)
            if not country:
                logging.info('No country to delete')
                raise NoRecordsFound

            if Recorder.has_child(country, Region):
                raise HasChildError

            Recorder.delete(session, country)

    except NoRecordsFound as e:
        logging.error(
            {f"No records found for deleting: {e}"},
            exc_info=True
        )
        raise

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while deleting: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while deleting: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while deleting: {e}"},
            exc_info=True
        )
        raise
