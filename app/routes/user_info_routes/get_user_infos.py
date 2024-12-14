import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserInfoController
from .user_info_blueprint import user_info_bp

from utils import create_response
from config import session_scope


@user_info_bp.route("", methods=['GET'])
def get_user_infos_handler():
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_infos = UserInfoController.get_all(session)

            if user_infos:
                return create_response(
                    data=[("user infos", user_infos)],
                    code=200
                )

            return {"message": "Gender not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error occured while fetching user infos: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Error occurred while fetching user infos: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )
