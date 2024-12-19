from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info
from .get_city import get_city


def update_city(city_id: int, data: dict, session: Session):
    log_info('City updating started')
    try:
        with session.begin_nested():
            Validator.validate_id(city_id)

            field = 'name'
            Validator.validate_required_field(field, data)

            new_name = data.get(field)
            Validator.validate_name(new_name)

            Validator.validate_uniqueness(
                session=session,
                Model=City,
                criteria={field: new_name}
            )

            city = get_city(
                id=city_id,
                session=session,
                return_instance=True
            )

            Recorder.update(session, city, {field: new_name})   # type: ignore

        log_info(f"City with ID {city_id} successfully updated.")

    except (
        NoRecordsFound, ValidationError, ValueError,
        SQLAlchemyError, Exception
    ):
        raise
