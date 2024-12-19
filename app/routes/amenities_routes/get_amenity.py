from flask import Response, request
from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = 'Error occurred while fetching Amenity record'


@amenities_bp.route(
    "/getone", methods=['GET'], endpoint='get_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def get_amenity_by_name_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # requeting body from user request
        amenity_data = request.get_json()
        # fetching the amenity by name
        amenity = AmenityController.get_one_by_name(
            amenity_data, session
        )

        # creating user response
        return create_response(
            data=[
                ("amenity", amenity)
            ],
            code=200
        )
