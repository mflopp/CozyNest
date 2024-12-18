from typing import List, Dict, Any, Type
from sqlalchemy.orm import Session
from models import AmenitiesCategory
from .methods import (
    add_amenity_category, fetch_amenity_category,
    fetch_amenity_categories, del_amenity_category,
    parse_full_amenity_category
)


class AmenityCategoryController:
    @staticmethod
    def create(data: Dict, session: Session) -> AmenitiesCategory:
        category = add_amenity_category(data, session)
        session.commit()
        return category

    @staticmethod
    def get_one_by_name(
        category: Dict, session: Session, return_instance: bool = False
    ):
        category = fetch_amenity_category(
            'category', category, session, return_instance
        )
        return category

    @staticmethod
    def get_one_by_id(
        category_id: int, session: Session, return_instance: bool = False
    ):
        category = fetch_amenity_category(
            'id', category_id, session, return_instance
        )
        return category

    @staticmethod
    def get_all(session: Session) -> List:
        categories = fetch_amenity_categories(session)
        return categories

    @staticmethod
    def delete(category_id: int, session: Session) -> List:
        result = del_amenity_category(category_id, session)
        session.commit()
        return result

    @staticmethod
    def parse_full(amenity_category: Type[Any]) -> Dict[str, Any]:
        result = parse_full_amenity_category(amenity_category)
        return result
