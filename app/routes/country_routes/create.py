from flask import request, Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import ValidationError

from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope

from utils.logs_handler import log_err

ERR_MSG = 'Error occurred while creating Country record'


@country_bp.route("", methods=['POST'])
def create_country_handler() -> Response:
    try:
        request_data = request.get_json()

        if not request_data:
            raise ValueError("Request body is required")

        with session_scope() as session:
            country = CountryController.create(request_data, session)

            return create_response(
                data=[("country", country)],
                code=200
            )

    except ValueError as e:
        log_err(f"Value {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=400)

    except ValidationError as e:
        log_err(f"Validation {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=409)

    except SQLAlchemyError as e:
        log_err(f"Data Base {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=500)

    except Exception as e:
        log_err(f"Unexpected {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", "Creation error")], code=500)
