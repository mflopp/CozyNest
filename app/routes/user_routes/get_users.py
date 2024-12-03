import logging
from controllers.user_controllers import fetch_users
from config import get_session
from .users_blueprint import users_bp


@users_bp.route("", methods=['GET'])
def get_users_handler() -> tuple:
    """
    Endpoint for retrieving all users from the database.
    Returns a list of users or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Call get_session() to get a session
        users = fetch_users(db)

        if users:
            return {"users": users}, 200

        return "Users not found", 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving users: {str(e)}")
        return "Error finding users", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
