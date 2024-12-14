from flask import request
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import GenderController
from .genders_blueprint import genders_bp
from utils.error_handler import ValidationError

from utils import create_response
from config import session_scope


@genders_bp.route("/getone", methods=['GET'])
def get_gender_by_name_handler():
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
            gender_data = request.get_json()
            gender = GenderController.get_one_by_name(
                gender_data, session
            )

            if gender:
                return create_response(
                    data=[
                        ("id", gender.id),
                        ("gender", gender.gender),
                        ("description", gender.description)
                    ],
                    code=200
                )

            return {"message": "Gender not found"}, 404

    except SQLAlchemyError as e:
        logging.error(f"{e}")
        return create_response(
            data=[("error", f"{str(e)}")],
            code=500
        )

    except ValidationError as e:
        msg = f"Validation error while getting a gender: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        logging.error(f"Unexpected error while getting a gender: {e}")
        return create_response(
            data=[("error", f"Unexpected error while getting a gender: {e}")],
            code=500
        )
