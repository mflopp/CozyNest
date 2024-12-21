from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from utils.error_handler import ValidationError, NoRecordsFound
from models.accommodations import AccommodationType
from utils import Finder
from .parse_full_accommodation_type import parse_full_accommodation_type
from utils.logs_handler import log_info


def fetch_accommodation_types(session: Session) -> List:
    log_info('Accommodation types fetching started...')
    try:
        # Fetch all Amenity categories records
        accommodation_types = Finder.fetch_records(session, AccommodationType)
        Finder.log_found_amount(accommodation_types)

        result = [
            parse_full_accommodation_type(type) for type in accommodation_types
        ]

        log_info('Accommodation types fetching successfully finished')

        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
