import logging
from flask import request, Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import ValidationError, NoRecordsFound

from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp

ERR_MSG = 'Error occurred while creating Region record'
TRACEBACK = True


@region_bp.route("", methods=['POST'])
def create_region_handler() -> Response:
    try:
        request_data = request.get_json()
        if not request_data:
            return create_response(
                data=[("error", "Request body is required")],
                code=400
            )

        with session_scope() as session:
            region = RegionController.create(request_data, session)
            if region:
                return create_response(
                    data=[("region", region)],
                    code=200
                )

            # Returning response for unsuccessful creation
            return create_response(
                data=[("message", "Region not created")],
                code=400
            )

    except ValueError as e:
        logging.error(f"Value {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(data=[("error", str(e))], code=400)

    except SQLAlchemyError as e:
        logging.error(f"Data Base {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(data=[("error", str(e))], code=400)

    except NoRecordsFound as e:
        logging.error(f"NoRecordsFound {ERR_MSG}:{str(e)}", exc_info=TRACEBACK)
        return create_response(data=[("error", str(e))], code=404)

    except ValidationError as e:
        logging.error(f"Validation {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(data=[("error", str(e))], code=409)

    except Exception as e:
        logging.error(f"Unexpected {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(data=[("error", ERR_MSG)], code=500)
