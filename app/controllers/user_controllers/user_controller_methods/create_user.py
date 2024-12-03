import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.users import User, UserInfo, UserRole, Gender, UserSettings


def get_first_record_by_criteria(
    session: Session,
    Model: type,
    filter_criteria: dict
) -> object | None:
    """Retrieve the first record from the database that matches
    the given criteria."""
    return session.query(Model).filter_by(**filter_criteria).first()


def add_user(user_data: dict, session: Session):
    errors = []

    try:
        # Validate required fields
        required_fields = [
            'email', 'password',
            'first_name', 'last_name',
            'gender', 'phone'
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

        # Find or create gender before any commits
        gender = get_first_record_by_criteria(
            session, Gender, {"gender": user_data["gender"]}
        )

        if not gender:
            errors.append(f"Gender {user_data['gender']} not found")
            return {"error": "Validation failed", "details": errors}, 400

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
            gender_id=gender.id,
            user_settings_id=user_settings.id,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            birthdate=user_data.get('birthdate'),
            created_at=func.now(),
            updated_at=func.now()
        )
        session.add(user_info)
        session.commit()

        # Determine user role
        if 'role' in user_data and user_data['role'] == 'Owner':
            user_role = get_first_record_by_criteria(
                session,
                UserRole,
                {"role": 'Owner'}
            )
            # -- this part may be unnecessary
            if not user_role:
                user_role = UserRole(
                    role='Owner',
                    description='Owner of the property role'
                )
                session.add(user_role)
                session.commit()
        else:
            user_role = get_first_record_by_criteria(
                session,
                UserRole,
                {"role": 'User'}
            )

            # -- this part may be unnecessary
            if not user_role:
                user_role = UserRole(
                    role='User',
                    description='Regular user role'
                )
                session.add(user_role)
                session.commit()

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
        return {"message": "User created successfully", "user_id": user.id}
    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error creating user", "details": str(e)}, 500
