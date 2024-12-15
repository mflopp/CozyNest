import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserInfoController
from .user_info_blueprint import user_info_bp
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)

from utils import create_response
from config import session_scope


@user_info_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_info_handler(id: int) -> tuple:
    """
    Endpoint for deleting a user info by ID. Attempts to delete the user info
    from the database and returns a response indicating success or failure.

    Args:
        id (int): The ID of the user info to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            UserInfoController.delete(id, session)

            return create_response(
                data=[
                    ("info", f"User info ID {id} deleted successfully")
                ],
                code=200
            )

    except NoRecordsFound as e:
        message, code = e.args  # Unpacking the tuple
        logging.error(f"{message}", exc_info=True)
        return create_response(
            data=[("error", message)],
            code=code
        )

    except HasChildError as e:
        message, code = e.args  # Unpacking the tuple
        logging.error(f"{message}", exc_info=True)
        return create_response(
            data=[("error", message)],
            code=code
        )

    except SQLAlchemyError as e:
        msg = f"DB error occurred while deleting user info with ID {id}: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Error occurred while deleting user info with ID {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
