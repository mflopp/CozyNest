from sqlalchemy.orm import Session
import logging

from controllers.general_controllers import delete_record

from .get_region import get_region


def delete_region(id: int, session: Session):
    """
    Deletes a region from the database by its ID.

    Args:
        id (int): The ID of the region to delete.
        session (Session): SQLAlchemy database session.

    Returns:
        bool: True if the region was successfully deleted.

    Raises:
        Exception: If any unexpected error occurs during deletion.
    """
    try:

        with session.begin_nested():
            # Attempt to fetch the country
            region_to_delete = get_region(
                field='id',
                value=id,
                session=session
            )

            # Attempt to delete the record
            result = delete_record(
                session=session,
                record=region_to_delete,
                entity="Region"
            )

        session.flush()
        logging.info(f"Successfully deleted Region with id={id}.")
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
