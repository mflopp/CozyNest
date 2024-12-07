import logging
from flask import Response

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("", methods=['GET'])
def get_countries_handler() -> Response:
    """
    Handle GET request to retrieve a list of countries.

    Returns:
        Response: JSON response containing the list of countries or
                  an error message.
    Raises:
        Logs any unexpected exceptions occurring during the process.
    """
    try:
        # Using session_scope context manager for database session
        with session_scope() as session:
            # Fetch all countries
            countries = CountryController.get_all(session)

            if countries:
                # Returning the response with countries data
                return create_response(
                    data=[("countries", countries)],
                    code=200
                )

            # Return response when no countries are found
            return create_response(
                data=[("message", "Countries not found")],
                code=404
            )
    except Exception as e:
        # Logging the exception with traceback
        logging.error(
            f"Error occurred while retrieving country data: {str(e)}"
        )

        # Returning an error response
        return create_response(
            data=[("error", "Error retrieving country data")],
            code=500
        )
