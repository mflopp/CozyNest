from sqlalchemy.orm import Session
from models.addresses import City
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import add_record
from region_controller import RegionController
import logging
from ...utils import throw_error


def create_city(data: dict, session: Session) -> City:
    try:
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = ['name', 'region_id']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=City,
                data=data,
                required_fields=required_fields,
                unique_fields=["name"]
            )

            # Fetch the region data
            region = RegionController.get_one_by_id(
                region_id=data['region_id'],
                session=session
            )

            # Create a new City object
            new_city = City(
                region_id=region.id,
                name=data['name']
            )

            # Attempt to add the record
            result, status_code = add_record(
                session=session,
                record=new_city,
                entity="City"
            )

            # Log the successful creation with the correct object reference
            if status_code == 200:
                logging.info(
                    f"City successfully created with ID: {new_city.id}"
                )
                return new_city
            throw_error(
                500,
                f"Failed to create city '{new_city.name}'."
            )
    except Exception as e:
        logging.error(f"Unexpected error during city creation: {e}")
        raise
