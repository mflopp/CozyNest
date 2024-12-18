from flask import Response
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import NoRecordsFound, ValidationError, HasChildError
from utils import create_response
from config import session_scope
from utils.logs_handler import log_err
from .regions_blueprint import region_bp

ERR_MSG = 'Error occurred while deleting Region record'


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
        log_err(f"Value {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=400)

    except NoRecordsFound as e:
        log_err(f"{ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=404)

    except HasChildError as e:
        log_err(f"{ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=409)

    except ValidationError as e:
        log_err(f"Validation {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=409)

    except SQLAlchemyError as e:
        log_err(f"Data Base {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=500)

    except Exception as e:
        log_err(f"Unexpected {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", "Deletion error")], code=500)
