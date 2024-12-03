import logging
from controllers.user_controllers import del_user
from config import get_session
from .users_blueprint import users_bp


@users_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_handler(id: int) -> tuple:
    """
    Endpoint for deleting a user by ID. Attempts to delete the user from
    the database and returns a response indicating success or failure.

    Args:
        id (int): The ID of the user to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Get a session
        response, status = del_user(id, db)

        return response, status
    except Exception as e:
        logging.error(f"Error occurred while deleting user {id}: {str(e)}")
        return {"error": "Error deleting user"}, 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
