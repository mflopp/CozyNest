from sqlalchemy.orm import Session
from typing import Any, Optional, Type
import logging


def get_first_record_by_criteria(
    session: Session,
    Model: Type,
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
        res = session.query(Model).filter_by(**filter_criteria).first()
        return res
    except Exception as e:
        logging.error(
            f"Error querying {Model} with criteria {filter_criteria}: {e}"
        )
        return None
