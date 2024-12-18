import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import AmenitiesCategory
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from .parse_full_amenity_category import parse_full_amenity_category


def add_amenity_category(
    user_data: Dict,
    session: Session
) -> Dict[str, Any]:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            field = 'category'

            Validator.validate_required_field(field, user_data)

            category = user_data.get(field)

            Validator.validate_unique_field(
                session, AmenitiesCategory,
                field, category
            )

            logging.info(
                "Validations succesfully passed! "
                "(creating an amenity category)"
            )

            new_category = AmenitiesCategory(category=category)
            Recorder.add(session, new_category)

        session.flush()
        return parse_full_amenity_category(new_category)

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
