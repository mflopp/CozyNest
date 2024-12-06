import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from controllers.general_controllers import add_record
from models.users import User, UserInfo, UserRole, Gender
from controllers.controller_utils.validations import validate_data
from controllers.user_controllers.user_settings_controller_methods import add_user_setting

from controllers.controller_utils import get_first_record_by_criteria


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
                unique_fields=fields
            )
            # Validate required fields
            # required_fields = [
            #     'email', 'password', 'phone'
            # ]

            # for field in required_fields:
            #     if field not in user_data or not user_data[field]:
            #         errors.append(f"{field} is required")

            # if errors:
            #     return {"error": "Validation failed", "details": errors}, 400

            # # Check for unique email
            # if get_first_record_by_criteria(
            #     session, User, {"email": user_data['email']}
            # ):
            #     errors.append(f"Email {user_data['email']} already exists")

            # # Check for unique phone
            # if get_first_record_by_criteria(
            #     session, User, {"phone": user_data['phone']}
            # ):
            #     errors.append(f"Phone {user_data['phone']} already exists")

            # if errors:
            #     return {"error": "Validation failed", "details": errors}, 400

            gender_pre = "Male"

            # Find or create gender before any commits
            gender = get_first_record_by_criteria(
                session, Gender, {"gender": gender_pre}
            )

            # adding UserSettings with default values (if it doesn't exist)
            user_settings = {"currency": "USD", "language": "ENG"}
            response, status = add_user_setting(user_settings, session)
            if status != 200:
                logging.error(f"user setting was not provided, Error: {response}")
                raise ValueError(f"User setting was not provided, error: {response}")
            user_setting = response["id"]

            # Create UserInfo
            user_info = UserInfo(
                gender_id=gender.id,    # may cause trouble
                user_settings_id=user_setting,
                first_name='first_name',
                last_name='last_name',
                birthdate=None,
                created_at=func.now(),
                updated_at=func.now()
            )

            response, status = add_record(session, user_info, 'user info')
            if status != 200:
                logging.error(f"user info was not created, Error: {response}")
                raise ValueError(f"Failed to create user info, Error: {response}")
            
            user_role = get_first_record_by_criteria(
                            session,
                            UserRole,
                            {"role": 'User'}
                        )

            # Create the user
            user = User(
                role_id=user_role.id,
                info_id=user_info.id,
                email=user_data['email'],
                password=user_data['password'],
                phone=user_data['phone'],
                created_at=func.now(),
                updated_at=func.now()
            )
            # session.add(user)
            # session.commit()
            add_record(session, user, 'user')
            if status != 200:
                logging.error(f"user was not created, Error: {response}")
                raise Exception(f"Failed to create user, Error: {response}")
            
            logging.info(f"User created successfully with ID {user.id}")
            return (
                {"message": "User created successfully", "user_id": user.id},
                200
            )

    except (ValueError, Exception) as e:
        logging.error(str(e))
        return {"error": "Error creating user", "details": str(e)}, 500
