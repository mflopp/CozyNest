import logging
from flask import request
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from utils.error_handler import ValidationError
from controllers import GenderController
from .genders_blueprint import genders_bp

from utils import create_response
from config import session_scope


@genders_bp.route("", methods=['POST'])
def create_gender_handler() -> Dict:
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

            gender_data = request.get_json()
            gender = GenderController.create(
                gender_data,
                session
            )
            return create_response(
                data=[
                    ("id", gender.id),
                    ("gender", gender.gender),
                    ("description", gender.description)
                ],
                code=200
            )

    except ValidationError as e:
        # Logging validation error
        logging.error(
            f"Validation error while creating a gender: {str(e)}"
        )

        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except ValueError as e:
        logging.error(
            f"Value Error occured while creating a gender: {e}",
            exc_info=True
        )
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while creating a gender: {e}"},
            exc_info=True
        )
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except Exception as e:
        logging.error(f"Error occurred while creating a gender: {str(e)}")
        return create_response(
            data=[("error", f"Error creating a gender: {str(e)}")],
            code=500
        )
