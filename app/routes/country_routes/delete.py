import logging
from flask import Response

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("/<int:id>", methods=['DELETE'])
def delete_country_handler(id: int) -> Response:
    """
    Handle DELETE request to delete a country by its ID.

    Args:
        id (int): ID of the country to be deleted.

    Returns:
        Response: JSON response indicating the success or failure of
                  the operation.

    Raises:
        Logs unexpected exceptions and returns a 500 error response.
    """
    try:
        # Using session_scope context manager for database session
        with session_scope() as session:
            # Call the controller's delete method
            CountryController.delete(id, session)

            # Return the appropriate response
            return create_response(
                data=[("info", f'Deleted Succesfully {id}')],
                code=200
            )
    except Exception as e:
        # Log unexpected errors with traceback
        logging.error(
            f"Error occurred while deleting country with ID {id}: {str(e)}",
            exc_info=True
            )
        return create_response(
            data=[(
                "error",
                "An unexpected error occurred while deleting country data."
            )],
            code=500
        )
