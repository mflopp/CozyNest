import logging
from controllers import UserController
from .users_blueprint import users_bp
from utils import create_response
from config import session_scope

@users_bp.route("", methods=['GET'])
def get_users_handler() -> list:
    """
    Endpoint for retrieving all users from the database.
    Returns a list of users or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            users = UserController.get_all(session)
            
            if users:
                return create_response(
                    data=[("users", users)],
                    code=200
                )

            return "Users not found", 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving users: {str(e)}")
        return create_response(
            data=[("error", f"Error finding users: {str(e)}")],
            code=500
        )

