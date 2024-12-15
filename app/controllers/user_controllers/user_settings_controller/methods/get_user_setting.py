import logging
from typing import Dict
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import UserSettings
from utils import Finder, Validator


def fetch_user_setting(data: Dict, session: Session):
    try:
        # ISO 639-3 language codes are used
        fields = ['currency', 'language']
        # getting only fiels from the user request data
        relevant_values = Finder.extract_required_data(fields, data)

        # Validate that data contains 'currency' and 'language' keys
        Validator.validate_required_fields(fields, relevant_values)

        currency = relevant_values.get(fields[0])
        language = relevant_values.get(fields[1])

        # Validate the input data format
        Validator.validate_currency(currency)
        Validator.validate_language(language)

        logging.info(
            'Currency and language validations succesfully passed!'
        )

        # Retrieve the record from the DB
        user_setting = Finder.fetch_record(
            session=session,
            Model=UserSettings,
            criteria={"currency": currency, "language": language}
        )

        return user_setting

    except (Exception, SQLAlchemyError):
        raise
