from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import AccommodationAmenity
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info
from .get_one import fetch_accommodation_amenity


def update_accommodation_amenity(id: int, data: dict, session: Session):
    log_info('Accommodation Amenity updating started...')
    try:

        # Chech if Accommodation Amenity update data exists
        if not ('accommodation_id' in data or 'amenity_id' in data):
            raise ValueError(
                f"Not enough data to update Accommodation Amenity {id}"
            )

        accommodation_id_new = data.get('accommodation_id')
        amenity_id_new = data.get('amenity_id')

        with session.begin_nested():
            acc_amenity_current = fetch_accommodation_amenity(
                'id',
                id,
                session,
                True
            )

            if not accommodation_id_new:
                accommodation_id_new = acc_amenity_current.accommodation_id
            else:
                Validator.validate_id(accommodation_id_new)
            if not amenity_id_new:
                amenity_id_new = acc_amenity_current.amenity_id
            else:
                Validator.validate_id(amenity_id_new)

            new_data = {
                'accommodation_id': accommodation_id_new,
                'amenity_id': amenity_id_new
            }

            Validator.validate_uniqueness(
                session=session,
                Model=AccommodationAmenity,
                criteria=new_data
            )
            log_info(
                "Validations succesfully passed! "
                "(trying to update an acommodation amenity)"
            )

            Recorder.update(session, acc_amenity_current, new_data)

        log_info(f"Accommodation Amenity with ID {id} successfully updated.")

    except (
        NoRecordsFound, ValidationError, ValueError,
        SQLAlchemyError, Exception
    ):
        raise
