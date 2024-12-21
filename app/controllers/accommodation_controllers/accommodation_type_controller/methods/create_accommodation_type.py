from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import AccommodationType
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from .parse_full_accommodation_type import parse_full_accommodation_type
from utils.logs_handler import log_info, log_err


def add_accommodation_type(
    user_data: Dict,
    session: Session
) -> Dict[str, Any]:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            field = 'accommodation_type'

            Validator.validate_required_field(field, user_data)

            accommodation_type = user_data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=AccommodationType,
                criteria={field: accommodation_type}
            )

            log_info(
                "Validations succesfully passed! "
                "(creating an accommodation type)"
            )

            new_accommodation_type = AccommodationType(
                accommodation_type=accommodation_type
            )
            if not new_accommodation_type:
                log_err(
                    "add_accommodation_type(): accommodation type was not "
                    "created for some reason"
                )
                raise SQLAlchemyError
            Recorder.add(session, new_accommodation_type)

        log_info('accommodation type creation successfully finished')
        return parse_full_accommodation_type(new_accommodation_type)

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
