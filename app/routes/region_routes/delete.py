import logging
from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import NoRecordsFound, ValidationError, HasChildError
from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp

ERR_MSG = 'Error occurred while deleting Region record'
TRACEBACK = True


@region_bp.route("/<int:id>", methods=['DELETE'])
def delete_region_handler(id: int) -> Response:
    try:
        with session_scope() as session:
            RegionController.delete(id, session)

            return create_response(
                data=[("info", f'Deleted Succesfully {id}')],
                code=200
            )

    except ValueError as e:
        logging.error(f"Value {ERR_MSG}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except SQLAlchemyError as e:
        logging.error(f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", str(e))],
            code=400
        )

    except NoRecordsFound as e:
        msg = f"No records found {ERR_MSG} with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", msg)],
            code=404
        )

    except HasChildError as e:
        msg = f"{ERR_MSG} with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", msg)],
            code=409
        )

    except ValidationError as e:
        msg = f"Validation {ERR_MSG} with ID {id}"
        logging.error(f"{msg}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", msg)],
            code=409
        )

    except Exception as e:
        msg = "An unexpected {ERR_MSG}"
        logging.error(f"{msg}: {str(e)}", exc_info=TRACEBACK)
        return create_response(
            data=[("error", msg)],
            code=500
        )
