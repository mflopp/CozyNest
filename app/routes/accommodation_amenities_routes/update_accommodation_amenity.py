from flask import Response, request

from controllers import AccommodationAmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_amenities_blueprint import accommodation_amenities_bp

ERR_MSG = "Error occurred while updating Accommodation Amenity record"


@accommodation_amenities_bp.route(
    "/<int:id>", methods=['PUT'], endpoint='update_accommodation_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def update_accommodation_amenity_handler(id: int) -> Response:

    new_data = request.get_json()

    if not new_data:
        raise ValueError("Request body is required")

    with session_scope() as session:
        AccommodationAmenityController.update(id, new_data, session)
        return create_response(
            data=[(
                "info",
                f'Accommodation Amenity ID {id} succesfully updated'
            )],
            code=200
        )
