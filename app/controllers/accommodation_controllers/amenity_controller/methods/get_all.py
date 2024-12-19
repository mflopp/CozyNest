from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from utils.error_handler import ValidationError, NoRecordsFound
from models.accommodations import Amenity
from utils import Finder
from .parse_full_amenity import parse_full_amenity
from utils.logs_handler import log_info


def fetch_amenities(session: Session) -> List:
    log_info('Amenities fetching started...')
    try:
        # Fetch all Amenities records
        amenities = Finder.fetch_records(session, Amenity)
        Finder.log_found_amount(amenities)

        result = [
            parse_full_amenity(amenity) for amenity in amenities
        ]

        log_info('Amenities fetching successfully finished')

        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
