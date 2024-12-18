from flask import request
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import AmenityCategoryController
from .amenity_categories_blueprint import amenity_categories_bp
from utils.error_handler import ValidationError

from utils import create_response
from config import session_scope


@amenity_categories_bp.route("/getone", methods=['GET'])
def get_amenity_category_by_name_handler():
    """
    Endpoint for retrieving a user setting by ID. Looks up the user
    in the database and returns the user setting data or a 404 error
    if not found.

    Args:
        id (int): The ID of the user setting to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            amenity_category_data = request.get_json()
            amenity_category = AmenityCategoryController.get_one_by_name(
                amenity_category_data, session
            )

            if amenity_category:
                return create_response(
                    data=[
                        ("amenity category", amenity_category)
                        # ("id", amenity_category.id),
                        # ("categoty", amenity_category.category)
                    ],
                    code=200
                )

            return {"message": "Amenity category not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error occured while fetching an amenity_category: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except ValidationError as e:
        msg = f"Validation error while getting an amenity_category: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Unexpected error while getting an amenity_category: {e}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )
