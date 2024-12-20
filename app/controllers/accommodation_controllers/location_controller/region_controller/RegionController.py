from typing import List, Dict, Any
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
        return get_region(region_id, session, return_instance)

    @staticmethod
    def get_all(session: Session) -> List:
        return get_regions(session)

    @staticmethod
    def delete(region_id: int, session: Session):
        delete_region(region_id, session)
        session.commit()

    @staticmethod
    def update(region_id: int, data: Dict, session: Session):
        update_region(region_id, data, session)
        session.commit()

    @staticmethod
    def parse_full(region: Region) -> Dict[str, Any]:
        return parse_full_region(region)
