from flask import request
import logging

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

    except ValidationError as err:
        logging.error(f"Error occurred while creating country: {str(err)}")
        return create_response(
            data=[("error", str(err))],
            code=400
        )

    except Exception as e:
        logging.error(f"Error occurred while creating user: {str(e)}")
        return create_response(
            data=[("error", f"Error creating user: {str(e)}")],
            code=500
        )
