from flask import Response
from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = 'Error occurred while fetching Amenity record'


@amenities_bp.route(
    "<int:id>", methods=['GET'], endpoint='get_amenity_by_id'
)
@crud_exceptions_handler(ERR_MSG)
def get_amenity_by_id_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching the amenity by id
        amenity = AmenityController.get_one_by_id(
            id, session
        )

        # creating user response
        return create_response(
            data=[
                ("amenity", amenity)
            ],
            code=200
        )
