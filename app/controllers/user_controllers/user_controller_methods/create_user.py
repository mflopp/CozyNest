import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.users import User, UserInfo, UserRole, Gender, UserSettings

from controllers.controller_utils import get_first_record_by_criteria


def add_user(user_data: dict, session: Session):
    errors = []

    try:
        # Validate required fields
        required_fields = [
            'email', 'password', 'phone'
        ]

        for field in required_fields:
            if field not in user_data or not user_data[field]:
                errors.append(f"{field} is required")

        if errors:
            return {"error": "Validation failed", "details": errors}, 400

        # Check for unique email
        if get_first_record_by_criteria(
            session, User, {"email": user_data['email']}
        ):
            errors.append(f"Email {user_data['email']} already exists")

        # Check for unique phone
        if get_first_record_by_criteria(
            session, User, {"phone": user_data['phone']}
        ):
            errors.append(f"Phone {user_data['phone']} already exists")

        if errors:
            return {"error": "Validation failed", "details": errors}, 400
        
        gender_pre = "Male"

        # Find or create gender before any commits
        gender = get_first_record_by_criteria(
            session, Gender, {"gender": user_data[gender_pre]}
        )

        # # Parse the birthdate
        # birthdate = user_data.get('birthdate')
        # if birthdate:
        #     try:
        #         birthdate = datetime.strptime(birthdate, "%d.%m.%Y").date()
        #     except ValueError:
        #         errors.append("Invalid birthdate format. Use DD.MM.YYYY")
        #         return {"error": "Validation failed", "details": errors}, 400
            
        # Start a new transaction
        session.begin_nested()
        
        # Default UserSettings
        default_currency = 'USD'
        default_language = 'ENG'

        # Check if default UserSettings exists, if not, create it
        user_settings = get_first_record_by_criteria(
            session,
            UserSettings,
            {"currency": default_currency, "language": default_language}
        )
        if not user_settings:
            user_settings = UserSettings(
                currency=default_currency, language=default_language
            )
            session.add(user_settings)
            session.commit()

        # Create UserInfo
        user_info = UserInfo(
            gender_id=gender.id, # may cause trouble
            user_settings_id=1, # may cause trouble
            first_name='first_name',
            last_name='last_name',
            birthdate = None,
            created_at=func.now(),
            updated_at=func.now()
        )
        # user_info = UserInfo(
        #     gender_id=gender.id,
        #     user_settings_id=user_settings.id,
        #     first_name=user_data['first_name'],
        #     last_name=user_data['last_name'],
        #     birthdate=user_data.get('birthdate'),
        #     created_at=func.now(),
        #     updated_at=func.now()
        # )
        session.add(user_info)
        session.commit()

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
        session.add(user)
        session.commit()

        logging.info(f"User created successfully with ID {user.id}")
        return {"message": "User created successfully", "user_id": user.id}, 200
    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error creating user", "details": str(e)}, 500
