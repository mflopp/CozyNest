from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import City
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_city import parse_full_city
from utils.logs_handler import log_info


def get_cities(session: Session) -> List:
    log_info('Cities fetching started')
    try:
        cities = Finder.fetch_records(session, City)
        Finder.log_found_amount(cities)

        result = [parse_full_city(city) for city in cities]

        log_info('Cities fetching successfully finished')
        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
