import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from controllers.controller_utils import fetch_records
from models.addresses import Country


def get_countries(session: Session) -> List[Country]:
    try:
        # Query all countries
        countries = fetch_records(session, Country, 'Country')

        # Log the number of countries found
        if countries:
            logging.info(f"{len(countries)} countries found in the database.")
        else:
            logging.info("No countries found in the database.")
        return countries
    except SQLAlchemyError:
        logging.error(
            "Error while retrieving countries from the database.",
            exc_info=True
        )
        raise
