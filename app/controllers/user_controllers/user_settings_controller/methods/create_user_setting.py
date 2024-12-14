import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import UserSettings
from utils import Validator, Recorder, Finder
from utils.error_handler import ValidationError


def add_user_setting(user_data: Dict, session: Session) -> UserSettings:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            # ISO 639-3 language codes are used
            fields = ['currency', 'language']
            relevant_values = Finder.extract_required_data(fields, user_data)

            Validator.validate_required_fields(fields, relevant_values)

            currency = user_data.get(fields[0])
            language = user_data.get(fields[1])

            Validator.validate_uniqueness(
                session, UserSettings,
                relevant_values
            )

            Validator.validate_currency(currency)
            Validator.validate_language(language)

            logging.info(
                'Currency and language validations succesfully passed!'
            )

            user_setting = UserSettings(currency=currency, language=language)
            Recorder.add(session, user_setting)

        session.flush()
        return user_setting

    except ValidationError:
        raise

    except ValueError:
        raise

    except SQLAlchemyError:
        raise

    except Exception:
        raise
