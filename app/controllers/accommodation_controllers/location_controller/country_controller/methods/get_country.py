import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Country
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound


def get_country(id: int, session: Session) -> Country:
    try:
        Validator.validate_id(id)

        # Retrieve the record
        country = Finder.fetch_record(
            session=session,
            Model=Country,
            criteria={'id': id}
        )

        if country:
            return country

        raise NoRecordsFound

    except NoRecordsFound as e:
        logging.error(
            {f"No Records Found occurred while fetching Country: {e}"},
            exc_info=True
        )
        raise

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while fetching Country: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"DB error occurred while fetching Country: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while fetching Country: {e}"},
            exc_info=True
        )
        raise
