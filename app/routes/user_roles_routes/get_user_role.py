from flask import request
from models import UserRole
import logging
from controllers import UserRoleController
from .user_roles_blueprint import user_roles_bp
from utils import create_response
from config import session_scope


@user_roles_bp.route("/getone", methods=['GET'])
def get_user_role_handler() -> UserRole:
    """
    Endpoint for retrieving a user role by ID. Looks up the user in the database
    and returns the user role data or a 404 error if not found.

    Args:
        id (int): The ID of the user role to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:
        # Extract role name from query parameters
        role_name = request.get_json()['role']
        if not role_name:
            return create_response(
                data=[("error", "Role name is required")],
                code=400
            )
        # Use the session_scope context manager
        with session_scope() as session:
            user_role = UserRoleController.get_one_by_role(role_name, session)
            
            if user_role:
                return create_response(
                    data=[
                    ("id", user_role.id),
                    ("role", user_role.role),
                    ("description", user_role.description)
                ],
                    code=200
                )

            return {"message": "User role not found"}, 404
    except Exception as e:
        logging.error(f"Error occurred while retrieving user role: {str(e)}")
        return create_response(
            data=[("error", f"Error finding user role: {str(e)}")],
            code=500
        )
