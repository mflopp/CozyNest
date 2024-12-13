import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Region
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound


def get_regions(session: Session) -> List[str]:
    try:
        # Query all regions
        regions = Finder.fetch_records(session, Region)

        # Log the number of countries found
        Finder.log_found_amount(regions)

        return regions

    except NoRecordsFound as e:
        logging.warning(
            {f"No records found: {e}"},
            exc_info=True
        )
        raise

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while fetching records: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while fetching records: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while fetching records: {e}"},
            exc_info=True
        )
        raise
