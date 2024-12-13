from typing import List
from sqlalchemy.orm import Session
from models import UserRole
from .methods import fetch_user_roles, fetch_user_role


class UserRoleController:
    @staticmethod
    def get_all(session: Session) -> List:
        user = fetch_user_roles(session)
        return user

    @staticmethod
    def get_one_by_id(role_id: int, session: Session) -> UserRole:
        contry = fetch_user_role('id', role_id, session)
        return contry

    @staticmethod
    def get_one_by_role(role_name: str, session: Session) -> UserRole:
        country = fetch_user_role('role', role_name, session)
        return country
