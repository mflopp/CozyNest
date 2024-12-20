from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict

from models import Amenity
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

from .parse_full_amenity import parse_full_amenity
from utils.logs_handler import log_info, log_err


# def fetch_gender(id: int, session: Session) -> Dict:
def fetch_amenity(
    field: str,
    value: Any,
    session: Session,
    return_instance: bool = False
) -> Amenity | Dict[str, Any]:
    log_info(f"Amenity fetching by {field} started...")
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'name' parameter exists in user request
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the amenity record
        amenity = Finder.fetch_record(
            session=session,
            Model=Amenity,
            criteria=filter_criteria
        )

        if amenity and isinstance(amenity, Amenity):
            log_info('Amenity fetching successfully finished')

            if return_instance:
                log_info('Return Amenity as Model')
                return amenity

            log_info('Return Amenity as Dict')
            return parse_full_amenity(amenity)

        log_err('fetch_amenity(): No Amenity record found')
        raise NoRecordsFound

    except (ValidationError, NoRecordsFound, SQLAlchemyError, Exception):
        raise
