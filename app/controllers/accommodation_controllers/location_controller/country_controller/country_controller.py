from typing import List, Dict
from sqlalchemy.orm import Session
from models import Country
from .methods import create_country, delete_country, get_country, get_countries


class CountryController:
    @staticmethod
    def create(data: dict, session: Session) -> Country:
        return create_country(data, session)

    @staticmethod
    def get_one_by_id(country_id: int, session: Session) -> Country:
        return get_country(field='id', value=country_id, session=session)

    @staticmethod
    def get_one_by_name(country_name: str, session: Session) -> Country:
        return get_country(field='name', value=country_name, session=session)

    @staticmethod
    def get_all(session: Session) -> List:
        return get_countries(session)

    @staticmethod
    def delete(country_id: int, session: Session) -> Dict:
        return delete_country(country_id, session)
