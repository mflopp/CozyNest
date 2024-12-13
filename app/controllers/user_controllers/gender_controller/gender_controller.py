from typing import List, Dict
from sqlalchemy.orm import Session
from models import Gender
from .methods import (
    add_gender, fetch_gender, fetch_genders, del_gender
)


class GenderController:
    @staticmethod
    def create(data: Dict, session: Session) -> Gender:
        gender = add_gender(data, session)
        session.commit()
        return gender

    @staticmethod
    def get_one_by_name(gender: Dict, session: Session) -> Gender:
        gender = fetch_gender('gender', gender, session)
        return gender

    @staticmethod
    def get_one_by_id(gender_id: int, session: Session) -> Gender:
        gender = fetch_gender('id', gender_id, session)
        return gender

    @staticmethod
    def get_all(session: Session) -> List:
        genders = fetch_genders(session)
        return genders

    @staticmethod
    def delete(gender_id: int, session: Session) -> List:
        result = del_gender(gender_id, session)
        session.commit()
        return result
