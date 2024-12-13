from flask import request, Response
import logging

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("/<int:id>", methods=['PUT'])
def update_country_handler(id: int) -> Response:
    try:
        # Extract new data from the request
        new_data = request.get_json()
        if not new_data:
            return create_response(
                data=[("error", "Request body is required")],
                code=400
            )

        # Using session_scope context manager for database session
        with session_scope() as session:
            CountryController.update(id, new_data, session)
            return create_response(
                data=[("info", 'Succesfully updated')],
                code=200
            )

    except KeyError as e:
        logging.error(
            f"Key error occurred while updating country ID {id}: {str(e)}",
            exc_info=True
        )
        return create_response(
            data=[("error", "Invalid data format or missing fields")],
            code=400
        )

    except Exception as e:
        logging.error(
            f"Unexpected error occurred while updating country: {str(e)}",
            exc_info=True
        )
        return create_response(
            data=[("error", "Error updating country data")],
            code=500
        )
