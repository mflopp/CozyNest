import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import Region
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_region import parse_full_region

ERR_MSG = "Error occurred while fetching Region record"
TRACEBACK = True


def get_region(id: int, session: Session) -> Dict[str, Any]:
    try:
        Validator.validate_id(id)

        # Retrieve the record
        region = Finder.fetch_record(
            session=session,
            Model=Region,
            criteria={'id': id}
        )

        if region:
            return parse_full_region(region)

        raise NoRecordsFound

    except NoRecordsFound as e:
        logging.error(e, exc_info=TRACEBACK)
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
