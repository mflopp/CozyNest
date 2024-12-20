from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import AccommodationAmenity
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from .parse_full_accommodation_amenity import parse_full_accommodation_amenity
from utils.logs_handler import log_info, log_err
from ...amenity_controller import AmenityController
# from ...accommodation_controller import AccommodationController


def add_accommodation_amenity(
    user_data: Dict,
    session: Session
) -> Dict[str, Any]:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            fields = ['accommodation_id', 'amenity_id']

            Validator.validate_required_fields(fields, user_data)

            accommodation_id = user_data.get('accommodation_id')
            amenity_id = user_data.get('amenity_id')
            Validator.validate_id(accommodation_id)
            Validator.validate_id(amenity_id)

            Validator.validate_uniqueness(
                session=session,
                Model=AccommodationAmenity,
                criteria={
                    'accommodation_id': accommodation_id,
                    'amenity_id': amenity_id
                }
            )

            log_info(
                "Validations succesfully passed! "
                "(trying to create an Accommodation Amenity)"
            )

            amenity = AmenityController.get_one_by_id(
                amenity_id=amenity_id,
                session=session,
                return_instance=True
            )

            accommodation = AccommodationController.get_one_by_id(
                accommodation_id=accommodation_id,
                session=session,
                return_instance=True
            )

            new_accommodation_amenity = AccommodationAmenity(
                amenity_id=amenity.id,
                accommodation_id=accommodation.id
            )
            if not new_accommodation_amenity:
                log_err(
                    "add_accommodation_amenity(): Accommodation Amenity was "
                    "not created for some reason"
                )
                raise SQLAlchemyError

            Recorder.add(session, new_accommodation_amenity)

        log_info('Accommodation Amenity creation successfully finished')
        return parse_full_accommodation_amenity(new_accommodation_amenity)

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
