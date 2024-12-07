import logging
from controllers import UserController
from .users_blueprint import users_bp
from collections import OrderedDict
from utils import create_response
from config import session_scope

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
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            
            user = UserController.get_one(id, session)
            if user:
                return create_response(
                    data=[
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
                ],
                    code=200
                )

            return {"error": f"User ID {id} not found"}, 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user {id}: {str(e)}")
        return create_response(
            data=[("error", f"Error finding user: {str(e)}")],
            code=500
        )

