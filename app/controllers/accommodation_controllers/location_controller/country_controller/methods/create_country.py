import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Country
from utils import Validator, Recorder
from utils.error_handler import ValidationError

ERR_MSG = "Error occurred while Country record creating"
TRACEBACK = True


def create_country(data: Dict, session: Session) -> Country:
    try:
        with session.begin_nested():
            field = 'name'
            Validator.validate_required_field(field, data)

            name = data.get(field)

            Validator.validate_uniqueness(
                session=session,
                Model=Country,
                criteria={field: name}
            )

            Validator.validate_name(name)

            new_country = Country(name=name)
            if not new_country:
                raise SQLAlchemyError

            Recorder.add(session, new_country)

        return new_country

    except ValidationError as e:
        logging.error(
            f"Validation {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except ValueError as e:
        logging.error(
            f"Value {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise
