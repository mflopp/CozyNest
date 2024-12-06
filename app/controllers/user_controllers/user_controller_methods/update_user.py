from sqlalchemy.orm import Session
import logging
from datetime import datetime

from models.users import UserInfo, UserRole, Gender
from controllers.controller_utils import get_first_record_by_criteria
from controllers.user_controllers.user_settings_controller_methods import add_user_setting
from .get_only_user import fetch_only_user


def update_user_data(id: int, user_data: dict, session: Session):
    errors = []

    try:
        # Start a new transaction
        with session.begin_nested():
        
            # Fetch the user by ID
            user = fetch_only_user(id, session)
            if not user:
                return {"error": "User not found"}, 404

            # Update user fields
            if 'email' in user_data:
                user.email = user_data['email']
            if 'password' in user_data:
                user.password = user_data['password']
            if 'phone' in user_data:
                user.phone = user_data['phone']

            # Fetch and update UserInfo (replace to functions from userInfo models)
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
                    try:
                        user_info.birthdate = datetime.strptime(user_data['birthdate'], "%d.%m.%Y").date()
                    except ValueError:
                        errors.append("Invalid birthdate format. Use DD.MM.YYYY")

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
                if 'currency' not in user_data:
                    user_data['currency'] = user_info.settings.currency
                if 'language' not in user_data:
                    user_data['language'] = user_info.settings.language


                # Check if default UserSettings exists, if not, create it
                response, status = add_user_setting(user_data, session)
                if status != 200:
                    logging.error(f"user setting was not provided, Error: {response}")
                    raise ValueError(f"User setting was not provided, error: {response}")

                user_setting = response["id"]


                user_info.user_settings_id = user_setting

            # Fetch and update UserRole (replace with Roles methods)
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
    except (ValueError, Exception) as e:
        logging.error(str(e))
        return {"error": "Error updating user", "details": str(e)}, 500
