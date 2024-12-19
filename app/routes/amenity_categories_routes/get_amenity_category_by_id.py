from flask import Response
from controllers import AmenityCategoryController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .amenity_categories_blueprint import amenity_categories_bp

ERR_MSG = 'Error occurred while fetching Amenity category record'


@amenity_categories_bp.route("<int:id>", methods=['GET'])
@crud_exceptions_handler(ERR_MSG)
def get_amenity_category_by_id_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching the amenity category by id
        amenity_category = AmenityCategoryController.get_one_by_id(
            id, session
        )

        # creating user response
        return create_response(
            data=[
                ("amenity category", amenity_category)
            ],
            code=200
        )
