from flask import Response

from controllers import AmenityCategoryController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenity_categories_blueprint import amenity_categories_bp

ERR_MSG = 'Error occurred while fetching Amenity categories record'


@amenity_categories_bp.route(
    "", methods=['GET'], endpoint='get_amenity_categories'
)
@crud_exceptions_handler(ERR_MSG)
def get_amenity_categories_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching amenity categories
        amenity_categories = AmenityCategoryController.get_all(session)

        # creating user response
        return create_response(
            data=[("amenity categories", amenity_categories)],
            code=200
        )
