import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models.addresses import Country

from ...utils import throw_error


def get_countries(session: Session) -> List[Country]:
    """
    Retrieves a list of all countries from the database.

    Args:
        session (Session): SQLAlchemy session object.

    Returns:
        List[Country]: List of Country records.

    Raises:
        404 Not Found: If no countries are found in the database.
        500 Internal Server Error: If database query fails.
    """
    try:
        # Query all countries
        countries = session.query(Country).all()

        # Check if no countries are found
        if not countries:
            throw_error(404, "No countries found in the database.")

        # Log number of countries found
        logging.info(
            f"{len(countries)} countries found in the database."
        )
        return countries
    except SQLAlchemyError as e:
        throw_error(500, f"Database error while fetching countries: {e}")
    except Exception as e:
        throw_error(500, f"Unexpected error: {e}")
