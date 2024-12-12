import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, Type, List, Any


def fetch_records(
    session: Session,
    Model: Type[Any],
    filter_conditions: Optional[Any] = None,
    order_by: Optional[Any] = None
) -> List[Any]:
    """
    Fetch all records from the database for a given model with optional
    filters and sorting.

    Args:
        session (Session): SQLAlchemy database session.
        Model (Type[Any]): The SQLAlchemy model to query.
        model_name (str): Name of the model (for logging purposes).
        filter_conditions (Optional[Any], optional):
            SQLAlchemy filter conditions (e.g., Model.field == value).
            Defaults to None.
        order_by (Optional[Any], optional):
            SQLAlchemy order_by condition (e.g., Model.field.asc()).
            Defaults to None.

    Returns:
        List[Any]: List of model instances if records exist, otherwise
        an empty list.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        model_name = Model.__name__
        # Build the query
        query = session.query(Model)

        if filter_conditions:
            for condition in filter_conditions:
                query = query.filter(condition)

        if order_by:
            query = query.order_by(order_by)

        # Execute the query
        records = query.all()

        if not records:
            logging.warning(f"No {model_name} records found.")
            return []

        logging.info(f"{len(records)} {model_name} records found.")
        return records

    except SQLAlchemyError as db_err:
        logging.error(
            f"Database error while querying {model_name}: {db_err}",
            exc_info=True
        )
        raise
