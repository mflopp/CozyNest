from flask import request
import logging

from controllers.user_controllers import add_user
from config import get_session
from .users_blueprint import users_bp


@users_bp.route("", methods=['POST'])
def create_user_handler() -> tuple:
    """
    Endpoint for creating a new user. Receives user data as JSON and returns
    the result of creating a user in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())

        user_data = request.get_json()
        response, status = add_user(user_data, db)

        return response, status
    except Exception as e:
        logging.error(f"Error occurred while creating user: {str(e)}")
        return {"error": "Error creating user"}, 500
    finally:
        if db:
            db.close()
