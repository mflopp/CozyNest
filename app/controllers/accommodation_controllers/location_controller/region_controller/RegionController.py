from typing import Type, List, Dict, Any
from sqlalchemy.orm import Session
from models import Region
from .methods import (
    create_region,
    get_region,
    get_regions,
    delete_region,
    update_region,
    parse_full_region
)


class RegionController:
    @staticmethod
    def create(data: dict, session: Session) -> Dict[str, Any]:
        result = create_region(data, session)
        session.commit()
        return result

    @staticmethod
    def get_region(
        region_id: int, session: Session, return_instance: bool = False
    ) -> Region | Dict[str, Any]:
        result = get_region(region_id, session, return_instance)
        return result

    @staticmethod
    def get_all(session: Session) -> List:
        result = get_regions(session)
        session.commit()
        return result

    @staticmethod
    def delete(region_id: int, session: Session):
        delete_region(region_id, session)
        session.commit()

    @staticmethod
    def update(region_id: int, data: Dict, session: Session) -> Region:
        result = update_region(region_id, data, session)
        session.commit()
        return result

    @staticmethod
    def parse_full(region: Type[Any]) -> Dict[str, Any]:
        result = parse_full_region(region)
        return result
