from sqlalchemy.orm import Session
import logging

from models.addresses import Country
from controllers.controller_utils import get_first_record_by_criteria
from controllers.general_controllers import delete_record

from ...utils import throw_error


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
    # Attempt to fetch the country
    country = get_first_record_by_criteria(
        session=session,
        Model=Country,
        filter_criteria={"id": id}
    )

    # If the country doesn't exist, abort with 404
    if not country:
        throw_error(404, f"Country with id={id} not found.")

    # Attempt to delete the record
    result = delete_record(
        session=session,
        record=country,
        entity_name="Countries"
    )

    if result[1] != 200:  # If deletion failed
        throw_error(500, "Failed to delete the country.")

    logging.info(f"Successfully deleted country with id={id}.")
    return result
