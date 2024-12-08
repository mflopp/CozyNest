import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from controllers.controller_utils import fetch_records
from models import Country


def get_countries(session: Session) -> List[Country]:
    """
    Fetches all countries from the database.

    Args:
        session (Session): The database session to use for fetching data.

    Returns:
        List[Country]: A list of Country objects.

    Raises:
        SQLAlchemyError: If an error occurs during the database query.
    """
    try:
        # Query all countries
        countries = fetch_records(session, Country, 'Country')

        # Log the number of countries found
        countries_count = len(countries)
        if countries_count:
            logging.info(f"{countries_count} countries found in the database.")
        else:
            logging.info("No countries found in the database.")

        return countries
    except SQLAlchemyError:
        logging.error(
            "Database error occurred while fetching countries.",
            exc_info=True
        )
        raise
