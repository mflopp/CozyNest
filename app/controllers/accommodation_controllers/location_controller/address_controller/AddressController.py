from typing import List, Dict, Any
from sqlalchemy.orm import Session
from models import Address
from .methods import (
    create_address,
    delete_address,
    get_address,
    get_addresses,
    update_address,
    parse_full_address
)


class AddressController:
    @staticmethod
    def create(
        data: dict, session: Session
    ) -> Dict[str, Any]:
        address = create_address(data, session)
        session.commit()
        return address

    @staticmethod
    def get(
        address_id: int,
        session: Session,
        return_instance: bool = False
    ) -> Address | Dict[str, Any]:
        result = get_address(
            id=address_id,
            session=session,
            return_instance=return_instance
        )
        return result

    @staticmethod
    def get_all(session: Session) -> List:
        return get_addresses(session)

    @staticmethod
    def delete(address_id: int, session: Session) -> Dict:
        return delete_address(address_id, session)

    @staticmethod
    def update(address_id: int, data: Dict, session: Session):
        update_address(address_id, data, session)
        session.commit()

    @staticmethod
    def parse_full(address: Address) -> Dict[str, Any]:
        return parse_full_address(address)
