from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from utils.error_handler import ValidationError, NoRecordsFound
from models.accommodations import AccommodationAmenity
from utils import Finder
from .parse_full_accommodation_amenity import parse_full_accommodation_amenity
from utils.logs_handler import log_info


def fetch_accommodation_amenities(session: Session) -> List:
    log_info('Accommodation Amenities fetching started...')
    try:
        # Fetch all Amenities records
        acc_amenities = Finder.fetch_records(
            session, AccommodationAmenity
        )
        Finder.log_found_amount(acc_amenities)

        result = [
            parse_full_accommodation_amenity(item) for item in acc_amenities
        ]

        log_info('Accommodation Amenities fetching successfully finished')

        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
