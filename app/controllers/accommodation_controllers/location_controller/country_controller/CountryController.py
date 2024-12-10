from typing import List, Dict
from sqlalchemy.orm import Session
from models import Country

from .methods import (
    create_country,
    delete_country,
    get_country,
    get_countries,
    update_country
)


class CountryController:
    @staticmethod
    def create(data: dict, session: Session) -> Country:
        country = create_country(data, session)
        session.commit()
        return country

    @staticmethod
    def get_one_by_id(country_id: int, session: Session) -> Country:
        contry = get_country('id', country_id, session)
        session.commit()
        return contry

    @staticmethod
    def get_one_by_name(country_name: str, session: Session) -> Country:
        country = get_country('name', country_name, session)
        session.commit()
        return country

    @staticmethod
    def get_all(session: Session) -> List:
        countries = get_countries(session)
        session.commit()
        return countries

    @staticmethod
    def delete(country_id: int, session: Session):
        delete_country(country_id, session)
        session.commit()

    @staticmethod
    def update(country_id: int, data: Dict, session: Session) -> Country:
        result = update_country(country_id, data, session)
        session.commit()
        return result
