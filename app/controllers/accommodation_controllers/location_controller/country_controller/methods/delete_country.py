from sqlalchemy.orm import Session
import logging
from controllers.general_controllers import delete_record
from .get_country import get_country


def delete_country(id: int, session: Session):
    """
    Deletes a country by its ID from the database.

    Args:
        id (int): The ID of the country to delete.
        session (Session): SQLAlchemy session object.

    Returns:
        dict: Response indicating successful deletion.

    Raises:
        404 Not Found: If the country is not found.
        500 Internal Server Error: If database operation fails.
    """
    try:

        with session.begin_nested():
            # Attempt to fetch the country
            country = get_country(field='id', value=id, session=session)
            # Attempt to delete the record
            result = delete_record(
                session=session,
                record=country,
                entity="Country"
            )

        session.flush()
        logging.info(f"Successfully deleted country with id={id}.")
        return result

    except ValueError as ve:
        logging.error(f"Deletion error: {ve}", exc_info=True)
        raise

    except Exception as e:
        logging.error(
            f"Unexpected error during deleting: {e}",
            exc_info=True
        )
        raise
