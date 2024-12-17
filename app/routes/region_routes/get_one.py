import logging
from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import NoRecordsFound, ValidationError
from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp

ERR_MSG = "Error occurred while fetching Region record"
TRACEBACK = True


@region_bp.route("/<int:id>", methods=['GET'])
def get_region_handler(id: int) -> Response:
    try:
        with session_scope() as session:
            region = RegionController.get_region(id, session)

            if region:
                return create_response(
                    data=[("region", region)],
                    code=200
                )

            return create_response(
                data=[("info", "Region not found")],
                code=404
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
