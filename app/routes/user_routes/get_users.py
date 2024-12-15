import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserController
from .users_blueprint import users_bp

from utils import create_response
from config import session_scope


@users_bp.route("", methods=['GET'])
def get_users_handler() -> list:
    """
    Endpoint for retrieving all users from the database.
    Returns a list of users or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            users = UserController.get_all(session)

            if users:
                return create_response(
                    data=[("users", users)],
                    code=200
                )

            return "Users not found", 404

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while getting users: {str(e)}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while getting users: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
