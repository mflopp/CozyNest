from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

from models.addresses import Region

from ...utils import throw_error


def get_regions(session: Session) -> list[str]:
    """
    Retrieves a list of all regions from the database.

    Args:
        session (Session): SQLAlchemy session object.

    Returns:
        list[str]: List of region names.

    Raises:
        404 Not Found: If no regions are found in the database.
        500 Internal Server Error: If database query fails.
    """
    try:
        # Query all countries
        regions = session.query(Region).all()

        # Check if no countries are found
        if not regions:
            throw_error(404, "No Regions found in the database.")

        # Log number of regions found
        logging.info(
            f"{len(regions.id)} regions found in the database."
        )
        return regions
    except SQLAlchemyError as e:
        throw_error(500, f"Database error while fetching regions: {e}")
    except Exception as e:
        throw_error(500, f"Unexpected error: {e}")
