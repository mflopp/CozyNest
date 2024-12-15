import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserController
from .users_blueprint import users_bp

from utils import create_response
from config import session_scope


@users_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_handler(id: int) -> list:
    """
    Endpoint for deleting a user by ID. Attempts to delete the user from
    the database and returns a response indicating success or failure.

    Args:
        id (int): The ID of the user to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            response, status = UserController.delete(id, session)

            return response, status

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while deleting user ID {id}: {str(e)}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while deleting user ID {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
