import logging
from controllers.user_controllers import fetch_users
from config import get_session
from .users_blueprint import users_bp
from flask import make_response
from collections import OrderedDict
import json

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
            response_data = OrderedDict([("users", users)])
            response_json = json.dumps(response_data, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return "Users not found", 404
    except Exception as e:
        print ("exception fetching users")
        logging.error(f"Error occurred while retrieving users: {str(e)}")
        return "Error finding users", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
