import logging
from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import NoRecordsFound, ValidationError
from utils import create_response
from config import session_scope
from .countries_blueprint import country_bp


@country_bp.route("/<int:id>", methods=['GET'])
def get_country_by_id_handler(id: int) -> Response:
    try:
        with session_scope() as session:
            country = CountryController.get_country(id, session)

            if country:
                return create_response(
                    data=[("countries", country)],
                    code=200
                )

            # Handle the case where the country is not found
            return create_response(
                data=[("message", "Countries not found")],
                code=404
            )

    except ValidationError as e:
        msg = f"Validation Error occurred while fetching country with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)

        return create_response(
            data=[("error", msg)],
            code=409
        )

    except NoRecordsFound as e:
        msg = f"No records found while fetching country with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=True)

        return create_response(
            data=[("error", msg)],
            code=404
        )

    except ValueError as e:
        logging.error(
            f"Value Error occured while fetching: {str(e)}",
            exc_info=True
        )

        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error(
            {f"Data Base error occurred while fetching: {e}"},
            exc_info=True
        )

        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except Exception as e:
        msg = "An unexpected error occurred while fetching"
        logging.error(f"{msg}: {str(e)}", exc_info=True)

        return create_response(
            data=[("error", msg)],
            code=500
        )
