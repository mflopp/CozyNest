from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import City
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_city import parse_full_city
from utils.logs_handler import log_info, log_err


def get_city(
    id: int, session: Session, return_instance: bool = False
) -> City | Dict[str, Any]:
    log_info('City fetching started')
    try:
        Validator.validate_id(id)

        city = Finder.fetch_record(
            session=session,
            Model=City,
            criteria={'id': id}
        )

        if city:
            log_info('City fetching successfully finished')

            if return_instance:
                log_info('Return City as Model')
                return city

            log_info('Return City as Dict')
            return parse_full_city(city)

        log_err('get_city(): No City record found')
        raise NoRecordsFound

    except (ValidationError, SQLAlchemyError, Exception):
        raise
