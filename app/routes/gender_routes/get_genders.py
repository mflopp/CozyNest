import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import GenderController
from .genders_blueprint import genders_bp

from utils import create_response
from config import session_scope


@genders_bp.route("", methods=['GET'])
def get_genders_handler():
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            genders = GenderController.get_all(session)

            if genders:
                return create_response(
                    data=[("genders", genders)],
                    code=200
                )

            return {"message": "Gender not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error occured while fetching genders: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Error occurred while fetching genders: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
