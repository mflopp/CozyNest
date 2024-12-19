from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from models import Amenity
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from .parse_full_amenity import parse_full_amenity
from utils.logs_handler import log_info, log_err
from ...amenity_category_controller import AmenityCategoryController


def add_amenity(
    user_data: Dict,
    session: Session
) -> Dict[str, Any]:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            fields = ['name', 'category_id']

            Validator.validate_required_fields(fields, user_data)

            name = user_data.get('name')
            category_id = user_data.get('category_id')
            Validator.validate_id(category_id)

            Validator.validate_uniqueness(
                session=session,
                Model=Amenity,
                criteria={'name': name, 'category_id': category_id}
            )

            log_info(
                "Validations succesfully passed! "
                "(trying to create an amenity)"
            )

            category = AmenityCategoryController.get_one_by_id(
                category_id=category_id,
                session=session,
                return_instance=True
            )

            new_amenity = Amenity(
                name=name,
                category_id=category.id
            )
            if not new_amenity:
                log_err(
                    "add_amenity(): Amenity was not created for some reason"
                )
                raise SQLAlchemyError

            Recorder.add(session, new_amenity)

        log_info('Amenity creation successfully finished')
        return parse_full_amenity(new_amenity)

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
