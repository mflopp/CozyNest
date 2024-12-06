import logging
from sqlalchemy.orm import Session
from models.users import UserSettings
from controllers.controller_utils import get_first_record_by_criteria

def fetch_user_setting(user_data: dict, session: Session):
    
    try:
        # Validate that user_data contains 'currency' and 'language' keys
        if 'currency' not in user_data or 'language' not in user_data:
            return False
        
        user_setting = get_first_record_by_criteria(
            session,
            UserSettings,
            {"currency": user_data['currency'], "language": user_data['language']}
        )
        if user_setting:
            return user_setting
        else:
            return False

    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error getting a user setting", "details: ": str(e)}, 500
