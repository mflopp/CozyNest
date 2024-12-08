from sqlalchemy.orm import Session
from typing import Any, Optional, Type, Dict, List
import logging

from sqlalchemy.exc import SQLAlchemyError


def get_first_record_by_criteria(
    session: Session,
    Model: Type[Any],
    filter_criteria: Dict[str, Any]
) -> Optional[Any]:
    """
    Retrieve the first record from the database that matches
    the given criteria.

    Args:
        session (Session): SQLAlchemy session for database access.
        Model (Type): SQLAlchemy Model class to query.
        filter_criteria (Dict[str, Any]): Filtering criteria
                                          as key-value pairs.

    Returns:
        Optional[Any]: The first matching record, or None if
        no record matches.
    """
    try:
        record = session.query(Model).filter_by(**filter_criteria).first()
        return record

    except SQLAlchemyError as e:
        logging.error(
            f"Unexpected database error while querying {Model}: {e}"
        )
        return None


def fetch_record(
    session: Session,
    Model: Type[Any],
    criteria: dict[str, Any],
    model_name: str
) -> Any:
    """
    Fetch a record from the database by criteria.

    Args:
        session (Session): The database session.
        Model (Type[Any]): The SQLAlchemy model to query.
        criteria (dict): Dictionary containing filtering criteria.
        model_name (str): Name of the model for logging purposes.

    Returns:
        Any: Retrieved record.

    Raises:
        HTTP 404 if no record is found.
        HTTP 500 if a database error occurs.
    """
    try:
        # Attempt to fetch the record
        record = get_first_record_by_criteria(session, Model, criteria)

        if not record:
            return None
        # Log the found record's ID only if found
        logging.info(f"{model_name} found with ID {record.id}")
        return record

    except SQLAlchemyError as e:
        logging.error(
            f"Database error while querying {model_name}: {e}"
        )
        raise


def fetch_records(
    session: Session,
    Model: Type[Any],
    model_name: str,
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
        # Build the query
        query = session.query(Model)

        if filter_conditions:
            query = query.filter(filter_conditions)

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
