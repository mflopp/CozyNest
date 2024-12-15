import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError

from models import User
from utils import Validator, Recorder, Finder
from utils.error_handler import ValidationError

from ...user_info_controller.methods import add_user_info
from ...user_role_controller.methods import fetch_user_role


def add_user(user_data: dict, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():

            # validating fields
            fields = ['email', 'password', 'phone']
            Validator.validate_required_fields(fields, user_data)
            relevant_values = Finder.extract_required_data(fields, user_data)

            # validate data format
            Validator.validate_email(relevant_values['email'])
            Validator.validate_pswrd(relevant_values['password'])
            Validator.validate_phone(relevant_values['phone'])
            # Validate uniqueness of email and phone in the DB
            Validator.validate_uniqueness(
                session, User, {'email': user_data.get('email')}
            )
            Validator.validate_uniqueness(
                session, User, {'phone': user_data.get('phone')}
            )

            logging.info(
                'All validations succesfully passed!'
            )

            # Create UserInfo
            user_info = add_user_info(
                user_data,
                session
            )

            # getting default user role from the DB
            user_role_default = "User"
            user_role = fetch_user_role(
                'role',
                {'role': user_role_default},
                session
            )

            if not user_role:
                raise ValueError(
                    f"Default user role {user_role_default} was not found "
                    "in the DB"
                )

            # Create the user
            user = User(
                role_id=user_role.id,
                info_id=user_info.id,
                email=relevant_values['email'],
                password=relevant_values['password'],
                phone=relevant_values['phone'],
                created_at=func.now(),
                updated_at=func.now()
            )

            Recorder.add(session, user)

        # commit the transaction after 'with' block
        session.flush()
        logging.info(f"User created successfully with ID {user.id}")
        return user

    except (ValidationError, ValueError, SQLAlchemyError, Exception):
        raise
