import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserController
from .users_blueprint import users_bp

from utils import create_response
from config import session_scope


@users_bp.route("/only/<int:id>", methods=['GET'])
def get_only_user_handler(id: int) -> tuple:
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

            user = UserController.get_minimum(id, session)
            if user:
                return create_response(data=[
                    ("user_id", user.id),
                    ("email", user.email),
                    # Consider excluding sensitive data (password)
                    ("password", user.password),
                    ("phone", user.phone),
                    ("role", user.role_id),
                    ("deleted", user.deleted),
                    ("created_at", user.created_at),
                    ("updated_at", user.updated_at)
                ],
                    code=200
                )

            return {"error": f"User ID {id} not found"}, 404

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while getting user ID {id}: {str(e)}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while getting a user ID {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
