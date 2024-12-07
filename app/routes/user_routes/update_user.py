from flask import request
import logging
from controllers import UserController
from .users_blueprint import users_bp
from utils import create_response
from config import session_scope

@users_bp.route("/<int:id>", methods=['PUT'])
def update_user_handler(id: int) -> tuple:
    """
    Endpoint for updating a user by ID. Receives user data in JSON format
    and updates the user's information in the database.

    Args:
        id (int): The ID of the user to update.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_data = request.get_json()
            response = UserController.update(id, user_data, session)
            return create_response(
                data=[("user", response)],
                code=200
            )

    except Exception as e:
        logging.error(f"Error occurred while updating user ID {id}: {str(e)}")
        return create_response(
            data=[("error", f"Error updating user ID {id}: {str(e)}")],
            code=500
        )
