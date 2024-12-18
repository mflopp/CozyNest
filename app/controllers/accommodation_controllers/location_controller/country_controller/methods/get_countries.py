from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Country
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_country import parse_full_country
from utils.logs_handler import log_info


def get_countries(session: Session) -> List:
    log_info('Countries fetching started')
    try:
        countries = Finder.fetch_records(session, Country)
        Finder.log_found_amount(countries)

        result = [parse_full_country(country) for country in countries]

        log_info('Countries fetching successfully finished')
        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
