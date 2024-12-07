from typing import List, Dict
from sqlalchemy.orm import Session
from models import City
from .methods import create_city, delete_city, get_city, get_cities


class CityController:
    @staticmethod
    def create(data: dict, session: Session) -> City:
        return create_city(data, session)

    @staticmethod
    def get_one_by_id(city_id: int, session: Session) -> City:
        return get_city(field='id', value=city_id, session=session)

    @staticmethod
    def get_one_by_name(city_name: str, session: Session) -> City:
        return get_city(field='name', value=city_name, session=session)

    @staticmethod
    def get_all(session: Session) -> List:
        return get_cities(session)

    @staticmethod
    def delete(city_id: int, session: Session) -> Dict:
        return delete_city(city_id, session)
