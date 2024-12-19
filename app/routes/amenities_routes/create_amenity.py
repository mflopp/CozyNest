from flask import Response, request
from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = 'Error occurred while creating Amenity record'


@amenities_bp.route(
    "", methods=['POST'], endpoint='create_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def create_amenity_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:

        # requeting body from user request
        amenity_data = request.get_json()
        # creating a new amenity
        amenity = AmenityController.create(
            amenity_data,
            session
        )

        # creating user response
        return create_response(
            data=[
                    ("amenity", amenity)
            ],
            code=200
        )
