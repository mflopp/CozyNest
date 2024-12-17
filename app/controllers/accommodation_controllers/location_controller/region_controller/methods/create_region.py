import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Region
from ...country_controller import CountryController
from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_region import parse_full_region

ERR_MSG = "Error occurred while Region record creating"
TRACEBACK = False


def create_region(data: Dict, session: Session) -> Dict:
    try:
        with session.begin_nested():
            required_fields = ['name', 'country_id']
            Validator.validate_required_fields(required_fields, data)

            name = data.get('name')
            country_id = data.get('country_id')

            Validator.validate_uniqueness(
                session=session,
                Model=Region,
                criteria={'name': name, 'country_id': country_id}
            )

            Validator.validate_name(name)

            country = CountryController.get_country(
                country_id=data['country_id'],
                session=session
            )
            if not country:
                raise NoRecordsFound

            new_region = Region(
                country_id=country.id,
                name=data['name']
            )
            if not new_region:
                raise SQLAlchemyError

            Recorder.add(session, new_region)

            return parse_full_region(new_region, session)

    except NoRecordsFound as e:
        logging.error(
            f"No Records Found for creatings: {e}",
            exc_info=TRACEBACK
        )
        raise

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
