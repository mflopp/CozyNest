from flask import Response, request
from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = 'Error occurred while creating Accommodation Amenity record'


@accommodation_amenities_bp.route(
    "", methods=['POST'], endpoint='create_accommodation_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def create_accommodation_amenity_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:

        # requeting body from user request
        accommodation_amenity_data = request.get_json()
        # creating a new accommodation amenity
        accommodation_amenity = AccommodationAmenityController.create(
            accommodation_amenity_data,
            session
        )

        # creating user response
        return create_response(
            data=[
                    ("accommodation amenity", accommodation_amenity)
            ],
            code=200
        )
