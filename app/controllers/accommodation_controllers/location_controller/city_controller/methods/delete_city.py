import logging
from sqlalchemy.orm import Session

from controllers.general_controllers import delete_record
from .get_city import get_city
from ...utils import throw_error


def delete_city(id: int, session: Session):
    """
    Deletes a City by its ID from the database.

    Args:
        id (int): The ID of the city to delete.
        session (Session): SQLAlchemy session object.

    Returns:
        dict: Response indicating successful deletion.

    Raises:
        404 Not Found: If the City is not found.
        500 Internal Server Error: If database operation fails.
    """
    # Attempt to fetch the record
    city = get_city(field='id', value=id, session=session)

    # Attempt to delete the record
    result, status_code = delete_record(
        session=session,
        record=city,
        entity_name="Region"
    )

    # Log the successful deletion
    if status_code == 200:
        logging.info(
            f"Record with ID: {city.id} was successfully deleted."
        )

        return result
    throw_error(
        500,
        f"Failed to delete record '{city.name}'."
    )
