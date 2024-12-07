from flask import make_response
import logging
from controllers.user_controllers import fetch_user_info
from config import get_session
from .user_info_blueprint import user_info_bp
from collections import OrderedDict
import json

@user_info_bp.route("<int:id>", methods=['GET'])
def get_user_info_handler(id: int) -> tuple:
    """
    Endpoint for retrieving a user setting by ID. Looks up the user in the database
    and returns the user setting data or a 404 error if not found.

    Args:
        id (int): The ID of the user setting to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Call get_session() to get a session
        user_info = fetch_user_info(id, db)

        if user_info:
            # Convert UserSettings object to OrderedDict
            user_info_dict = OrderedDict([
                ("id", user_info.id),
                ("gender_id", user_info.gender_id),
                ("user_settings_id", user_info.user_settings_id),
                ("first_name", user_info.first_name),
                ("last_name", user_info.last_name),
                ("birthdate", user_info.birthdate),
                ("created_at", user_info.created_at),
                ("updated_at", user_info.updated_at)
            ])

    
            response_json = json.dumps(user_info_dict, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return {"message": f"User setting ID {id} not found"}, 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user setting {id}: {str(e)}")
        return "Error finding user setting", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
