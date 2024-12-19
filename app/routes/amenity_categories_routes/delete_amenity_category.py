from flask import Response
from controllers import AmenityCategoryController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenity_categories_blueprint import amenity_categories_bp

ERR_MSG = 'Error occurred while deleting Amenity category record'


@amenity_categories_bp.route("/<int:id>", methods=['DELETE'])
@crud_exceptions_handler(ERR_MSG)
def delete_amenity_category_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # deleting amenity category record by id
        AmenityCategoryController.delete(id, session)

        # creating user response
        return create_response(
            data=[("info", f"Amenity category ID {id} deleted successfully")],
            code=200
        )
