from sqlalchemy.orm import Session
import logging
from models.addresses import Country
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import update_record
from ...utils import throw_error
from .get_country import get_country

def update_country(country_id: int, data: dict, session: Session) -> Country:
    """
    Updates an existing country record in the database.

    Args:
        country_id (int): ID of the country to update.
        data (dict): Data for updating the record. Expected key: "name".
        session (Session): SQLAlchemy session for database operations.

    Returns:
        Country: The updated country record.

    Raises:
        werkzeug.exceptions.HTTPException: If validation fails or the country is not found.
    """
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Fetch the existing country record
            country = get_country(field='id', value=country_id, session=session)

            # Define fields for validation
            required_fields = ['name']
            unique_fields = ['name']
            print(f"\033[34m ############# BEGINNIG: {country}\033[0m")

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Country,
                data=data,
                required_fields=required_fields,
                unique_fields=unique_fields
            )
            print("\033[34m ############# after validation: \033[0m")

            # Attempt to update the record
            result = update_record(
                session=session,
                record=country,
                new_data=data,
                entity="Country"
            )
            print(f"\033[34m ############# after update: {result}\033[0m")
        return result
    except Exception as e:
        logging.error(f"Unexpected error during country update: {e}")
        return {"Unexpected error during country update. Check logs for details"}, 500

