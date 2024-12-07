from typing import List, Dict
from sqlalchemy.orm import Session
from models import Country
from .methods import create_country, delete_country, get_country, get_countries


class CountryController:
    @staticmethod
    def create(data: dict, session: Session) -> Country:
        response, status = create_country(data, session)
        session.commit()
        return response, status

    @staticmethod
    def get_one_by_id(country_id: int, session: Session) -> Country:
        contry = get_country(field='id', value=country_id, session=session)
        session.commit()
        return contry

    @staticmethod
    def get_one_by_name(country_name: str, session: Session) -> Country:
        country = get_country(field='name', value=country_name, session=session)
        session.commit()
        return country

    @staticmethod
    def get_all(session: Session) -> List:
        countries = get_countries(session)
        session.commit()
        return countries

    @staticmethod
    def delete(country_id: int, session: Session) -> Dict:
        return delete_country(country_id, session)
