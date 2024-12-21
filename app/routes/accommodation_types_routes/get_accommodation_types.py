from flask import Response

from controllers import AccommodationTypeController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_types_blueprint import accommodation_types_bp

ERR_MSG = 'Error occurred while fetching Accommodation Type record'


@accommodation_types_bp.route(
    "", methods=['GET'], endpoint='get_accommodation_types'
)
@crud_exceptions_handler(ERR_MSG)
def get_accommodation_types_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching accommodation types
        accommodation_types = AccommodationTypeController.get_all(session)

        # creating user response
        return create_response(
            data=[("accommodation types", accommodation_types)],
            code=200
        )
