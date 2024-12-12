import logging
from sqlalchemy.orm import Session
from models import UserSettings
from utils import Finder


def fetch_user_setting_by_id(id: int, session: Session):
    try:
        user_setting = Finder.fetch_record_by_criteria(
            session,
            UserSettings,
            {"id": id}
        )

        if user_setting:
            return user_setting
        else:
            return False

    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error getting a user setting", "details: ": str(e)}, 500
