from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

from models import AmenitiesCategory
from utils import Finder, Validator
from utils.error_handler import ValidationError

from .parse_full_amenity_category import parse_full_amenity_category
from utils.logs_handler import log_info


# def fetch_gender(id: int, session: Session) -> Dict:
def fetch_amenity_category(
    field: str,
    value: Any,
    session: Session,
    return_instance: bool = False
) -> AmenitiesCategory:
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'gender' parameter exists in user request
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the gender record
        category = Finder.fetch_record(
            session=session,
            Model=AmenitiesCategory,
            criteria=filter_criteria
        )

        if category:
            log_info('Amenity category fetching successfully finished')

            if return_instance:
                log_info('Return Amenity category as Model')
                return category

            log_info('Return Amenity category as Dict')
            return parse_full_amenity_category(category)

    except SQLAlchemyError as e:
        raise SQLAlchemyError(
            {f"DB error occurred while querying amenity category by {field}: "
             f"{e}"}, 500
        )

    except (ValidationError, Exception):
        raise
