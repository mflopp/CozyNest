import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from .get_region import get_region
# from controllers import CountryController

from utils.error_handler import ValidationError, NoRecordsFound


def get_full_region(id: int, session: Session) -> Dict:
    try:
        if not isinstance(id, int):
            raise ValidationError("ID must be integer")

        # Retrieve the record
        region = get_region('id', id, session)
        # country = CountryController.get_one_by_id(region.country_id, session)

        full_record = {
            'id': region.id,
            'name': region.name,
            'country': region.country
        }

        return full_record

    except NoRecordsFound as e:
        logging.warning(
            {f"No records found: {e}"},
            exc_info=True
        )
        raise

    except ValidationError as e:
        logging.error(
            {f"Validation Error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise
