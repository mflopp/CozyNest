from sqlalchemy.orm import Session
import logging

from models.users import Gender
from controllers.user_controllers.user_info_controller_methods import update_user_info, fetch_user_info
from controllers.user_controllers.user_role_controller.methods import fetch_user_role
from controllers.user_controllers.user_settings_controller.methods import update_user_setting
from .get_only_user import fetch_only_user


def update_user_data(id: int, user_data: dict, session: Session):

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
            
            # fetch UserInfo from the DB
            user_info = fetch_user_info(user.info_id, session)
            if not user_info:
                raise ValueError("Error: User info was not provided from the DB")                
            # fetch UserSettings from the DB
            user_setting_id = update_user_setting(user_info.user_settings_id, user_data, session)
            if not user_setting_id:
                user_setting_id = user_info.user_settings_id
            # Fetch UserRole
            if 'role' in user_data:
                role = fetch_user_role (user_data, session)
                if not role:
                    raise ValueError(f"Error: User role {user_data['role']} was not found in the DB")  
                user.role_id = role.id
            # Fetch Gender
            if 'gender' in user_data:
                gender = get_first_record_by_criteria(
                    session, Gender, {"gender": user_data["gender"]}
                )
                if gender:
                    gender_id = gender.id
                else:
                    raise ValueError(f"Error: User gender {user_data['gender']} was not found in the DB")
            else:
                gender_id = user_info.gender_id

            # Fetch and update UserInfo (replace to functions from userInfo models)
            update_user_info(user_info.id, user_data, gender_id, user_setting_id, session)
               

        # Commit the changes
        session.flush()
        logging.info(f"User with ID {id} updated successfully")
        return {f"User with ID {id} updated successfully"}
    except (ValueError, Exception) as e:
        raise
