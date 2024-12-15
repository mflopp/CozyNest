import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Gender
from utils import Validator, Recorder
from utils.error_handler import ValidationError


def add_gender(user_data: Dict, session: Session) -> Gender:

    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():

            fields = ['gender', 'description']

            Validator.validate_required_field(fields[0], user_data)

            gender = user_data.get(fields[0])
            description = user_data.get(fields[1])

            Validator.validate_unique_field(
                session, Gender,
                fields[0], gender
            )

            logging.info('Validations succesfully passed! (creating a gender)')

            new_gender = Gender(gender=gender, description=description)
            Recorder.add(session, new_gender)

        session.flush()
        return new_gender

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
