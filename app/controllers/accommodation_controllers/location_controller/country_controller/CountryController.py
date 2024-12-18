from typing import Type, List, Dict, Any
from sqlalchemy.orm import Session
from models import Country

from .methods import (
    create_country,
    delete_country,
    get_country,
    get_countries,
    update_country,
    parse_full_country
)


class CountryController:
    @staticmethod
    def create(data: dict, session: Session) -> Dict[str, Any]:
        country = create_country(data, session)
        session.commit()
        return country

    @staticmethod
    def get_country(
        country_id: int, session: Session, return_instance: bool = False
    ) -> Country | Dict[str, Any]:
        country = get_country(country_id, session, return_instance)
        return country

    @staticmethod
    def get_all(session: Session) -> List:
        countries = get_countries(session)
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

    @staticmethod
    def parse_full(country: Type[Any]) -> Dict[str, Any]:
        result = parse_full_country(country)
        return result
