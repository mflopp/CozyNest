from flask import request
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserInfoController
from .user_info_blueprint import user_info_bp
from utils.error_handler import ValidationError

from utils import create_response
from config import session_scope


@user_info_bp.route("/<int:id>", methods=['PUT'])
def update_user_info_handler(id: int) -> tuple:
    """
    Endpoint for updating a user by ID. Receives user data in JSON format
    and updates the user's information in the database.

    Args:
        id (int): The ID of the user to update.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_data = request.get_json()

            UserInfoController.update(id, user_data, session)

            msg = f"User info with ID {id} updated successfully"
            logging.info(msg)
            return create_response(
                data=[("message", msg)],
                code=200
            )

    except (ValueError, ValidationError) as e:
        msg = f"Unable to update user info with ID {id}: {e}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except SQLAlchemyError as e:
        msg = f"DB error occurred while updating user info ID {id}: {str(e)}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while updating user info ID {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
