import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import AmenityCategoryController
from .amenity_categories_blueprint import amenity_categories_bp
from utils.error_handler import (
    NoRecordsFound,
    HasChildError
)

from utils import create_response
from config import session_scope


@amenity_categories_bp.route("/<int:id>", methods=['DELETE'])
def delete_amenity_category_handler(id: int) -> tuple:
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
            AmenityCategoryController.delete(id, session)

            return create_response(
                data=[
                    ("info", f"Amenity category ID {id} deleted successfully")
                ],
                code=200
            )

    except NoRecordsFound as e:
        msg, code = e.args  # Unpacking the tuple
        logging.error(f"{msg}", exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=code
        )

    except HasChildError as e:
        msg, code = e.args  # Unpacking the tuple
        logging.error(f"{msg}", exc_info=True, stack_info=True, stacklevel=2)
        # Returning validation error response
        return create_response(
            data=[("error", msg)],
            code=code
        )

    except SQLAlchemyError as e:
        msg = (
            "DB error occurred while deleting amenity category "
            f"with ID {id}: {e}"
        )
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = (
            "Error occurred while deleting amenity category "
            f"with ID {id}: {str(e)}"
        )
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )
