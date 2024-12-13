import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

from models import Country
from utils import Finder, Validator
from utils.error_handler import ValidationError, NoRecordsFound


def get_country(field: str, value: Any, session: Session) -> Country:
    try:
        # possible_fields = {'id', 'name'}

        # if field not in possible_fields:
        #     raise ValidationError(f'Field must be in {possible_fields}')

        # if field == "id":
        Validator.validate_id(value)

        # if field == 'name':
        #     value = value.capitalize()
        #     Validator.validate_name(value)

        # Retrieve the record
        country = Finder.fetch_record(
            session=session,
            Model=Country,
            criteria={field: value}
        )

        if country:
            return country

        raise NoRecordsFound(f'No country found with ID: {value}')

    except ValidationError as e:
        logging.error(
            {f"ValidationErr occurred while fetching Country by {field}: {e}"},
            exc_info=True
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            {f"DB error occurred while fetching Country by {field}: {e}"},
            exc_info=True
        )
        raise

    except Exception as e:
        logging.error(
            {f"Unexpected error while fetching Country by {field}: {e}"},
            exc_info=True
        )
        raise
