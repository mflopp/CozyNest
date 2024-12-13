import logging
from sqlalchemy.orm import Session
from models.users import UserRole


def fetch_user_roles(session: Session):

    try:
        # get user roles list
        user_roles = session.query(
            UserRole.id.label("role_id"),
            UserRole.role,
            UserRole.description,
        ).all()
        if user_roles:
            return user_roles
        else:
            return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting user roles", "details: ": str(e)}, 500
