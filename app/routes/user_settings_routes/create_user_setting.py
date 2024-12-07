from flask import request
import logging

from controllers.user_controllers import add_user_setting
from config import get_session
from .user_settings_blueprint import user_settings_bp


@user_settings_bp.route("", methods=['POST'])
def create_user_setting_handler() -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())

        user_setting = request.get_json()
        response, status = add_user_setting(user_setting, db)
        print(f"\033[34m ############# create_user_setting_handler: {response}\033[0m")
        return response, status
    except Exception as e:
        logging.error(f"Error occurred while creating user setting: {str(e)}")
        return {"error": "Error creating user setting"}, 500
    finally:
        if db:
            db.close()
            print("\033[34m ############# after closing DB\033[0m")
        print("\033[34m ############# outside cloding DB\033[0m")
