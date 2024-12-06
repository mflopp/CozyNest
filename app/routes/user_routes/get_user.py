from flask import make_response
import logging
from controllers.user_controllers import fetch_user
from config import get_session
from .users_blueprint import users_bp
from collections import OrderedDict
import json

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
            # Transform data to the desired format
            user_data = OrderedDict([
                ("user_id", user.user_id),
                ("email", user.email),
                ("password", user.password),  # Consider excluding sensitive data
                ("first_name", user.first_name),
                ("last_name", user.last_name),
                ("birthdate", user.birthdate.strftime("%d.%m.%Y") if user.birthdate else None),
                ("gender", user.gender),
                ("phone", user.phone),
                ("role", user.user_role),
                ("user_settings", OrderedDict([
                    ("currency", user.currency),
                    ("language", user.language)
                ])),
                ("deleted", user.deleted),
                ("created_at", user.created_at),
                ("updated_at", user.updated_at)
            ])
            response_json = json.dumps(user_data, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return {"error": f"User ID {id} not found"}, 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user {id}: {str(e)}")
        return "Error finding user", 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
