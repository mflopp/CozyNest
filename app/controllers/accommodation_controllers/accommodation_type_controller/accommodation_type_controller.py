from typing import List, Dict, Any, Type
from sqlalchemy.orm import Session
from models import AccommodationType
from .methods import (
    add_accommodation_type, fetch_accommodation_type,
    fetch_accommodation_types, del_accommodation_type,
    parse_full_accommodation_type
)


class AccommodationTypeController:
    @staticmethod
    def create(data: Dict, session: Session) -> AccommodationType:
        type = add_accommodation_type(data, session)
        session.commit()
        return type

    @staticmethod
    def get_one_by_name(
        type: Dict, session: Session, return_instance: bool = False
    ):
        type = fetch_accommodation_type(
            'accommodation_type', type, session, return_instance
        )
        return type

    @staticmethod
    def get_one_by_id(
        type_id: int, session: Session, return_instance: bool = False
    ):
        type = fetch_accommodation_type(
            'id', type_id, session, return_instance
        )
        return type

    @staticmethod
    def get_all(session: Session) -> List:
        types = fetch_accommodation_types(session)
        return types

    @staticmethod
    def delete(type_id: int, session: Session) -> List:
        result = del_accommodation_type(type_id, session)
        session.commit()
        return result

    @staticmethod
    def parse_full(accommodation_type: Type[Any]) -> Dict[str, Any]:
        result = parse_full_accommodation_type(accommodation_type)
        return result
