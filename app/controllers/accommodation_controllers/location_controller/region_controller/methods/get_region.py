import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while fetching Region record"


def get_region(id: int, session: Session) -> Region:
    try:
        Validator.validate_id(id)

        # Retrieve the record
        region = Finder.fetch_record(
            session=session,
            Model=Region,
            criteria={'id': id}
        )

        if region:
            return region

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
