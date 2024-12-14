import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Country
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while fetching Country record"


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
        logging.error(e, exc_info=True)
        raise

    except ValidationError as e:
        logging.error(
            f"Validation {ERR_MSG}: {e}", exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            f"Data Base {ERR_MSG}: {e}", exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected {ERR_MSG}: {e}", exc_info=True
        )
        raise
