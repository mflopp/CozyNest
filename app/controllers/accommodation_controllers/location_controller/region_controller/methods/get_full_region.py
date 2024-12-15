import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from .get_region import get_region
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while fetching Region record"
TRACEBACK = True


def get_full_region(id: int, session: Session) -> Dict:
    try:
        # Retrieve the record
        region = get_region(id, session)

        full_record = {
            'id': region.id,
            'name': region.name,
            'country': region.country
        }

        return full_record

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
