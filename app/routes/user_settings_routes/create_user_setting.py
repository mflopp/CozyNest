import logging
from flask import request
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from utils.error_handler import ValidationError
from controllers import UserSettingsController
from .user_settings_blueprint import user_settings_bp

from utils import create_response
from config import session_scope


@user_settings_bp.route("", methods=['POST'])
def create_user_setting_handler() -> Dict:
    """
    Endpoint for creating a new user setting. Receives user
    data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            user_setting_data = request.get_json()
            user_setting = UserSettingsController.create(
                user_setting_data,
                session
            )
            return create_response(
                data=[
                    ("id", user_setting.id),
                    ("currency", user_setting.currency),
                    ("language", user_setting.language)
                ],
                code=200
            )

    except ValidationError as e:
        msg = f"Validation error while creating a user setting: {str(e)}"
        # Logging validation error
        logging.error(msg)

        # Returning validation error response
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except ValueError as e:
        msg = f"Value Error occured while creating a user setting: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while creating a user setting: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while creating user a setting: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
