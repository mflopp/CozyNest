from flask import Response, request

from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = "Error occurred while updating Amenity record"


@amenities_bp.route("/<int:id>", methods=['PUT'], endpoint='update_amenity')
@crud_exceptions_handler(ERR_MSG)
def update_amenity_handler(id: int) -> Response:

    new_data = request.get_json()

    if not new_data:
        raise ValueError("Request body is required")

    with session_scope() as session:
        AmenityController.update(id, new_data, session)
        return create_response(
            data=[("info", f'Amenity ID {id} succesfully updated')],
            code=200
        )
