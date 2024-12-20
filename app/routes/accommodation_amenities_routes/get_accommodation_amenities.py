from flask import Response

from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = 'Error occurred while fetching Accommodation Amenities record'


@accommodation_amenities_bp.route(
    "", methods=['GET'], endpoint='get_accommodation_amenities'
)
@crud_exceptions_handler(ERR_MSG)
def get_accommodation_amenities_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching accommodation amenities
        accommodation_amenities = AccommodationAmenityController.get_all(
            session
        )

        # creating user response
        return create_response(
            data=[("accommodation amenities", accommodation_amenities)],
            code=200
        )
