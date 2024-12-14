import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models import User, Gender

from controllers.user_controllers.user_settings_controller.methods import fetch_user_setting
# from controllers.user_controllers.user_info_controller_methods import add_user_info
from controllers.user_controllers.user_role_controller.methods import fetch_user_role

from utils.error_handler import ValidationError


def add_user(user_data: dict, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():
        
            # validating fields
            fields = ['email', 'password', 'phone']

            validate_data(
                session=session,
                Model=User,
                data=user_data,
                required_fields=fields,
                unique_fields=['email', 'phone']
            )

            gender_pre = "Male"

            # Find or create gender before any commits
            gender = get_first_record_by_criteria(
                session, Gender, {"gender": gender_pre}
            )

            # getting UserSettings with default values
            user_settings = {"currency": "USD", "language": "ENG"}
            user_setting = fetch_user_setting(user_settings, session)
            if not user_setting:
                logging.error(f"Error: Default user setitng was not found in the DB: {user_settings}")
                raise ValueError("Failed to get default user settings from the DB")

            # Create UserInfo
            response, status = add_user_info(user_data, gender.id, user_setting.id, session)
            if status != 200:
                logging.error(f"user info was not created, Error: {response}")
                raise ValueError(f"Failed to create user info, Error: {response}")

            user_role = fetch_user_role({"role": 'User'}, session)
            if not user_role:
                logging.error("User role was not provided")
                raise ValueError(f"Failed to add user role")

            # Create the user
            user = User(
                role_id=user_role.id,
                info_id=response,
                email=user_data['email'],
                password=user_data['password'],
                phone=user_data['phone'],
                created_at=func.now(),
                updated_at=func.now()
            )

            add_record(session, user, 'user')

        # commit the transaction after 'with' block
        session.flush()            
        logging.info(f"User created successfully with ID {user.id}")
        return user
    
    except ValidationError:
        raise
    except (ValueError, Exception) as e:
        logging.error(f"Error creating user: {str(e)}")
        raise
