import logging
from sqlalchemy.orm import Session
from models.users import UserInfo
from controllers.controller_utils import get_first_record_by_criteria

def fetch_user_info(id: int, session: Session):
    
    try:
        # get user roles list
        user_info = get_first_record_by_criteria(
            session,
            UserInfo,
            {'id': id}
        )
        if user_info:
            return user_info
        else:
            return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user role", "details: ": str(e)}, 500
