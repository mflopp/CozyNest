from flask import Response
from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = 'Error occurred while deleting Accommodation Amenity record'


@accommodation_amenities_bp.route(
    "/<int:id>", methods=['DELETE'], endpoint='delete_accommodation_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def delete_accommodation_amenity_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # deleting accommodation amenity record by id
        AccommodationAmenityController.delete(id, session)

        # creating user response
        return create_response(
            data=[(
                "info",
                f"Accommodation Amenity ID {id} deleted successfully"
            )],
            code=200
        )
