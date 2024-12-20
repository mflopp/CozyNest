from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region, Country
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_country import get_country


def delete_country(id: int, session: Session):
    log_info(f"Country with ID={id} deletion started.")
    try:
        Validator.validate_id(id)

        with session.begin_nested():
            country: Country = get_country(id, session, True)   # type: ignore

            if Recorder.has_child(country, Region):
                log_err(
                    f'delete_country(): Deletion forbidden'
                    f'- {country} has associations in Region'
                )
                raise HasChildError

            Recorder.delete(session, country)
            log_info('Country deletion successfully finished')

    except (
        NoRecordsFound, ValidationError,
        SQLAlchemyError, ValueError, Exception
    ):
        raise
