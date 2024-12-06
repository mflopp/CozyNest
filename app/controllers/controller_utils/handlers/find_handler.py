from sqlalchemy.orm import Session
from typing import Any, Optional, Type
import logging
from flask import abort


def get_first_record_by_criteria(
    session: Session,
    Model: Type[Any],
    filter_criteria: dict[str, Any]
) -> Optional[object]:
    """
    Retrieve the first record from the database that matches
    the given criteria.

    Args:
        session (Session): SQLAlchemy session for database access.
        Model (Type): SQLAlchemy Model class to query.
        filter_criteria (dict[str, Any]): Filtering criteria
                                          as key-value pairs.

    Returns:
        Optional[object]: The first matching record, or None if
        no record matches.
    """
    try:
        record = session.query(Model).filter_by(**filter_criteria).first()
        return record
    except Exception as e:
        logging.error(
            f"Error querying {Model} with criteria {filter_criteria}: {e}"
        )
        return None


def fetch_record(session: Session, Model, criteria, model_name):
    record = get_first_record_by_criteria(
        session, Model, criteria
    )

    if not record:
        abort(404, description=f"{model_name} not found")

    logging.info(f"{model_name} found with ID {id}")

    return record
