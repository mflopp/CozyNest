import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, Type, List, Any, Dict


def fetch_records(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any] = {},
    order_by: Optional[Any] = None
) -> List[Any]:
    try:
        logging.info('')
        model_name = Model.__name__
        # Build the query
        query = session.query(Model)

        if criteria:
            query = query.filter(**criteria)

        if order_by:
            query = query.order_by(order_by)

        # Execute the query
        records = query.all()

        if not records:
            logging.info(f"No {model_name} records found.")
            return []

        logging.info(f"{len(records)} {model_name} records found.")
        return records

    except SQLAlchemyError as db_err:
        logging.error(
            f"Database error while querying {model_name}: {db_err}",
            exc_info=True
        )
        raise
