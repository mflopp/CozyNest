import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Country
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound


def get_countries(session: Session) -> List[Country]:
    try:
        # Query all countries
        countries = Finder.fetch_records(session, Country)

        # Log the number of countries found
        countries_count = len(countries)
        if countries_count:
            logging.info(f"{countries_count} countries found in the database.")
        else:
            raise NoRecordsFound

        return countries

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
