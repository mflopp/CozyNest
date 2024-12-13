import logging
from typing import List

from controllers import UserRoleController
from .user_roles_blueprint import user_roles_bp

from utils import create_response
from config import session_scope


@user_roles_bp.route("", methods=['GET'])
def get_user_roles_handler() -> List:
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_roles = UserRoleController.get_all(session)

            if user_roles:
                return create_response(
                    data=[("user roles", user_roles)],
                    code=200
                )

            return "User roles not found", 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user roles: {str(e)}")
        return create_response(
            data=[("error", f"Error finding user roles: {str(e)}")],
            code=500
        )
