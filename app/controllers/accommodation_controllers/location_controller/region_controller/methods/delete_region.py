from sqlalchemy.orm import Session
import logging

from controllers.general_controllers import delete_record

from .get_region import get_region
from ...utils import throw_error


def delete_region(id: int, session: Session):
    """
    Deletes a Region by its ID from the database.

    Args:
        id (int): The ID of the region to delete.
        session (Session): SQLAlchemy session object.

    Returns:
        dict: Response indicating successful deletion.

    Raises:
        404 Not Found: If the region is not found.
        500 Internal Server Error: If database operation fails.
    """
    # Attempt to fetch the region
    region = get_region(field='id', value=id, session=session)

    # Attempt to delete the record
    result, status_code = delete_record(
        session=session,
        record=region,
        entity_name="Region"
    )

    # Log the successful creation with the correct object reference
    if status_code == 200:
        logging.info(
            f"Region with ID: {region.id} was successfully deleted."
        )

        return result
    throw_error(
        500,
        f"Failed to delete region '{region.name}'."
    )
