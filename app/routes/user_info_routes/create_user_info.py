from flask import request
import logging

from controllers.user_controllers import add_user_info
from config import get_session
from .user_info_blueprint import user_info_bp


@user_info_bp.route("", methods=['POST'])
def create_user_info_handler() -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON
    and returns the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    session = None

    try:
        session = next(get_session())

        user_info = request.get_json()
        response, status = add_user_info(
            user_data=user_info,
            gender_id=user_info['gender_id'],
            user_settings_id=user_info['user_settings_id'],
            session=session
        )

        return response, status
    except Exception as e:
        logging.error(f"Error occurred while creating user info: {str(e)}")
        return {"error": "Error creating user info"}, 500
    finally:
        if session:
            session.close()
