import logging
from flask import request
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from utils.error_handler import ValidationError
from controllers import AmenityCategoryController
from .amenity_categories_blueprint import amenity_categories_bp

from utils import create_response
from config import session_scope


@amenity_categories_bp.route("", methods=['POST'])
def create_amenity_category_handler() -> Dict:
    """
    Endpoint for creating a new gender. Receives user
    data as JSON and returns
    the result of creating a gender in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            amenity_category_data = request.get_json()
            amenity_category = AmenityCategoryController.create(
                amenity_category_data,
                session
            )
            return create_response(
                data=[
                        ("amenity category", amenity_category)
                        # ("id", amenity_category.id),
                        # ("categoty", amenity_category.category)
                ],
                code=200
            )

    except ValidationError as e:
        # Logging validation error
        msg = f"Validation error while creating an amenity category: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)

        # Returning validation error response
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except ValueError as e:
        msg = f"Value Error occured while creating an amenity category: {e}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except SQLAlchemyError as e:
        msg = f"DB error occurred while creating an amenity category: {e}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=400
        )

    except Exception as e:
        msg = f"Error occurred while creating an amenity category: {str(e)}"
        logging.error(msg, exc_info=True, stack_info=True, stacklevel=2)
        return create_response(
            data=[("error", msg)],
            code=500
        )
