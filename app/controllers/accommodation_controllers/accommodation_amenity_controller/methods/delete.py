from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import Amenity, AccommodationAmenity, Accommodation

from utils import Recorder
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
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

            # Check if accommodation_amenity is in use in Amenity
            if Recorder.has_child(acc_amenity, Amenity):
                log_err(
                    f"del_accommodation_amenity(): Deletion {id} forbidden "
                    f"- {acc_amenity} has associations in Amenity"
                )
                raise HasChildError

            # Check if accommodation_amenity is in use in Accommodation
            if Recorder.has_child(acc_amenity, Accommodation):
                log_err(
                    f"del_accommodation_amenity(): Deletion {id} forbidden "
                    f"- {acc_amenity} has associations "
                    "in Accommodation"
                )
                raise HasChildError

            # Attempt to delete the record
            Recorder.delete(session, acc_amenity)

        log_info(
            f"Accommodation Amenity ID {id} deletion successfully finished"
        )

    except (NoRecordsFound, ValueError, HasChildError,
            ValidationError, SQLAlchemyError, Exception):
        raise
