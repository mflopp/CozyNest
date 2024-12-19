from flask import Response
from controllers import AmenityController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenities_blueprint import amenities_bp

ERR_MSG = 'Error occurred while deleting Amenity record'


@amenities_bp.route(
    "/<int:id>", methods=['DELETE'], endpoint='delete_amenity'
)
@crud_exceptions_handler(ERR_MSG)
def delete_amenity_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # deleting amenity record by id
        AmenityController.delete(id, session)

        # creating user response
        return create_response(
            data=[("info", f"Amenity ID {id} deleted successfully")],
            code=200
        )
