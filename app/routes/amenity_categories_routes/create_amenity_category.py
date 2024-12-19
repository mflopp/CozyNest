from flask import Response, request
from controllers import AmenityCategoryController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenity_categories_blueprint import amenity_categories_bp

ERR_MSG = 'Error occurred while creating Amenity category record'


@amenity_categories_bp.route(
    "", methods=['POST'], endpoint='create_amenity_category'
)
@crud_exceptions_handler(ERR_MSG)
def create_amenity_category_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:

        # requeting body from user request
        amenity_category_data = request.get_json()
        # creating a new amenity category
        amenity_category = AmenityCategoryController.create(
            amenity_category_data,
            session
        )

        # creating user response
        return create_response(
            data=[
                    ("amenity category", amenity_category)
            ],
            code=200
        )
