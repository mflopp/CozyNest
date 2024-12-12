import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserSettingsController
from .user_settings_blueprint import user_settings_bp
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)

from utils import create_response
from config import session_scope


@user_settings_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_setting_handler(id: int) -> tuple:
    """
    Endpoint for deleting a user setting by ID. Attempts to delete
    the user setting from the database and returns a response indicating
    success or failure.

    Args:
        id (int): The ID of the user setting to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            UserSettingsController.delete(id, session)

            return create_response(
                data=[
                    ("info", f"User ID {id} setting deleted successfully")
                ],
                code=200
            )

    except NoRecordsFound as no_record:
        message, code = no_record.args  # Unpacking the tuple
        logging.error(f"User setting ID {id} not found", exc_info=True)
        return create_response(
            data=[("error", message)],
            code=code
        )

    except HasChildError as child_error:
        message, code = child_error.args  # Unpacking the tuple
        logging.error(
            f"Impossible to delete user setting with ID {id}. "
            "Records has child records", exc_info=True
        )
        # Returning validation error response
        return create_response(
            data=[("error", message)],
            code=code
        )

    except SQLAlchemyError as err:
        logging.error(
            {f"Data Base error occurred while deleting: {err}"},
            exc_info=True
        )
        return create_response(
            data=[(
                "error",
                f"DB error occurred while deleting user setting with ID {id}: "
                f"{str(err)}"
            )],
            code=500
        )

    except Exception as e:
        logging.error(
            f"Error occurred while deleting user setting {id}: {str(e)}"
        )
        return create_response(
            data=[(
                "error",
                f"Error deleting user setting with ID {id}: {str(e)}"
            )],
            code=500
        )
