from flask import Response, request
from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = 'Error occurred while fetching Accommodation Amenity record'


@accommodation_amenities_bp.route(
    "/getone", methods=['GET'], endpoint='get_accommodation_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def get_accommodation_amenity_by_accommodation_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # requeting body from user request
        accommodation_amenity_data = request.get_json()
        # fetching the accommodation amenity by accommodation
        accommodation_amenity = AccommodationAmenityController.get_one_by_name(
            accommodation_amenity_data, session
        )

        # creating user response
        return create_response(
            data=[
                ("accommodation amenity", accommodation_amenity)
            ],
            code=200
        )
