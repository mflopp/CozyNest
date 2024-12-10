import logging
from sqlalchemy.orm import Session

from models import UserRole


def fetch_user_role_by_id(id: int, session: Session):
    try:
        # get user roles list
        user_role = get_first_record_by_criteria(
            session,
            UserRole,
            {'id': id}
        )
        if user_role:
            return user_role
        else:
            return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user role", "details: ": str(e)}, 500
