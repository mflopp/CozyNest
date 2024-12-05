from sqlalchemy.orm import Session
import logging

from models.users import User, UserInfo, UserRole, Gender, UserSettings
from controllers.controller_utils import get_first_record_by_criteria


def update_user_data(id: int, user_data: dict, session: Session):
    errors = []

    try:
        # Fetch the user by ID
        user = get_first_record_by_criteria(
            session,
            User,
            {'id': id}
        )
        if not user:
            return {"error": "User not found"}, 404

        # Update user fields
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password = user_data['password']
        if 'phone' in user_data:
            user.phone = user_data['phone']

        # Fetch and update UserInfo
        user_info = get_first_record_by_criteria(
            session,
            UserInfo,
            {'id': user.info_id}
        )
        if not user_info:
            errors.append("User info not found")
        else:
            if 'first_name' in user_data:
                user_info.first_name = user_data['first_name']

            if 'last_name' in user_data:
                user_info.last_name = user_data['last_name']

            if 'birthdate' in user_data:
                user_info.birthdate = user_data['birthdate']

            if 'gender' in user_data:
                gender = get_first_record_by_criteria(
                    session, Gender, {"gender": user_data["gender"]}
                )
                if gender:
                    user_info.gender_id = gender.id
                else:
                    errors.append(f"Gender {user_data['gender']} not found")

        # Update UserSettings
        if 'currency' in user_data or 'language' in user_data:
            currency = user_data.get('currency', user_info.settings.currency)
            language = user_data.get('language', user_info.settings.language)

            user_settings = get_first_record_by_criteria(
                session,
                UserSettings,
                {"currency": currency, "language": language}
            )

            if not user_settings:
                user_settings = UserSettings(currency=currency, language=language)
                db.add(user_settings)
                db.commit()

            user_info.user_settings_id = user_settings.id

        # Fetch and update UserRole
        if 'role' in user_data:
            role = get_first_record_by_criteria(
                session,
                UserRole,
                {"role": user_data['role']}
            )
            if role:
                user.role_id = role.id
            else:
                errors.append(f"Role {user_data['role']} not found")

        # If there are any errors, roll back and return error message
        if errors:
            session.rollback()
            return {"error": "Update failed", "details": errors}, 400

        # Commit the changes
        session.commit()
        logging.info(f"User with ID {id} updated successfully")
        return {"message": "User updated successfully"}
    except Exception as e:
        session.rollback()

        logging.error(str(e))
        return {"error": "Error updating user", "details": str(e)}, 500
