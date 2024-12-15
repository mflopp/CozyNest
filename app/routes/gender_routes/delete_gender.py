import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import GenderController
from .genders_blueprint import genders_bp
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)

from utils import create_response
from config import session_scope


@genders_bp.route("/<int:id>", methods=['DELETE'])
def delete_gender_handler(id: int) -> tuple:
    """
    Endpoint for deleting a gender by ID. Attempts to delete
    the gender from the database and returns a response indicating
    success or failure.

    Args:
        id (int): The ID of the gender to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            GenderController.delete(id, session)

            return create_response(
                data=[
                    ("info", f"Gender ID {id} deleted successfully")
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
        # Returning validation error response
        return create_response(
            data=[("error", message)],
            code=code
        )

    except SQLAlchemyError as e:
        msg = f"DB error occurred while deleting gender with ID {id}: {e}"
        logging.error(msg, exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Error occurred while deleting gender with ID {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
