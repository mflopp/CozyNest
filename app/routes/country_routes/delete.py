import logging

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope

@country_bp.route("/<int:id>", methods=['DELETE'])
def delete_country_handler(id: int) -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            message, status = CountryController.delete(id, session)
            return create_response(
                data=[("info", message)],
                code=status
            )
    except Exception as e:
        logging.error(f"Error occurred while deleteting country data: {str(e)}")
        return create_response(
            data=[("error", "Error deleteting country data")],
            code=500
        )
