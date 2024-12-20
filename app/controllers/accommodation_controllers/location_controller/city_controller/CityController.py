from typing import List, Dict, Any
from sqlalchemy.orm import Session
from models import City
from .methods import (
    create_city,
    delete_city,
    get_city,
    get_cities,
    update_city,
    parse_full_city
)


class CityController:
    @staticmethod
    def create(
        data: dict, session: Session
    ) -> Dict[str, Any]:
        city = create_city(data, session)
        session.commit()
        return city

    @staticmethod
    def get(
        city_id: int,
        session: Session,
        return_instance: bool = False
    ) -> City | Dict[str, Any]:
        result = get_city(
            id=city_id,
            session=session,
            return_instance=return_instance
        )
        return result

    @staticmethod
    def get_all(session: Session) -> List:
        return get_cities(session)

    @staticmethod
    def delete(city_id: int, session: Session) -> Dict:
        return delete_city(city_id, session)

    @staticmethod
    def update(city_id: int, data: Dict, session: Session):
        update_city(city_id, data, session)
        session.commit()

    @staticmethod
    def parse_full(city: City) -> Dict[str, Any]:
        return parse_full_city(city)
