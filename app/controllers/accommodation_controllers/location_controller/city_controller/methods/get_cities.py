import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.addresses import Region
from ...utils import throw_error


def get_cities(session: Session) -> list[str]:
    """
    Retrieves a list of all cities from the database.

    Args:
        session (Session): SQLAlchemy session object.

    Returns:
        list[str]: List of region names.

    Raises:
        404 Not Found: If no cities are found in the database.
        500 Internal Server Error: If database query fails.
    """
    try:
        # Query all cities
        cities = session.query(Region).all()

        # Check if no cities are found
        if not cities:
            throw_error(404, "No Cities found in the database.")

        # Log number of cities found
        logging.info(
            f"{len(cities.id)} cities found in the database."
        )
        return cities
    except SQLAlchemyError as e:
        throw_error(500, f"Database error while fetching cities: {e}")
    except Exception as e:
        throw_error(500, f"Unexpected error: {e}")
