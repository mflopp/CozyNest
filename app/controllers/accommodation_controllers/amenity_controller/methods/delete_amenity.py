from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import Amenity, AccommodationAmenity

from utils import Recorder
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_amenity import fetch_amenity


def del_amenity(id: int, session: Session):
    log_info(f"Amenity with ID={id} deletion started...")
    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            amenity: Amenity = fetch_amenity(
                'id', id, session, True
            )

            # Check if amenity is in use in AccommodationAmenity
            if Recorder.has_child(amenity, AccommodationAmenity):
                log_err(
                    f"del_amenity(): Deletion {id} forbidden "
                    f"- {amenity} has associations in AccommodationAmenity"
                )
                raise HasChildError

            # Attempt to delete the record
            Recorder.delete(session, amenity)

        log_info(f"Amenity ID {id} deletion successfully finished")

    except (NoRecordsFound, ValueError, HasChildError,
            ValidationError, SQLAlchemyError, Exception):
        raise
