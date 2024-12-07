from flask import request, make_response
import logging
from controllers.user_controllers import fetch_user_role
from config import get_session
from .user_roles_blueprint import user_roles_bp
from collections import OrderedDict
import json

@user_roles_bp.route("/getone", methods=['GET'])
def get_user_role_handler() -> tuple:
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
        user_role = request.get_json()
        user_role = fetch_user_role(user_role, db)
        
        if user_role:
            # Convert UserSettings object to OrderedDict
            user_role_dict = OrderedDict([
                ("id", user_role.id),
                ("role", user_role.role),
                ("description", user_role.description)
            ])
            
            response_json = json.dumps(user_role_dict, default=str, sort_keys=False)
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
