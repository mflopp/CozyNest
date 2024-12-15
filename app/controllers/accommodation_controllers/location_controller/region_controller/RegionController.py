from typing import List, Dict
from sqlalchemy.orm import Session
from models import Region
from .methods import (
    create_region,
    get_region,
    get_full_region,
    get_regions,
    delete_region,
    update_region
)


class RegionController:
    @staticmethod
    def create(data: dict, session: Session) -> Region:
        result = create_region(data, session)
        session.commit()
        return result

    @staticmethod
    def get_region(region_id: int, session: Session) -> Region:
        result = get_region(region_id, session)
        return result

    @staticmethod
    def get_full_region(region_id: int, session: Session) -> Dict:
        result = get_full_region(region_id, session)
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
