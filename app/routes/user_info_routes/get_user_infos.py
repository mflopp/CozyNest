import logging
from controllers.user_controllers import fetch_user_infos
from .user_info_blueprint import user_info_bp

from utils import create_response
from config import session_scope

@user_info_bp.route("", methods=['GET'])
def get_user_infos_handler() -> tuple:
    """
    Endpoint for retrieving all user settings from the database.
    Returns a list of user settings or an error message if not found.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Use the session_scope context manager
        with session_scope() as session:
            user_infos = fetch_user_infos(session)

            if user_infos:
                response_data = OrderedDict([("user infos", user_infos)])
                response_json = json.dumps(response_data, default=str, sort_keys=False)
                response = make_response(response_json, 200)
                response.headers['Content-Type'] = 'application/json'
                return response

            return "User infos not found", 404

    except Exception as e:
        logging.error(f"Error occurred while retrieving user infos: {str(e)}")
        return create_response(
            data=[("error", f"Error finding user info: {str(e)}")],
            code=500
        )
