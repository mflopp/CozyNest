import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from controllers.controller_utils import fetch_records
from models import Region


def get_regions(session: Session) -> List[Region]:
    """
    Fetches all regions from the database.

    Args:
        session (Session): The database session.

    Returns:
        List[Region]: A list of Region objects.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        # Query all regions
        regions = fetch_records(session, Region, 'Region')

        # Log the number of countries found
        regions_count = len(regions)
        if regions_count:
            logging.info(f"{regions_count} regions found in the database.")
        else:
            logging.info("No regions found in the database.")

        return regions
    except SQLAlchemyError:
        logging.error(
            "Database error occurred while fetching regions.",
            exc_info=True
        )
        raise
