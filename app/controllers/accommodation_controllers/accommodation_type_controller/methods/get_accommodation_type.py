from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict

from models import AccommodationType
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound

from .parse_full_accommodation_type import parse_full_accommodation_type
from utils.logs_handler import log_info, log_err


def fetch_accommodation_type(
    field: str,
    value: Any,
    session: Session,
    return_instance: bool = False
) -> AccommodationType | Dict[str, Any]:
    log_info(f"Accommodation type fetching by {field} started...")
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'accomodation_type' parameter is in user request
            Validator.validate_required_field(field, value)
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)
        # Fetch the accomodation_type record
        accomodation_type = Finder.fetch_record(
            session=session,
            Model=AccommodationType,
            criteria=filter_criteria
        )

        if accomodation_type and isinstance(
            accomodation_type, AccommodationType
        ):
            log_info('Accommodation type fetching successfully finished')

            if return_instance:
                log_info('Return Accommodation type as Model')
                return accomodation_type

            log_info('Return Accommodation type as Dict')
            return parse_full_accommodation_type(accomodation_type)

        log_err(
            'fetch_accommodation_type(): No Accommodation type record found'
        )
        raise NoRecordsFound

    except (ValidationError, NoRecordsFound, SQLAlchemyError, Exception):
        raise
