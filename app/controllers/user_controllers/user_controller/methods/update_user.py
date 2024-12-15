from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from datetime import datetime

from models import User
from utils import Validator
from utils.error_handler import ValidationError

from .get_only_user import fetch_only_user
from ...gender_controller.methods import get_updated_gender
from ...user_settings_controller.methods import update_user_setting
from ...user_info_controller.methods import fetch_user_info
from ...user_role_controller.methods import get_updated_user_role


def update_user_data(id: int, user_data: dict, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():

            # Fetch the user by ID
            user = fetch_only_user(id, session)
            if not user:
                # consider return false only !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                return {"error": "User not found"}, 404

            # Update user fields
            if 'email' in user_data:
                Validator.validate_email(user_data['email'])
                Validator.validate_uniqueness(
                    session, User, {'email': user_data['email']}
                )
                user.email = user_data['email']
            if 'password' in user_data:
                Validator.validate_pswrd(user_data['password'])

                user.password = user_data['password']
            if 'phone' in user_data:
                Validator.validate_phone(user_data['phone'])
                Validator.validate_uniqueness(
                    session, User, {'phone': user_data['phone']}
                )
                user.phone = user_data['phone']

            # maybe REPLACE XXX block to the following:
            # # updating all the information from user_data in UserInfo
            # Recorder.update(session, UserInfo, user_data)

            # fetch UserInfo from the DB
            user_info = fetch_user_info(user.info_id, session)
            if not user_info:
                raise ValueError(
                    "User info not found in the DB (DB integrity compromised)"
                )

            # beginning of XXX block
            # Update fields if they are provided in user_data (NO VALIDATION)
            user_info.first_name = user_data.get(
                'first_name',
                user_info.first_name
            )
            user_info.last_name = user_data.get(
                'last_name',
                user_info.last_name
            )
            birthdate_str = user_data.get('birthdate', None)
            if birthdate_str:
                try:
                    user_info.birthdate = datetime.strptime(
                        birthdate_str, "%d.%m.%Y"
                    ).date()
                except ValueError:
                    raise Exception(
                        f"Incorrect birthdate format: {birthdate_str}"
                    )
            else:
                user_info.birthdate = user_info.birthdate
            user_info.updated_at = func.now()
            # end of XXX block

            # fetch UserSettings from the DB
            user_setting_id = update_user_setting(
                user_info.user_settings_id,
                user_data,
                session
            )
            # update user_settings_id with a new user_setting_id
            if user_setting_id:
                user_info.user_settings_id = user_setting_id

            # Fetch new user role
            user_role_id = get_updated_user_role(user_data, session)
            # update role_id with a new role
            if user_role_id:
                user.role_id = user_role_id

            # Fetch new gender
            gender_id = get_updated_gender(user_data, session)
            # update gender_id with a new gender
            if gender_id:
                user_info.gender_id = gender_id

        session.flush()

    except (ValueError, ValidationError, SQLAlchemyError, Exception):
        raise
