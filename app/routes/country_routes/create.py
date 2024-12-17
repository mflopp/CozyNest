import logging
from flask import request, Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import ValidationError

from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope

ERR_MSG = 'Error occurred while creating Country record'
TRACEBACK = True


@country_bp.route("", methods=['POST'])
def create_country_handler() -> Response:
    try:
        request_data = request.get_json()
        if not request_data:
            return create_response(
                data=[("error", "Request body is required")],
                code=400
            )

        with session_scope() as session:
            country = CountryController.create(request_data, session)
            if country:
                return create_response(
                    data=[("country", country)],
                    code=200
                )

            return create_response(
                data=[("message", "Country not created")],
                code=400
            )

    except ValidationError as e:
        logging.error(f"Validation {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except ValueError as e:
        logging.error(f"Value {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error({f"Data Base {ERR_MSG}: {e}"}, exc_info=TRACEBACK)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except Exception as e:
        logging.error(f"Unexpected {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", "Error creating country data")],
            code=500
        )
