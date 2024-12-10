import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from .get_city import get_city
from utils import Recorder, ValidationError


def delete_city(id: int, session: Session):
    try:
        with session.begin_nested():
            # Attempt to fetch the region
            city_to_delete = get_city(field='id', value=id, session=session)

            # Attempt to delete the record
            Recorder.delete(session, city_to_delete)

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
