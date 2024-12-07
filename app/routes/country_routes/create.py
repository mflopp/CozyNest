from flask import request
import logging

from controllers import CountryController
from config import get_session
from .countries_blueprint import country_bp


@country_bp.route("", methods=['POST'])
def create_country_handler() -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    session = None

    try:
        session = next(get_session())

        country = request.get_json()
        response, status = CountryController.create(country, session)

        return response, status
    except Exception as e:
        logging.error(f"Error occurred while creating country data: {str(e)}")
        return {"error": "Error creating country data"}, 500
    finally:
        if session:
            session.close()
