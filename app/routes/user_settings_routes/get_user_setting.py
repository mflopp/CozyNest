from flask import request
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserSettingsController
from .user_settings_blueprint import user_settings_bp

from utils import create_response
from config import session_scope


@user_settings_bp.route("/getone", methods=['GET'])
def get_user_setting_handler():
    """
    Endpoint for retrieving a user setting. Looks up the user
    in the database and returns the user setting data or a 404 error
    if not found.

    Args:
        id (int): The ID of the user setting to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_settings = request.get_json()
            user_setting = UserSettingsController.get_one_by_name(
                user_settings, session
            )

            if user_setting:
                return create_response(
                    data=[
                        ("id", user_setting.id),
                        ("currency", user_setting.currency),
                        ("language", user_setting.language)
                    ],
                    code=200
                )

        return {"message": "User setting not found"}, 404

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while retrieving a user setting: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while retrieving a user setting: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
