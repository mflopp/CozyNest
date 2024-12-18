from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, Type, List, Any, Dict

from utils.logs_handler import log_info, log_err


def fetch_records(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any] = {},
    order_by: Optional[Any] = None
) -> List[Any]:
    log_info('Fetching records started')
    try:
        # model_name = Model.__name__
        # Build the query
        query = session.query(Model)

        if criteria:
            log_info('Adding filtering to query')
            query = query.filter(**criteria)

        if order_by:
            log_info('Adding sorting to query')
            query = query.order_by(order_by)

        # Execute the query
        records = query.all()

        # if not records:
        #     return []

        log_info('Countries fetching successfully finished')
        return records

    except SQLAlchemyError as e:
        log_err(f'fetching_records(): DB Error: {e}')
        raise
