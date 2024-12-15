import logging
from flask import Response, request
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import ValidationError, NoRecordsFound

from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp


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

    except ValidationError as e:
        # Logging validation error
        logging.error(f"Validation Error occurred while updating: {str(e)}")

        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except ValueError as e:
        logging.error(
            f"Value Error occured while updating: {str(e)}",
            exc_info=True
        )
        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except NoRecordsFound as e:
        msg = f"No records found to update with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)

        return create_response(
            data=[("error", msg)],
            code=404
        )

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while updating: {e}"},
            exc_info=True
        )
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except Exception as e:
        # Logging unexpected error with traceback
        logging.error(f"Error occurred while updating country data: {str(e)}")

        # Returning general error response
        return create_response(
            data=[("error", "Error updating country data")],
            code=500
        )
