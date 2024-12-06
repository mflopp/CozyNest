import logging
from sqlalchemy.orm import Session
from models.users import UserSettings


def fetch_user_settings(session: Session):
    
    try:
        # Query all UserSettings
        user_settings = session.query(
            UserSettings.id.label("user_settings_id"),
            UserSettings.currency,
            UserSettings.language,
        ).all()
        
        if user_settings:
            return user_settings
        else:
            return False

    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error getting user settings", "details: ": str(e)}, 500
