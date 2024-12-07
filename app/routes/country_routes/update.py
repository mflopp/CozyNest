from flask import request
import logging

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope

@country_bp.route("/<int:id>", methods=['PUT'])
def update_country_handler(id: int) -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            new_data = request.get_json()
            message, status = CountryController.update(id, new_data, session)
            return create_response(
                data=[("info", message)],
                code=status
            )
    except Exception as e:
        logging.error(f"Error occurred while updating country data: {str(e)}")
        return create_response(
            data=[("error", "Error updating country data")],
            code=500
        )
