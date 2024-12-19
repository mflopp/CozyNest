from typing import List, Dict, Any, Type
from sqlalchemy.orm import Session
from models import Amenity
from .methods import (
    add_amenity, fetch_amenity,
    fetch_amenities, del_amenity,
    parse_full_amenity, update_amenity
)


class AmenityController:
    @staticmethod
    def create(data: Dict, session: Session) -> Amenity:
        amenity = add_amenity(data, session)
        session.commit()
        return amenity

    @staticmethod
    def get_one_by_name(
        amenity: Dict, session: Session, return_instance: bool = False
    ):
        amenity = fetch_amenity(
            'name', amenity, session, return_instance
        )
        return amenity

    @staticmethod
    def get_one_by_id(
        amenity_id: int, session: Session, return_instance: bool = False
    ):
        amenity = fetch_amenity(
            'id', amenity_id, session, return_instance
        )
        return amenity

    @staticmethod
    def get_all(session: Session) -> List:
        categories = fetch_amenities(session)
        return categories

    @staticmethod
    def delete(amenity_id: int, session: Session) -> List:
        result = del_amenity(amenity_id, session)
        session.commit()
        return result

    @staticmethod
    def update(amenity_id: int, data: Dict, session: Session):
        update_amenity(amenity_id, data, session)
        session.commit()

    @staticmethod
    def parse_full(amenity: Type[Any]) -> Dict[str, Any]:
        result = parse_full_amenity(amenity)
        return result
