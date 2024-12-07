import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Address
from ...utils import throw_error


def get_addresses(session: Session) -> list[str]:
    """
    Retrieves a list of all addresses from the database.

    Args:
        session (Session): SQLAlchemy session object.

    Returns:
        list[str]: List of region names.

    Raises:
        404 Not Found: If no addresses are found in the database.
        500 Internal Server Error: If database query fails.
    """
    try:
        # Query all addresses
        addresses = session.query(Address).all()

        # Check if no addresses are found
        if not addresses:
            throw_error(404, "No addresses found in the database.")

        # Log number of addresses found
        logging.info(
            f"{len(addresses.id)} addresses found in the database."
        )
        return addresses
    except SQLAlchemyError as e:
        throw_error(500, f"Database error while fetching addresses: {e}")
    except Exception as e:
        throw_error(500, f"Unexpected error: {e}")
