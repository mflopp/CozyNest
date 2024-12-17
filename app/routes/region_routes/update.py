import logging
from flask import Response, request
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import ValidationError, NoRecordsFound

from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp

ERR_MSG = "Error occurred while updating Region record"
TRACEBACK = True


@region_bp.route("/<int:id>", methods=['PUT'])
def update_region_handler(id: int) -> Response:
    try:
        new_data = request.get_json()
        if not new_data:
            return create_response(
                data=[("error", "Request body is required")],
                code=400
            )

        with session_scope() as session:
            RegionController.update(id, new_data, session)
            return create_response(
                data=[("info", 'Succesfully updated')],
                code=200
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
