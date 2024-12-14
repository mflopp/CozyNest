import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.users import UserInfo

from .get_gender import fetch_gender
from utils import Recorder
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)


def del_gender(id: int, session: Session):

    try:

        # Start a new transaction
        with session.begin_nested():

            # Getting gender by id from the DB
            gender = fetch_gender('id', id, session)

            if not gender:
                msg = f"gender ID {id} not found"
                raise NoRecordsFound(msg)

            # Check if current gender is in use in user_info
            if not Recorder.has_child(gender, UserInfo):
                # Attempt to delete the record
                Recorder.delete(session, gender)
            else:
                msg = (
                    f"Impossible to delete gender with ID {id}. "
                    "Record has child records"
                )
                raise HasChildError(msg)

        # commit the transaction after 'with' block
        session.flush()
        logging.info(f"Gender ID:{id} deleted successfully")

    except NoRecordsFound:
        raise

    except HasChildError:
        raise

    except SQLAlchemyError:
        raise

    except Exception:
        raise
