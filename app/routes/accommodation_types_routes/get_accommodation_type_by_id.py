from flask import Response
from controllers import AccommodationTypeController

from utils.exceptions_handler import crud_exceptions_handler
from utils import create_response
from config import session_scope

from .accommodation_types_blueprint import accommodation_types_bp

ERR_MSG = 'Error occurred while fetching Accommodation Type record'


@accommodation_types_bp.route(
    "<int:id>", methods=['GET'], endpoint='get_accommodation_type_by_id'
)
@crud_exceptions_handler(ERR_MSG)
def get_accommodation_type_by_id_handler(id: int) -> Response:

    # Use the session_scope context manager
    with session_scope() as session:
        # fetching the accommodation type by id
        accommodation_type = AccommodationTypeController.get_one_by_id(
            id, session
        )

        # creating user response
        return create_response(
            data=[
                ("accommodation type", accommodation_type)
            ],
            code=200
        )
