from flask import request, Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import ValidationError, NoRecordsFound
from utils import create_response
from config import session_scope
from utils.logs_handler import log_err
from .regions_blueprint import region_bp

ERR_MSG = 'Error occurred while creating Region record'


@region_bp.route("", methods=['POST'])
def create_region_handler() -> Response:
    try:
        request_data = request.get_json()

        if not request_data:
            raise ValueError("Request body is required")

        with session_scope() as session:
            region = RegionController.create(request_data, session)

            return create_response(
                data=[("region", region)],
                code=200
            )

    except ValueError as e:
        log_err(f"Value {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=400)

    except NoRecordsFound as e:
        log_err(f"NoRecordsFound {ERR_MSG}:{str(e)}")
        return create_response(data=[("error", str(e))], code=404)

    except ValidationError as e:
        log_err(f"Validation {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=409)

    except SQLAlchemyError as e:
        log_err(f"Data Base {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=500)

    except Exception as e:
        log_err(f"Unexpected {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", "Creation error")], code=500)
