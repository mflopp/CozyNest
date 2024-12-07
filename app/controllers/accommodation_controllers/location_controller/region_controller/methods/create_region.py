from sqlalchemy.orm import Session
from models.addresses import Region
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import add_record
from country_controller import CountryController
import logging
from ...utils import throw_error


def create_region(data: dict, session: Session) -> Region:
    """
    Create a new region in the database after validating the data
    and ensuring the country exists.

    Args:
        data (dict): Input data containing region information.
        session (Session): Database session for transaction management.

    Returns:
        Region: The created region entity.

    Raises:
        400 Bad Request: If validation fails.
        404 Not Found: If the country doesn't exist.
        500 Internal Server Error: For database-related issues.
    """
    try:
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name', 'country_id']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Region,
                data=data,
                required_fields=required_fields,
                unique_fields=["name"]
            )

            # Fetch the country data
            country = CountryController.get_one_by_id(
                country_id=data['country_id'],
                session=session
            )

            # Create a new Region object
            new_region = Region(
                country_id=country.id,
                name=data['name']
            )

            # Attempt to add the record
            result, status_code = add_record(
                session=session,
                record=new_region,
                entity="Region"
            )

            # Log the successful creation with the correct object reference
            if status_code == 200:
                logging.info(
                    f"Region successfully created with ID: {new_region.id}"
                )
                return new_region
            throw_error(
                500,
                f"Failed to create region '{new_region.name}'."
            )
    except Exception as e:
        logging.error(f"Unexpected error during region creation: {e}")
        raise
