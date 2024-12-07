from sqlalchemy.orm import Session
from typing import Any, Optional, Type
import logging

from sqlalchemy.exc import SQLAlchemyError
from .error_handler import throw_error


def get_first_record_by_criteria(
    session: Session,
    Model: Type[Any],
    filter_criteria: dict[str, Any]
) -> Optional[Any]:
    """
    Retrieve the first record from the database that matches
    the given criteria.

    Args:
        session (Session): SQLAlchemy session for database access.
        Model (Type): SQLAlchemy Model class to query.
        filter_criteria (dict[str, Any]): Filtering criteria
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
            # Log and throw error if no record is found
            throw_error(
                code=404,
                description=f"{model_name} not found with given criteria."
            )

        # Log the found record's ID only if found
        logging.info(f"{model_name} found with ID {record.id}")
        return record

    except SQLAlchemyError as e:
        logging.error(
            f"Database error while querying {model_name}: {e}"
        )
        throw_error(
            code=500,
            description=f"Server error while querying {model_name}"
        )
