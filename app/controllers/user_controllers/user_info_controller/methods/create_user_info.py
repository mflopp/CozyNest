from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from datetime import datetime

from models import UserInfo
from typing import Dict
from utils import Validator, Recorder
from utils.error_handler import ValidationError

from ...gender_controller.methods import fetch_gender
from ...user_settings_controller.methods import fetch_user_setting


def add_user_info(
    user_data: Dict,
    session: Session
) -> UserInfo:

    try:
        # set default values
        gender_default = "Male"
        currency_default = "USD"
        language_default = "ENG"
        first_name_default = "first_name"
        last_name_default = "last_name"

        # Start a new transaction
        with session.begin_nested():

            # getting first and last name from the request
            first_name = user_data.get("first_name")
            last_name = user_data.get("last_name")
            # validating first and last names
            if first_name:
                Validator.validate_name(first_name)
            else:
                first_name = first_name_default
            if last_name:
                Validator.validate_name(last_name)
            else:
                last_name = last_name_default
            # getting default gender from the DB
            # Chech if user request has information about gender
            gender_new = user_data.get("gender", gender_default)

            gender = fetch_gender(
                'gender', {"gender": gender_new}, session
            )
            if not gender:
                raise ValueError(
                    f"Gender {gender_new} was not found in the DB"
                )

            # getting user setting from the request else setting default
            currency_new = user_data.get("currency", currency_default)
            language_new = user_data.get("language", language_default)
            # validating currency and language value
            Validator.validate_currency(currency_new)
            Validator.validate_language(language_new)
            user_setting_default = {
                "currency": currency_new, "language": language_new
            }
            # fetching user setting from the DB
            user_setting = fetch_user_setting(
                user_setting_default,
                session
            )

            if not user_setting:
                raise ValueError(
                    f"Default user setting {user_setting_default} was not "
                    "found in the DB"
                )

            # Handle birthdate format
            birthdate_new = user_data.get('birthdate', None)
            if birthdate_new:
                birthdate_new = datetime.strptime(
                    birthdate_new, "%d.%m.%Y"
                ).date()

            # Create UserInfo
            user_info = UserInfo(
                gender_id=gender.id,
                user_settings_id=user_setting.id,
                first_name=first_name,
                last_name=last_name,
                birthdate=birthdate_new,
                created_at=func.now(),
                updated_at=func.now()
            )

            Recorder.add(session, user_info)

        session.flush()
        return user_info

    except (ValidationError, ValueError, SQLAlchemyError):
        raise

    except Exception as e:
        msg = f"Error creating a user info: {str(e)}"
        raise Exception(msg)
