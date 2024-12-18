from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import Country
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_country import parse_full_country
from utils.logs_handler import log_info, log_err


def get_country(
    id: int, session: Session, return_instance: bool = False
) -> Country | Dict[str, Any]:
    log_info('Country fetching started')
    try:
        Validator.validate_id(id)

        country = Finder.fetch_record(
            session=session,
            Model=Country,
            criteria={'id': id}
        )

        if country and isinstance(country, Country):
            log_info('Country fetching successfully finished')

            if return_instance:
                log_info('Return Country as Model')
                return country

            log_info('Return Country as Dict')
            return parse_full_country(country)

        log_err('get_country(): No Country record found')
        raise NoRecordsFound

    except (ValidationError, SQLAlchemyError, Exception):
        raise
