from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import Region
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_region import parse_full_region
from utils.logs_handler import log_info, log_err


def get_region(
    id: int, session: Session, return_instance: bool = False
) -> Region | Dict[str, Any]:
    log_info('Region fetching started')
    try:
        Validator.validate_id(id)

        region = Finder.fetch_record(
            session=session,
            Model=Region,
            criteria={'id': id}
        )

        if region:
            log_info('Region fetching successfully finished')

            if return_instance:
                log_info('Return Region as Model')
                return region

            log_info('Return Region as Dict')
            return parse_full_region(region)

        log_err('get_region(): No Region record found')
        raise NoRecordsFound

    except (ValidationError, SQLAlchemyError, Exception):
        raise
