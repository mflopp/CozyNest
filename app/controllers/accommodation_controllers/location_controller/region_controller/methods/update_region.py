from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Region
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info
from .get_region import get_region


def update_region(region_id: int, data: dict, session: Session):
    log_info('Region updating started')
    try:
        with session.begin_nested():
            Validator.validate_id(region_id)

            field = 'name'
            Validator.validate_required_field(field, data)

            new_name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Region,
                criteria={field: new_name}
            )

            Validator.validate_name(new_name)

            region = get_region(
                id=region_id,
                session=session,
                return_instance=True
            )

            Recorder.update(session, region, {field: new_name})

        log_info(f"Region with ID {region_id} successfully updated.")

    except (
        NoRecordsFound, ValidationError, ValueError,
        SQLAlchemyError, Exception
    ):
        raise
