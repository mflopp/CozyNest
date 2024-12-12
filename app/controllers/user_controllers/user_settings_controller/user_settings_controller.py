from typing import List, Dict
from sqlalchemy.orm import Session
from models import UserSettings
from .methods import (
    add_user_setting, del_user_setting, fetch_user_settings,
    fetch_user_setting, fetch_user_setting_by_id, update_user_setting
)


class UserSettingsController:
    @staticmethod
    def create(data: Dict, session: Session) -> UserSettings:
        user_setting = add_user_setting(data, session)
        session.commit()
        return user_setting

    @staticmethod
    def get_one_by_name(data: Dict, session: Session) -> UserSettings:
        user_setting = fetch_user_setting(data, session)
        session.commit()
        return user_setting

    @staticmethod
    def get_one_by_id(user_setting_id: int, session: Session) -> UserSettings:
        user_setting = fetch_user_setting_by_id(user_setting_id, session)
        session.commit()
        return user_setting

    @staticmethod
    def get_all(session: Session) -> List:
        user_settings = fetch_user_settings(session)
        session.commit()
        return user_settings

    @staticmethod
    def delete(user_id: int, session: Session) -> List:
        result = del_user_setting(user_id, session)
        session.commit()
        return result

    @staticmethod
    def update(user_id: int, data: Dict, session: Session) -> List:
        result = update_user_setting(user_id, data, session)
        session.commit()
        return result
