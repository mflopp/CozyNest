import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.accommodations import Amenity

from .get_amenity_category import fetch_amenity_category
from utils import Recorder
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)


def del_amenity_category(id: int, session: Session):

    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            category = fetch_amenity_category('id', id, session, True)

            if not category:
                msg = f"Amenity category ID {id} not found"
                raise NoRecordsFound(msg)

            # Check if current category is in use in user_info
            if not Recorder.has_child(category, Amenity):
                # Attempt to delete the record
                Recorder.delete(session, category)
            else:
                msg = (
                    f"Impossible to delete amenity category with ID {id}. "
                    "Record has child records"
                )
                raise HasChildError(msg)

        # commit the transaction after 'with' block
        session.flush()
        logging.info(f"Amenity category ID {id} deleted successfully")

    except (NoRecordsFound, HasChildError, SQLAlchemyError, Exception):
        raise
