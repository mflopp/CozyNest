import logging
from sqlalchemy.orm import Session

from models import UserRole
from utils import Finder


def fetch_user_role_by_id(id: int, session: Session):
    # This function may not be needed
    try:
        # get user roles list
        user_role = Finder.fetch_record(
            session,
            UserRole,
            {'id': id}
        )

        return user_role

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user role", "details: ": str(e)}, 500
