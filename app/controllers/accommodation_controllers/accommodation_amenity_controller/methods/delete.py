from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import AccommodationAmenity

from utils import Recorder
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_info
from .get_one import fetch_accommodation_amenity


def del_accommodation_amenity(id: int, session: Session):
    log_info(f"Accommodation Amenity with ID={id} deletion started...")
    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            acc_amenity: AccommodationAmenity = fetch_accommodation_amenity(
                'id',
                id,
                session,
                True
            )

            # Attempt to delete the record
            Recorder.delete(session, acc_amenity)

        log_info(
            f"Accommodation Amenity ID {id} deletion successfully finished"
        )

    except (NoRecordsFound, ValueError, HasChildError,
            ValidationError, SQLAlchemyError, Exception):
        raise
