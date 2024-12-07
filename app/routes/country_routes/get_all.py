import logging

from controllers import CountryController
from config import get_session
from .countries_blueprint import country_bp
from flask import make_response, Response
from collections import OrderedDict
import json

from contextlib import contextmanager


@contextmanager
def session_scope():
    """
    Provides a transactional scope for the database session.

    Yields:
        session: The database session.
    """
    session = next(get_session())
    try:
        yield session
    except Exception:
        session.rollback()  # Rollback in case of an exception
        raise
    finally:
        session.close()  # Always close the session


def create_response(data, code) -> Response:
    response_data = OrderedDict(data)
    response_json = json.dumps(
        response_data,
        default=str,
        sort_keys=False
    )
    response = make_response(response_json, code)
    response.headers['Content-Type'] = 'application/json'

    return response


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
