import logging
from sqlalchemy.orm import Session

from models.addresses import Address
from controllers.controller_utils.validate_handler import validate_data
from controllers.general_controllers import add_record
from city_controller import CityController
from ...utils import throw_error


def create_address(data: dict, session: Session) -> Address:
    try:
        with session.begin_nested():
            # Define required and unique fields for validation
            required_fields = [
                'city_id',
                'street', 'building', 'apartment',
                'zip_code',
                'latitude', 'longtitude'
            ]

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Address,
                data=data,
                required_fields=required_fields,
            )

            # Fetch the region data
            region = CityController.get_one_by_id(
                city_id=data['city_id'],
                session=session
            )

            # Create a new City object
            new_address = Address(
                region_id=region.id,
                name=data['name']
            )

            # Attempt to add the record
            result, status_code = add_record(
                session=session,
                record=new_address,
                entity="Address"
            )

            # Log the successful creation with the correct object reference
            if status_code == 200:
                logging.info(
                    f"Address successfully created with ID: {new_address.id}"
                )
                return new_address
            throw_error(
                500,
                f"Failed to create address '{new_address}'."
            )
    except Exception as e:
        logging.error(f"Unexpected error during address creation: {e}")
        raise
