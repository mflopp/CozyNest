from sqlalchemy.orm import Session
import logging
from models.addresses import Country
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import add_record
from ...utils import throw_error


def create_country(data: dict, session: Session) -> Country:
    """
    Creates a new country record in the database.

    Args:
        data (dict): Data for creating the record. Expected key: "name".
        session (Session): SQLAlchemy session for database operations.

    Returns:
        Country: The newly created country record.

    Raises:
        ValueError: If validation fails for the provided data.
    """
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Country,
                data=data,
                required_fields=required_fields,
                unique_fields=required_fields
            )

            # Create a new Country object using the validated data
            new_country = Country(name=data['name'])

            # Attempt to add the record
            result, status_code = add_record(
                session=session,
                record=new_country,
                entity="Country"
            )

            # Log the successful creation with the correct object reference
            if status_code == 200:
                logging.info(
                    f"Country successfully created with ID: {new_country.id}"
                )
                return new_country

            return throw_error(
                500,
                f"Failed to create country '{new_country.name}'."
            )
    except Exception as e:
        logging.error(f"Unexpected error during region creation: {e}")
        raise
