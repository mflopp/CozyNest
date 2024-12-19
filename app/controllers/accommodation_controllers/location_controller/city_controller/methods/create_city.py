from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import City
from ...region_controller import RegionController
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info, log_err
from .parse_full_city import parse_full_city


def create_city(data: dict, session: Session) -> Dict:
    log_info('City creation started')
    try:
        with session.begin_nested():
            Validator.validate_required_fields(['name', 'region_id'], data)

            name: str = data.get('name')    # type: ignore
            region_id: int = data.get('region_id')  # type: ignore

            Validator.validate_name(name)
            Validator.validate_id(region_id)

            Validator.validate_uniqueness(
                session=session,
                Model=City,
                criteria={
                    'name': name,
                    'region_id': region_id
                }
            )

            region = RegionController.get_region(
                region_id=region_id,
                session=session,
                return_instance=True
            )

            new_city = City(region.id, name)    # type: ignore
            if not new_city:
                log_err(
                    "create_city(): Region was not created for some reason"
                )
                raise SQLAlchemyError

            Recorder.add(session, new_city)

            log_info('Region creation successfully finished')
            return parse_full_city(new_city)

    except (NoRecordsFound, ValidationError, ValueError, Exception):
        raise
