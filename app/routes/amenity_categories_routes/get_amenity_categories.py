from flask import Response
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import AmenityCategoryController
from .amenity_categories_blueprint import amenity_categories_bp
# from utils.error_handler import NoRecordsFound, ValidationError

# from utils.logs_handler import log_err
from utils import create_response
from config import session_scope


@amenity_categories_bp.route("", methods=['GET'])
def get_amenity_categories_handler() -> Response:
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            amenity_categories = AmenityCategoryController.get_all(session)

            if amenity_categories:
                return create_response(
                    data=[("amenity categories", amenity_categories)],
                    code=200
                )

            return {"message": "Amenity categories not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error occured while fetching amenity categories: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Error occurred while fetching amenity categories: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )
