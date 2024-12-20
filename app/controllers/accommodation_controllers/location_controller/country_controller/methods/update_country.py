from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Country
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info
from .get_country import get_country


def update_country(country_id: int, data: dict, session: Session):
    log_info('Country updating started')
    try:
        with session.begin_nested():
            Validator.validate_id(country_id)

            field = 'name'
            Validator.validate_required_field(field, data)

            new_name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Country,
                criteria={field: new_name}
            )

            Validator.validate_name(new_name)

            country = get_country(
                id=country_id,
                session=session,
                return_instance=True
            )

            Recorder.update(
                session, country, {field: new_name}  # type: ignore
            )

        log_info(f"Country with ID {country_id} successfully updated.")

    except (
        NoRecordsFound, ValidationError, ValueError,
        SQLAlchemyError, Exception
    ):
        raise
