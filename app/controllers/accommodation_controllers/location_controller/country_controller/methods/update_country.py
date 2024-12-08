from sqlalchemy.orm import Session
import logging
from models.addresses import Country
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import update_record
from .get_country import get_country


def update_country(country_id: int, data: dict, session: Session) -> Country:
    """
    Updates an existing country record in the database.

    Args:
        country_id (int): The ID of the country to update.
        data (dict): The new data for the country. Must include required
                     fields.
        session (Session): SQLAlchemy session for database operations.

    Returns:
        Optional[Country]: The updated Country object if successful.

    Raises:
        ValueError: If validation fails or the record does not exist.
        Exception: For unexpected errors during the update process.
    """
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Define fields for validation
            fields = ['name']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Country,
                data=data,
                required_fields=fields,
                unique_fields=fields
            )

            # Fetch the existing country record
            country = get_country('id', country_id, session)

            # Attempt to update the record
            result = update_record(
                session=session,
                record=country,
                new_data=data,
                entity="Country"
            )

        logging.info(f"Country with ID {country_id} successfully updated.")
        return result
    except ValueError as ve:
        logging.warning(f"Validation or record error: {ve}")
        raise
    except Exception as e:
        logging.error(
            f"Unexpected error during country update: {e}", exc_info=True
        )
        raise
