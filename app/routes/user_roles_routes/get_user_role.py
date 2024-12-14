from flask import request
from models import UserRole
import logging
from sqlalchemy.exc import SQLAlchemyError

from controllers import UserRoleController
from .user_roles_blueprint import user_roles_bp
from utils.error_handler import ValidationError

from utils import create_response
from config import session_scope


@user_roles_bp.route("/getone", methods=['GET'])
def get_user_role_handler() -> UserRole:
    """
    Endpoint for retrieving a user role by ID. Looks up the user in the
    database and returns the user role data or a 404 error if not found.

    Args:
        id (int): The ID of the user role to retrieve.

    Returns:
        tuple: A tuple with the response and HTTP status code.
    """
    try:

        # Use the session_scope context manager
        with session_scope() as session:
            role_data = request.get_json()
            user_role = UserRoleController.get_one_by_role(role_data, session)

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

    except SQLAlchemyError as e:
        logging.error(f"{e}")
        return create_response(
            data=[("error", f"{str(e)}")],
            code=500
        )

    except ValidationError as e:
        logging.error(f"Validation error while getting a user role: {str(e)}")
        return create_response(
            data=[(
                "error",
                f"Validation error while getting a user role: {str(e)}"
            )],
            code=500
        )

    except Exception as e:
        logging.error(f"Error occurred while retrieving user role: {str(e)}")
        return create_response(
            data=[("error", f"Error finding user role: {str(e)}")],
            code=500
        )
