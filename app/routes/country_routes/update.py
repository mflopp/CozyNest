from flask import request, Response
import logging

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("/<int:id>", methods=['PUT'])
def update_country_handler(id: int) -> Response:
    """
    Handle PUT request to update an existing country by its ID.

    Args:
        id (int): ID of the country to update.

    Returns:
        Response: JSON response containing a success or error message.

    Raises:
        Logs unexpected exceptions and returns a 500 error response.
    """
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
            message, status = CountryController.update(id, new_data, session)
            return create_response(
                data=[("info", message)],
                code=status
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
