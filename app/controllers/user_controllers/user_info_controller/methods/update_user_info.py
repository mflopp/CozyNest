from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from datetime import datetime

from utils import Validator, Finder
from utils.error_handler import ValidationError

from .get_user_info import fetch_user_info
from ...gender_controller.methods import get_updated_gender
from ...user_settings_controller.methods import update_user_setting


def update_user_info(
    id: int,
    user_data: dict,
    session: Session
):
    try:
        # Start a new transaction
        with session.begin_nested():

            # Fetch existing user info from the database
            user_info = fetch_user_info(id, session)
            if not user_info:
                raise Exception(f"User info with ID {id} not found")
            # required fields
            fields = ['first_name', 'last_name']
            relevant_fields = Finder.extract_required_data(fields, user_data)
            for value in relevant_fields.values():
                Validator.validate_name(value)

            user_info.first_name = user_data.get(
                'first_name', user_info.first_name
            )
            user_info.last_name = user_data.get(
                'last_name', user_info.last_name
            )

            # Handle birthdate format
            birthdate_str = user_data.get('birthdate', None)
            if birthdate_str:
                try:
                    user_info.birthdate = datetime.strptime(
                        birthdate_str, "%d.%m.%Y"
                    ).date()
                except ValueError:
                    raise ValueError(
                        f"Incorrect birthdate format: {birthdate_str}"
                    )
            else:
                user_info.birthdate = user_info.birthdate
            user_info.updated_at = func.now()

            # the following 2 blocks maybe NOT necessary
            # Block 1: update user settings
            # fetch UserSettings from the DB
            user_setting_id = update_user_setting(
                user_info.user_settings_id,
                user_data,
                session
            )

            # update user_settings_id with a new user_setting_id
            if user_setting_id:
                user_info.user_settings_id = user_setting_id

            # Block 2: update gender
            # Fetch new gender
            gender_id = get_updated_gender(user_data, session)
            # update gender_id with a new gender
            if gender_id:
                user_info.gender_id = gender_id

            # commit the transaction after 'with' block
            session.flush()

    except (SQLAlchemyError, ValidationError, ValueError, Exception):
        raise
