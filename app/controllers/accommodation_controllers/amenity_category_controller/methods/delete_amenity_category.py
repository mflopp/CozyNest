from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import Amenity, AmenitiesCategory

from utils import Recorder
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_amenity_category import fetch_amenity_category


def del_amenity_category(id: int, session: Session):
    log_info(f"Amenity category with ID={id} deletion started...")
    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            category: AmenitiesCategory = fetch_amenity_category(
                'id', id, session, True
            )

            # if not category:
            #     msg = f"Amenity category ID {id} not found"
            #     raise NoRecordsFound(msg)

            # Check if current category is in use in user_info
            if Recorder.has_child(category, Amenity):
                log_err(
                    f"del_amenity_category(): Deletion {id} forbidden"
                    f"- {category} has associations in Amenity"
                )
                raise HasChildError

            # Attempt to delete the record
            Recorder.delete(session, category)

        # commit the transaction after 'with' block
        session.flush()
        log_info(f"Amenity category ID {id} deletion successfully finished")

    except (NoRecordsFound, ValueError, HasChildError,
            ValidationError, SQLAlchemyError, Exception):
        raise
