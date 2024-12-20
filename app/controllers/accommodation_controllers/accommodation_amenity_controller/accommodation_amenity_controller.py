from typing import List, Dict, Any, Type
from sqlalchemy.orm import Session
from models import Amenity
from .methods import (
    add_accommodation_amenity, fetch_accommodation_amenity,
    fetch_accommodation_amenities, del_accommodation_amenity,
    parse_full_accommodation_amenity, update_accommodation_amenity
)


class AccommodationAmenityController:
    @staticmethod
    def create(data: Dict, session: Session) -> Amenity:
        amenity = add_accommodation_amenity(data, session)
        session.commit()
        return amenity

    @staticmethod
    def get_one_by_accommodation(
        amenity: Dict, session: Session, return_instance: bool = False
    ):
        amenity = fetch_accommodation_amenity(
            'accommodation_id', amenity, session, return_instance
        )
        return amenity

    @staticmethod
    def get_one_by_id(
        id: int, session: Session, return_instance: bool = False
    ):
        amenity = fetch_accommodation_amenity(
            'id', id, session, return_instance
        )
        return amenity

    @staticmethod
    def get_all(session: Session) -> List:
        categories = fetch_accommodation_amenities(session)
        return categories

    @staticmethod
    def delete(id: int, session: Session) -> List:
        result = del_accommodation_amenity(id, session)
        session.commit()
        return result

    @staticmethod
    def update(id: int, data: Dict, session: Session):
        update_accommodation_amenity(id, data, session)
        session.commit()

    @staticmethod
    def parse_full(amenity: Type[Any]) -> Dict[str, Any]:
        result = parse_full_accommodation_amenity(amenity)
        return result
