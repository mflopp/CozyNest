from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Region
from ...country_controller import CountryController
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_region import parse_full_region
from utils.logs_handler import log_info, log_err


def create_region(data: Dict, session: Session) -> Dict:
    log_info('Region creation started')
    try:
        with session.begin_nested():
            fields = ['name', 'country_id']
            Validator.validate_required_fields(fields, data)

            name = data.get('name')
            country_id = data.get('country_id')

            Validator.validate_uniqueness(
                session=session,
                Model=Region,
                criteria={'name': name, 'country_id': country_id}
            )

            Validator.validate_name(name)

            country = CountryController.get_country(
                country_id=data['country_id'],
                session=session,
                return_instance=True
            )

            new_region = Region(
                country_id=country.id,
                name=data['name']
            )
            if not new_region:
                log_err(
                    "create_region(): Region was not created for some reason"
                )
                raise SQLAlchemyError

            Recorder.add(session, new_region)

            log_info('Region creation successfully finished')
            return parse_full_region(new_region)

    except (NoRecordsFound, ValidationError, ValueError, Exception):
        raise
