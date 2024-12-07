import logging
from flask import request, Response

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope
from utils.api_error import ValidationError


@country_bp.route("", methods=['POST'])
def create_country_handler() -> Response:
    """
    Handle POST request to create a new country.

    Returns:
        Response: JSON response containing the created country or
        an error message.
    Raises:
        Logs any unexpected exceptions and returns appropriate error responses.
    """
    try:
        # Using session_scope context manager for database session
        with session_scope() as session:
            # Extracting data from the request
            request_data = request.get_json()

            # Creating the country via the controller
            country = CountryController.create(request_data, session)
            if country:
                # Returning success response with created country data
                return create_response(
                    data=[("country", country)],
                    code=200
                )

            # Returning response for unsuccessful creation
            return create_response(
                data=[("message", "Country not created")],
                code=400
            )

    except ValidationError as err:
        # Logging validation error
        logging.error(f"Error occurred while creating country: {str(err)}")

        # Returning validation error response
        return create_response(
            data=[("error", str(err))],
            code=400
        )

    except Exception as e:
        # Logging unexpected error with traceback
        logging.error(f"Error occurred while creating country data: {str(e)}")

        # Returning general error response
        return create_response(
            data=[("error", "Error creating country data")],
            code=500
        )
