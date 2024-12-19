from flask import Response

from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = 'Error occurred while fetching Amenities record'


@amenities_bp.route(
    "", methods=['GET'], endpoint='get_amenities'
)
@crud_exceptions_handler(ERR_MSG)
def get_amenities_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching amenities
        amenities = AmenityController.get_all(session)

        # creating user response
        return create_response(
            data=[("amenities", amenities)],
            code=200
        )
