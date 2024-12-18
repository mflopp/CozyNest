import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import GenderController
from .genders_blueprint import genders_bp

from utils import create_response
from config import session_scope


@genders_bp.route("<int:id>", methods=['GET'])
def get_gender_by_id_handler(id: int):
    """
    Endpoint for retrieving a user setting by ID. Looks up the user
    in the database and returns the user setting data or a 404 error
    if not found.

    Args:
        id (int): The ID of the user setting to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:

            gender = GenderController.get_one_by_id(
                id, session
            )

            if gender:
                return create_response(
                    data=[
                        ("id", gender.id),
                        ("gender", gender.gender),
                        ("description", gender.description)
                    ],
                    code=200
                )

            return {"message": f"Gender with ID {id} not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error while getting a gender ID {id}: {e}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Unexpected error while getting a gender ID {id}: {e}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
