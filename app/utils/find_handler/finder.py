from sqlalchemy.orm import Session
from typing import Any, Dict, Type, List, Optional

from .methods import (
    fetch_record,
    fetch_records,
    set_filter_criteria,
    get_first_record_by_criteria,
    log_found_amount,
    get_full_record
)


class Finder:
    @staticmethod
    def build_criteria(field: str, value: Any) -> Dict[str, Any]:
        return set_filter_criteria(field, value)

    @staticmethod
    def fetch_record_by_criteria(
        session: Session,
        Model: Type[Any],
        criteria: Dict[str, Any]
    ) -> Any:
        return get_first_record_by_criteria(session, Model, criteria)

    @staticmethod
    def fetch_records(
        session: Session,
        Model: Type[Any],
        filter_conditions: Optional[Any] = None,
        order_by: Optional[Any] = None
    ) -> List:
        return fetch_records(session, Model, filter_conditions, order_by)

    @staticmethod
    def fetch_record(
        session: Session,
        Model: Type[Any],
        field: str,
        value: Any
    ) -> Any:
        return fetch_record(session, Model, field, value)

    @staticmethod
    def log_found_amount(records: List[Any]) -> None:
        return log_found_amount(records)

    @staticmethod
    def get_associated(
        session: Session,
        id: int,
        Model: Type[Any]
    ) -> (Dict[str, Any] | None):
        return get_full_record(session, id, Model)
