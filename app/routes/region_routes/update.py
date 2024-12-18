from flask import Response, request
from sqlalchemy.exc import SQLAlchemyError

from controllers import RegionController
from utils.error_handler import ValidationError, NoRecordsFound
from utils.logs_handler import log_err
from utils import create_response
from config import session_scope
from .regions_blueprint import region_bp

ERR_MSG = "Error occurred while updating Region record"


@region_bp.route("/<int:id>", methods=['PUT'])
def update_region_handler(id: int) -> Response:
    try:
        new_data = request.get_json()

        if not new_data:
            raise ValueError("Request body is required")

        with session_scope() as session:
            RegionController.update(id, new_data, session)
            return create_response(
                data=[("info", 'Succesfully updated')],
                code=200
            )

    except ValueError as e:
        log_err(f"Value {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=400)

    except NoRecordsFound as e:
        log_err(f"No records found to update with ID={id}: {str(e)}")
        return create_response(data=[("error", str(e))], code=404)

    except ValidationError as e:
        log_err(f"Validation {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=409)

    except SQLAlchemyError as e:
        log_err(f"Data Base {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", str(e))], code=500)

    except Exception as e:
        log_err(f"Unexpected {ERR_MSG}: {str(e)}")
        return create_response(data=[("error", "Updating error")], code=500)
