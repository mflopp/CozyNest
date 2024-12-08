import logging
from sqlalchemy.orm import Session
from models.users import UserRole
from controllers.controller_utils import get_first_record_by_criteria

def fetch_user_role(user_data: dict, session: Session):
    
    try:
        # get user roles list
        user_role = get_first_record_by_criteria(
            session,
            UserRole,
            {'role': user_data['role']}
        )

        if user_role:
            return user_role
        else:
            return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user role", "details: ": str(e)}, 500
