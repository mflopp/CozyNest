from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict

from models import AmenitiesCategory
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

from .parse_full_amenity_category import parse_full_amenity_category
from utils.logs_handler import log_info, log_err


def fetch_amenity_category(
    field: str,
    value: Any,
    session: Session,
    return_instance: bool = False
) -> AmenitiesCategory | Dict[str, Any]:
    log_info(f"Amenity category fetching by {field} started...")
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'category' parameter exists in user request
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the category record
        category = Finder.fetch_record(
            session=session,
            Model=AmenitiesCategory,
            criteria=filter_criteria
        )

        if category and isinstance(category, AmenitiesCategory):
            log_info('Amenity category fetching successfully finished')

            if return_instance:
                log_info('Return Amenity category as Model')
                return category

            log_info('Return Amenity category as Dict')
            return parse_full_amenity_category(category)

        log_err('fetch_amenity_category(): No Amenity category record found')
        raise NoRecordsFound

    except (ValidationError, NoRecordsFound, SQLAlchemyError, Exception):
        raise
