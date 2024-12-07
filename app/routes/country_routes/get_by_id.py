import logging
from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope

@country_bp.route("/<int:id>", methods=['GET'])
def get_country_by_id_handler(id: int) -> tuple:
    """
    Endpoint for creating a new user setting. Receives user data as JSON and returns
    the result of creating a user setting in the database.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            country = CountryController.get_one_by_id(id, session)
            if country:
                return create_response(
                    data=[("countries", country)],
                    code=200
                )
            else:
                return create_response(
                    data=[("message", "Countries not found")],
                    code=404
                )

    except Exception as e:
        logging.error(f"Error occurred while getting country data: {str(e)}")
        return create_response(
            data=[("error", "Error getting country data")],
            code=500
        )
