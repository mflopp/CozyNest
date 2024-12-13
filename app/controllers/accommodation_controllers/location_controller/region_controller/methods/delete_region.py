import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from utils import Recorder
from utils.error_handler import ValidationError

from .get_region import get_region


def delete_region(id: int, session: Session):
    try:
        with session.begin_nested():
            # Attempt to fetch the region
            region = get_region(field='id', value=id, session=session)

            # Attempt to delete the record
            Recorder.delete(session, region)

    except ValidationError as e:
        logging.error(
            {f"Validation error occurred while deleting: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while deleting: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while deleting: {e}"},
            exc_info=True
        )
        raise
