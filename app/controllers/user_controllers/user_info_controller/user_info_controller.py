from typing import List, Dict
from sqlalchemy.orm import Session

from models import UserInfo
from .methods import (
    add_user_info, fetch_user_info, fetch_user_infos,
    del_user_info, update_user_info
)


class UserInfoController:
    @staticmethod
    def create(user_data: Dict, session: Session) -> UserInfo:
        user_info = add_user_info(user_data, session)
        return user_info

    @staticmethod
    def get_one(user_info_id: int, session: Session) -> UserInfo:
        user_info = fetch_user_info(user_info_id, session)
        return user_info

    @staticmethod
    def get_all(session: Session) -> List:
        user_infos = fetch_user_infos(session)
        return user_infos

    @staticmethod
    def delete(user_id: int, session: Session) -> List:
        result = del_user_info(user_id, session)
        session.commit()
        return result

    @staticmethod
    def update(user_id: int, data: Dict, session: Session) -> List:
        result = update_user_info(user_id, data, session)
        session.commit()
        return result
