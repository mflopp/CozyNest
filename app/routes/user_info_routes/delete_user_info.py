import logging
from controllers.user_controllers import del_user_info
from config import get_session
from .user_info_blueprint import user_info_bp


@user_info_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_info_handler(id: int) -> tuple:
    """
    Endpoint for deleting a user setting by ID. Attempts to delete the user setting from
    the database and returns a response indicating success or failure.

    Args:
        id (int): The ID of the user setting to delete.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    db = None

    try:
        db = next(get_session())  # Get a session
        response, status = del_user_info(id, db)

        return response, status
    except Exception as e:
        logging.error(f"Error occurred while deleting user setting {id}: {str(e)}")
        return {"error": "Error deleting user setting"}, 500
    finally:
        if db:
            db.close()  # Ensure the database session is properly closed
