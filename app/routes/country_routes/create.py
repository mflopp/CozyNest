import logging
from flask import request, Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import ValidationError

from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("", methods=['POST'])
def create_country_handler() -> Response:
    try:
        request_data = request.get_json()
        if not request_data:
            return create_response(
                data=[("error", "Request body is required")],
                code=400
            )

        # Using session_scope context manager for database session
        with session_scope() as session:
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

    except ValidationError as e:
        # Logging validation error
        logging.error(f"Error occurred while creating country: {str(e)}")

        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except ValueError as e:
        logging.error(
            f"Value Error occured while creating: {str(e)}",
            exc_info=True
        )
        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while creating: {e}"},
            exc_info=True
        )
        return create_response(
            data=[("error", str(e))],
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
