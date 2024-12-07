import logging
from controllers.user_controllers import fetch_user_infos
from config import get_session
from .user_info_blueprint import user_info_bp
from flask import make_response
from collections import OrderedDict
import json

@user_info_bp.route("", methods=['GET'])
def get_user_infos_handler() -> tuple:
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Call get_session() to get a session
        user_infos = fetch_user_infos(db)

        if user_infos:
            response_data = OrderedDict([("user infos", user_infos)])
            response_json = json.dumps(response_data, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return "User infos not found", 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user infos: {str(e)}")
        return "Error finding user infos", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
