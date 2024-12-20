from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict

from models import AccommodationAmenity
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

from .parse_full_accommodation_amenity import parse_full_accommodation_amenity
from utils.logs_handler import log_info, log_err


# def fetch_gender(id: int, session: Session) -> Dict:
def fetch_accommodation_amenity(
    field: str,
    value: Any,
    session: Session,
    return_instance: bool = False
) -> AccommodationAmenity | Dict[str, Any]:
    log_info(f"Accommodation Amenity fetching by {field} started...")
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'accomodation_id' parameter exists in user request
            Validator.validate_required_field(field, value)
            Validator.validate_id(value.get('accommodation_id'))
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the Accommodation Amenity record
        acc_amenity = Finder.fetch_record(
            session=session,
            Model=AccommodationAmenity,
            criteria=filter_criteria
        )

        if acc_amenity and isinstance(acc_amenity, AccommodationAmenity):
            log_info('Accommodation Amenity fetching successfully finished')

            if return_instance:
                log_info('Return Accommodation Amenity as Model')
                return acc_amenity

            log_info('Return Accommodation Amenity as Dict')
            return parse_full_accommodation_amenity(acc_amenity)

        log_err(
            "fetch_accommodation_amenity(): No Accommodation Amenity "
            "record found"
        )
        raise NoRecordsFound

    except (ValidationError, NoRecordsFound, SQLAlchemyError, Exception):
        raise
