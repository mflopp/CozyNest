import logging
from sqlalchemy.orm import Session
from models.users import UserInfo


def fetch_user_infos(session: Session):
    try:
        # get user roles list
        user_infos = session.query(
            UserInfo.id.label("info_id"),
            UserInfo.gender_id,
            UserInfo.user_settings_id,
            UserInfo.first_name,
            UserInfo.last_name,
            UserInfo.birthdate,
            UserInfo.created_at,
            UserInfo.updated_at,
        ).all()

        if user_infos:
            return user_infos
        else:
            return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting user roles", "details: ": str(e)}, 500
