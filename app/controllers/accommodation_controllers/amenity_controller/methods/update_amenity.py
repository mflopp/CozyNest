from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Amenity
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_info
from .get_amenity import fetch_amenity


def update_amenity(amenity_id: int, data: dict, session: Session):
    log_info('Amenity updating started...')
    try:

        # Chech if Amenity update data exists
        if not ('name' in data or 'category_id' in data):
            raise ValueError(f"Not enough data to update Amenity {amenity_id}")

        name_new = data.get('name')
        category_id_new = data.get('category_id')

        with session.begin_nested():
            amenity_current = fetch_amenity(
                'id',
                amenity_id,
                session,
                True
            )

            if not name_new:
                name_new = amenity_current.name
            if not category_id_new:
                category_id_new = amenity_current.category_id
            else:
                Validator.validate_id(category_id_new)

            new_data = {'name': name_new, 'category_id': category_id_new}

            Validator.validate_uniqueness(
                session=session,
                Model=Amenity,
                criteria=new_data
            )
            log_info(
                "Validations succesfully passed! "
                "(trying to update an amenity)"
            )

            Recorder.update(session, amenity_current, new_data)

        log_info(f"Amenity with ID {amenity_id} successfully updated.")

    except (
        NoRecordsFound, ValidationError, ValueError,
        SQLAlchemyError, Exception
    ):
        raise
