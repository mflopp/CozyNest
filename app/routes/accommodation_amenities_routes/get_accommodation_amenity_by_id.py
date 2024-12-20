from flask import Response
from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = 'Error occurred while fetching Accommodation Amenity record'


@accommodation_amenities_bp.route(
    "<int:id>", methods=['GET'], endpoint='get_accommodation_amenity_by_id'
)
@crud_exceptions_handler(ERR_MSG)
def get_accommodation_amenity_by_id_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching the accommodation amenity by id
        accommodation_amenity = AccommodationAmenityController.get_one_by_id(
            id, session
        )

        # creating user response
        return create_response(
            data=[
                ("accommodation amenity", accommodation_amenity)
            ],
            code=200
        )
