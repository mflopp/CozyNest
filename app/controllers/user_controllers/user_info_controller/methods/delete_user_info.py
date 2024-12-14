import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.users import User
from utils import Recorder
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)

from .get_user_info import fetch_user_info


def del_user_info(id: int, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():

            # Getting user setting by id from the DB
            user_info = fetch_user_info(id, session)

            if not user_info:
                msg = f"User info ID {id} not found"
                raise NoRecordsFound(msg)

            # Check if current user info is in use in User
            if not Recorder.has_child(user_info, User):
                # Attempt to delete the record
                Recorder.delete(session, user_info)
            else:
                msg = (
                    f"Impossible to delete user info with ID {id}. "
                    "Record has child records"
                )
                raise HasChildError(msg)

        # commit the transaction after 'with' block
        session.flush()
        logging.info(f"User info ID {id} deleted successfully")

    except NoRecordsFound:
        raise

    except HasChildError:
        raise

    except SQLAlchemyError:
        raise

    except Exception:
        raise
