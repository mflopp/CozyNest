from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import Country
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from .parse_full_country import parse_full_country
from utils.logs_handler import log_info, log_err

ERR_MSG = "Error occurred while Country record creating"


def create_country(data: Dict, session: Session) -> Dict[str, Any]:
    log_info('Country creation started')
    try:
        with session.begin_nested():
            field = 'name'
            Validator.validate_required_field(field, data)

            name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Country,
                criteria={field: name}
            )

            Validator.validate_name(name)

            new_country = Country(name=name)
            if not new_country:
                log_err("Country was not created for some reason")
                raise SQLAlchemyError

            Recorder.add(session, new_country)

        log_info('Country creation successfully finished')
        return parse_full_country(new_country)

    except (ValidationError, ValueError, Exception):
        raise
