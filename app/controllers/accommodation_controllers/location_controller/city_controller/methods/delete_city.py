from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City, Address
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_city import get_city


def delete_city(id: int, session: Session):
    log_info(f"City with ID={id} deletion started.")
    try:
        Validator.validate_id(id)

        with session.begin_nested():
            city_to_delete: City = get_city(
                id=id,
                session=session,
                return_instance=True
            )   # type: ignore

            if Recorder.has_child(city_to_delete, Address):
                log_err(
                    f'delete_city(): Deletion forbidden'
                    f'- {city_to_delete} has associations in Address'
                )
                raise HasChildError

            Recorder.delete(session, city_to_delete)
            log_info('City deletion successfully finished')

    except (
        NoRecordsFound, ValidationError,
        SQLAlchemyError, ValueError, Exception
    ):
        raise
