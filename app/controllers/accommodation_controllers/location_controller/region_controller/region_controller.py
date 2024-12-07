from .methods import create_region, get_region, get_regions, delete_region
from typing import List, Dict
from sqlalchemy.orm import Session
from models import Region


class RegionController:
    @staticmethod
    def create(data: dict, session: Session) -> Region:
        return create_region(data, session)

    @staticmethod
    def get_one_by_id(region_id: int, session: Session) -> Region:
        return get_region(field='id', value=region_id, session=session)

    @staticmethod
    def get_one_by_name(region_name: str, session: Session) -> Region:
        return get_region(field='name', value=region_name, session=session)

    @staticmethod
    def get_all(session: Session) -> List:
        return get_regions(session)

    @staticmethod
    def delete(region_id: int, session: Session) -> Dict:
        return delete_region(region_id, session)
