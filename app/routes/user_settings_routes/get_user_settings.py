import logging

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

    except Exception as e:
        logging.error(f"Error occurred while retrieving user settings:"
                      f"{str(e)}")
        return create_response(
            data=[(
                "error", f"Error finding user settings: {str(e)}"
            )],
            code=500
        )
