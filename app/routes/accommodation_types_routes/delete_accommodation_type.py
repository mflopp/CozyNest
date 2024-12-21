from flask import Response
from controllers import AccommodationTypeController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_types_blueprint import accommodation_types_bp

ERR_MSG = 'Error occurred while deleting Accommodation Type record'


@accommodation_types_bp.route(
    "/<int:id>", methods=['DELETE'], endpoint='delete_accommodation_type'
)
@crud_exceptions_handler(ERR_MSG)
def delete_accommodation_type_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # deleting accommodation type record by id
        AccommodationTypeController.delete(id, session)

        # creating user response
        return create_response(
            data=[(
                "info",
                f"Accommodation Type ID {id} deleted successfully"
            )],
            code=200
        )
