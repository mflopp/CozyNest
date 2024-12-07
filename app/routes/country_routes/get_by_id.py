from flask import request
import logging

from controllers import CountryController
from config import get_session
from .countries_blueprint import country_bp
from flask import make_response
from collections import OrderedDict
import json

@country_bp.route("<int:id>", methods=['GET'])
def get_country_by_id_handler(id: int) -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    session = None

    try:
        session = next(get_session())

        country = CountryController.get_one_by_id(id, session)
        if country:
            response_data = OrderedDict([("country", country)])
            response_json = json.dumps(response_data, default=str, sort_keys=False)
            response = make_response(response_json, 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        return "Users not found", 404
    except Exception as e:
        logging.error(f"Error occurred while getting country data: {str(e)}")
        return {"error": "Error getting country data"}, 500
    finally:
        if session:
            session.close()
            
