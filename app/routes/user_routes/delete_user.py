import logging
from controllers import UserController
from .users_blueprint import users_bp
from utils import create_response
from config import session_scope

@users_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_handler(id: int) -> list:
    """
    Endpoint for deleting a user by ID. Attempts to delete the user from
    the database and returns a response indicating success or failure.

    Args:
        id (int): The ID of the user to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            response, status = UserController.delete(id, session)

            return response, status
    except Exception as e:
        logging.error(f"Error occurred while deleting user {id}: {str(e)}")
        return create_response(
            data=[("error", f"Error deleting user: {str(e)}")],
            code=500
        )
