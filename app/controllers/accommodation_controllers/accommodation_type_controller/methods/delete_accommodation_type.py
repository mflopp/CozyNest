from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import Accommodation, AccommodationType

from utils import Recorder
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_accommodation_type import fetch_accommodation_type


def del_accommodation_type(id: int, session: Session):
    log_info(f"Accommodation type with ID={id} deletion started...")
    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            accommodation_type: AccommodationType = fetch_accommodation_type(
                'id', id, session, True
            )

            # Check if current accommodation_type is in use in Accommodation
            if Recorder.has_child(accommodation_type, Accommodation):
                log_err(
                    f"del_accommodation_type(): Deletion {id} forbidden"
                    f"- {accommodation_type} has associations in Accommodation"
                )
                raise HasChildError

            # Attempt to delete the record
            Recorder.delete(session, accommodation_type)

        log_info(f"Accommodation type ID {id} deletion successfully finished")

    except (NoRecordsFound, ValueError, HasChildError,
            ValidationError, SQLAlchemyError, Exception):
        raise
