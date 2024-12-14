import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.users import UserInfo

from .get_user_setting_by_id import fetch_user_setting_by_id
from utils import Recorder
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)


def del_user_setting(id: int, session: Session):

    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting user setting by id from the DB
            user_setting = fetch_user_setting_by_id(id, session)

            if not user_setting:
                msg = f"No records found for deleting with ID {id}"
                raise NoRecordsFound(msg)

            # Check if current user_setting is in use in user_info
            if not Recorder.has_child(user_setting, UserInfo):
                # Attempt to delete the record
                Recorder.delete(session, user_setting)
            else:
                msg = (
                    f"Impossible to delete user setting with ID {id}. "
                    "Record has child records"
                )
                raise HasChildError(msg)

        # commit the transaction after 'with' block
        session.flush()
        logging.info(f"User setting ID:{id} deleted successfully")

    except NoRecordsFound:
        raise

    except HasChildError:
        raise

    except SQLAlchemyError:
        raise

    except Exception:
        raise
