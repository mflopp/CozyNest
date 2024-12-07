from flask import request
import logging

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope
from utils.api_error import ValidationError

@country_bp.route("", methods=['POST'])
def create_country_handler() -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            country_data = request.get_json()
            country = CountryController.create(country_data, session)
            if country:
                return create_response(
                    data=[("country", country)],
                    code=200
                )
            else:
                return create_response(
                    data=[("message", "Country not created")],
                    code=400
                )
                
    except ValidationError as err:
        logging.error(f"Error occurred while creating country: {str(err)}")
        return create_response(
            data=[("error", str(err))],
            code=400
        )
    
    except Exception as e:
        logging.error(f"Error occurred while creating country data: {str(e)}")
        return create_response(
            data=[("error", "Error creating country data")],
            code=500
        )