from flask import request
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserController
from utils.error_handler import ValidationError
from .users_blueprint import users_bp

from utils import create_response
from config import session_scope


@users_bp.route("", methods=['POST'])
def create_user_handler() -> tuple:
    """
    Endpoint for creating a new user. Receives user data as JSON and returns
    the result of creating a user in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            user_data = request.get_json()
            user = UserController.create(user_data, session)
            return create_response(
                data=[
                    ("message", "user successfully created"),
                    ("id", user.id),
                    ("email", user.email),
                    ("password", user.password),
                    ("phone", user.phone),
                    ("role_id", user.role_id),
                    ("info_id", user.info_id)
                    ],
                code=200
            )

    except ValidationError as e:
        # creating validation error message
        msg = f"Validation error while creating a user: {str(e)}"
        logging.error(msg)

        # Returning validation error response
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except ValueError as e:
        logging.error(str(e), exc_info=True)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        msg = f"Data Base error occurred while creating a user: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while creating a user: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
