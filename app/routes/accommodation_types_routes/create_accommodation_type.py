from flask import Response, request
from controllers import AccommodationTypeController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_types_blueprint import accommodation_types_bp

ERR_MSG = 'Error occurred while creating Accommodation Type record'


@accommodation_types_bp.route(
    "", methods=['POST'], endpoint='create_accommodation_type'
)
@crud_exceptions_handler(ERR_MSG)
def create_accommodation_type_handler() -> Response:

    # Use the session_scope context manager
    with session_scope() as session:

        # requeting body from user request
        accommodation_type_data = request.get_json()
        # creating a new accommodation type
        accommodation_type = AccommodationTypeController.create(
            accommodation_type_data,
            session
        )

        # creating user response
        return create_response(
            data=[
                    ("accommodation type", accommodation_type)
            ],
            code=200
        )
