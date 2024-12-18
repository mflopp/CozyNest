from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import CountryController
from utils.error_handler import NoRecordsFound, ValidationError
from utils import create_response
from config import session_scope
from utils.logs_handler import log_err

from .countries_blueprint import country_bp

ERR_MSG = 'Error occurred while fetching Country record'


@country_bp.route("/<int:id>", methods=['GET'])
def get_country_handler(id: int) -> Response:
    try:
        with session_scope() as session:
            country = CountryController.get_country(id, session)

            return create_response(
                data=[("countries", country)],
                code=200
            )

    except ValueError as e:
        log_err(f"Value {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=400)

    except NoRecordsFound as e:
        log_err(f"{ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=404)

    except ValidationError as e:
        log_err(f'Validation {ERR_MSG}: {str(e)}')
        return create_response(data=[("error", str(e))], code=409)

    except SQLAlchemyError as e:
        log_err(f"Data Base {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=500)

    except Exception as e:
        log_err(f"Unexpected {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", "Fetching error")], code=500)
