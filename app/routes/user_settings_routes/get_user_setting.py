from flask import request, make_response
import logging
from controllers.user_controllers import fetch_user_setting
from config import get_session
from .user_settings_blueprint import user_settings_bp
from collections import OrderedDict
import json

@user_settings_bp.route("/getone", methods=['GET'])
def get_user_setting_handler() -> tuple:
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
        user_setting = request.get_json()
        user_setting = fetch_user_setting(user_setting, db)
        
        if user_setting:
            # Convert UserSettings object to OrderedDict
            user_setting_dict = OrderedDict([
                ("id", user_setting.id),
                ("currency", user_setting.currency),
                ("language", user_setting.language)
            ])
            
            response_json = json.dumps(user_setting_dict, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return {"message": "User setting not found"}, 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user setting: {str(e)}")
        return {"message": "Error finding user setting"}, 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
