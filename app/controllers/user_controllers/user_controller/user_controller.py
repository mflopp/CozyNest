from typing import List, Dict
from sqlalchemy.orm import Session
from models import User
from .methods import add_user, del_user, fetch_users, fetch_user, update_user_data

class UserController:
    @staticmethod
    def create(data: Dict, session: Session) -> User:
        user = add_user(data, session)
        session.commit()
        return user

    @staticmethod
    def get_one(user_id: int, session: Session) -> User:
        user = fetch_user(user_id, session)
        session.commit()
        return user

    @staticmethod
    def get_all(session: Session) -> List:
        users = fetch_users(session)
        session.commit()
        return users

    @staticmethod
    def delete(user_id: int, session: Session) -> List:
        result = del_user(user_id, session)
        session.commit()
        return result

    @staticmethod
    def update(user_id: int, data: Dict, session: Session) -> List:
        result = update_user_data(user_id, data, session)
        session.commit()
        return result