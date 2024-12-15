import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserSettingsController
from .user_settings_blueprint import user_settings_bp

from utils import create_response
from config import session_scope


@user_settings_bp.route("", methods=['GET'])
def get_user_settings_handler():
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_settings = UserSettingsController.get_all(session)

            if user_settings:
                return create_response(
                    data=[("user settings", user_settings)],
                    code=200
                )

            return "User settings not found", 404

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while retrieving user settings: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while retrieving user settings: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
