import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserInfoController
from .user_info_blueprint import user_info_bp

from utils import create_response
from config import session_scope


@user_info_bp.route("<int:id>", methods=['GET'])
def get_user_info_handler(id: int):
    """
    Endpoint for retrieving a user info by ID. Looks up the user
    in the database and returns the user info data or a 404 error if not found.

    Args:
        id (int): The ID of the user info to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_info = UserInfoController.get_one(id, session)

            if user_info:
                return create_response(
                    data=[
                        ("id", user_info.id),
                        ("gender_id", user_info.gender_id),
                        ("user_settings_id", user_info.user_settings_id),
                        ("first_name", user_info.first_name),
                        ("last_name", user_info.last_name),
                        ("birthdate", user_info.birthdate),
                        ("created_at", user_info.created_at),
                        ("updated_at", user_info.updated_at)
                    ],
                    code=200
                )

            return {"message": f"User setting ID {id} not found"}, 404

    except SQLAlchemyError as e:
        msg = f"DB error occured while fetching user info ID  {id}: {str(e)}"
        logging.error(msg)
        return create_response(
            data=[("error", msg)],
            code=500
        )

    except Exception as e:
        msg = f"Unexpected error while getting user info ID  {id}: {e}"
        logging.error(msg)
        return create_response(data=[("error", msg)], code=500)
