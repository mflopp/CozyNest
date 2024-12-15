from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from .get_user_role import fetch_user_role


def get_updated_user_role(user_data: dict, session: Session):

    try:
        with session.begin_nested():

            # Chech if UserRole update needed
            if 'role' in user_data:
                role_new = user_data["role"]
                # Fetch UserRole
                role = fetch_user_role(
                    'role',
                    {'role': role_new},
                    session
                )
                if role:
                    # return new user role id
                    return role.id
                else:
                    raise ValueError(
                        f"User role {role_new} not found in the DB"
                    )
            else:
                return None

    except (ValueError, SQLAlchemyError, Exception):
        raise
