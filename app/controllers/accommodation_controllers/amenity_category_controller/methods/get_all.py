from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from utils.error_handler import ValidationError, NoRecordsFound
from models.accommodations import AmenitiesCategory
from utils import Finder
from .parse_full_amenity_category import parse_full_amenity_category
from utils.logs_handler import log_info


def fetch_amenity_categories(session: Session) -> List:
    log_info('Amenity categories fetching started...')
    try:
        # Fetch all genders records
        categories = Finder.fetch_records(session, AmenitiesCategory)
        Finder.log_found_amount(categories)

        result = [
            parse_full_amenity_category(category) for category in categories
        ]

        log_info('Amenity categories fetching successfully finished')

        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
