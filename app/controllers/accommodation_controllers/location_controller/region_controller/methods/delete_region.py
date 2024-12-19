from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import City, Region
from utils import Recorder, Validator
from utils.error_handler import (
    ValidationError,
    NoRecordsFound,
    HasChildError
)

from utils.logs_handler import log_err, log_info
from .get_region import get_region


def delete_region(id: int, session: Session):
    log_info(f"Region with ID={id} deletion started.")
    try:
        Validator.validate_id(id)

        with session.begin_nested():
            region: Region = get_region(
                id=id,
                session=session,
                return_instance=True
            )  # type: ignore

            if Recorder.has_child(region, City):
                log_err(
                    f'delete_region(): Deletion forbidden'
                    f'- {region} has associations in City'
                )
                raise HasChildError

            Recorder.delete(session, region)
            log_info('Region deletion successfully finished')

    except (
        NoRecordsFound, ValidationError,
        SQLAlchemyError, ValueError, Exception
    ):
        raise
