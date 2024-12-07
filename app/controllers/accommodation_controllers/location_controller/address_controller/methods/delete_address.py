import logging
from sqlalchemy.orm import Session

from controllers.general_controllers import delete_record
from .get_address import get_address
from ...utils import throw_error


def delete_address(id: int, session: Session):
    """
    Deletes a address by its ID from the database.

    Args:
        id (int): The ID of the address to delete.
        session (Session): SQLAlchemy session object.

    Returns:
        dict: Response indicating successful deletion.

    Raises:
        404 Not Found: If the address is not found.
        500 Internal Server Error: If database operation fails.
    """
    # Attempt to fetch the record
    address = get_address(field='id', value=id, session=session)

    # Attempt to delete the record
    result, status_code = delete_record(
        session=session,
        record=address,
        entity_name="Address"
    )

    # Log the successful deletion
    if status_code == 200:
        logging.info(
            f"Record with ID: {address.id} was successfully deleted."
        )

        return result
    throw_error(
        500,
        f"Failed to delete record '{address}'."
    )
