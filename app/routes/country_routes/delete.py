import logging
from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import NoRecordsFound, ValidationError, HasChildError
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("/<int:id>", methods=['DELETE'])
def delete_country_handler(id: int) -> Response:
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

    except ValueError as e:
        logging.error(
            f"Value Error occured while deleting: {str(e)}",
            exc_info=True
        )
        # Returning validation error response
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while deleting: {e}"},
            exc_info=True
        )
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except NoRecordsFound as e:
        # Log unexpected errors with traceback
        msg = f"No records found while deleting country with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=404
        )

    except HasChildError as e:
        # Log unexpected errors with traceback
        msg = f"Error occurred while deleting country with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=409
        )

    except ValidationError as e:
        # Log unexpected errors with traceback
        msg = f"Validation Error occurred while deleting country with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=409
        )

    except Exception as e:
        # Log unexpected errors with traceback
        msg = "An unexpected error occurred while deleting"
        logging.error(f"{msg}: {str(e)}", exc_info=True)
        return create_response(
            data=[("error", msg)],
            code=500
        )
