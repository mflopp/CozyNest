import logging
from flask import  Response
from controllers import CountryController
from .countries_blueprint import country_bp

from utils import create_response
from config import session_scope


@country_bp.route("", methods=['GET'])
def get_countries_handler() -> Response:
    """
    Handles the GET request to retrieve a list of countries.

    Returns:
        Response: A JSON response containing the list of countries or
                  an error message.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            countries = CountryController.get_all(session)

            if countries:
                return create_response(
                    data=[("countries", countries)],
                    code=200
                )
            else:
                return create_response(
                    data=[("message", "Countries not found")],
                    code=404
                )
    except Exception as e:
        logging.error(
            f"Error occurred while retrieving country data: {str(e)}"
        )

        return create_response(
            data=[("error", "Error retrieving country data")],
            code=500
        )
