import logging
from controllers.user_controllers import fetch_user
from config import get_session
from .users_blueprint import users_bp


@users_bp.route("<int:id>", methods=['GET'])
def get_user_handler(id: int) -> tuple:
    """
    Endpoint for retrieving a user by ID. Looks up the user in the database
    and returns the user data or a 404 error if not found.

    Args:
        id (int): The ID of the user to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Call get_session() to get a session
        user = fetch_user(id, db)

        if user:
            return user, 200

        return "User not found", 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user {id}: {str(e)}")
        return "Error finding user", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
