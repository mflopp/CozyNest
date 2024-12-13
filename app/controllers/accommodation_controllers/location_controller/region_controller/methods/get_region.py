import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

from models import Region
from utils import Validator, Finder
from utils.error_handler import ValidationError


def get_region(field: str, value: Any, session: Session) -> Region:
    try:
        possible_fields = {'id', 'name'}

        if field not in possible_fields:
            raise ValidationError(f'Field must be in {possible_fields}')

        if field == "id":
            Validator.validate_id(value)

        if field == "name":
            Validator.validate_name(value)

        # Retrieve the record
        region = Finder.fetch_record(
            session=session,
            Model=Region,
            field=field,
            value=value
        )

        return region

    except ValidationError as e:
        logging.error(
            {f"Validation Error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base Error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected Error occurred while fetching record: {e}"},
            exc_info=True
        )
        raise
