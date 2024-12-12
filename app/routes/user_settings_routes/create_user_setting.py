import logging
from flask import request
from sqlalchemy.exc import SQLAlchemyError

from utils.error_handler import ValidationError
from controllers import UserSettingsController
from .user_settings_blueprint import user_settings_bp
from utils import create_response
from config import session_scope


@user_settings_bp.route("", methods=['POST'])
def create_user_setting_handler() -> tuple:
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

            user_settings = request.get_json()
            user_setting = UserSettingsController.create(
                user_settings,
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

    except ValidationError as val_error:
        # Logging validation error
        logging.error(
            f"Validation error while creating a user setting: {str(val_error)}"
        )

        # Returning validation error response
        return create_response(
            data=[("error", str(val_error))],
            code=400
        )

    except ValueError as value_err:
        logging.error(
            f"Value Error occured while creating a user setting: {value_err}",
            exc_info=True
        )
        return create_response(
            data=[("error", str(value_err))],
            code=400
        )

    except SQLAlchemyError as err:
        logging.error(
            {f"Data Base error occurred while creating a user setting: {err}"},
            exc_info=True
        )
        return create_response(
            data=[("error", str(err))],
            code=400
        )

    except Exception as e:
        logging.error(f"Error occurred while creating user setting: {str(e)}")
        return create_response(
            data=[("error", f"Error creating a user setting: {str(e)}")],
            code=500
        )
