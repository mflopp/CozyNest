from flask import request
import logging
from controllers.user_controllers import update_user_data
from config import get_session
from .users_blueprint import users_bp


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
    db = None

    try:
        db = next(get_session())  # Get a session
        user_data = request.get_json()
        response = update_user_data(id, user_data, db)

        return response, 200
    except Exception as e:
        logging.error(f"Error occurred while updating user {id}: {str(e)}")
        return "Error updating user", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
