import logging
from sqlalchemy.orm import Session, joinedload
from typing import Type, Optional, Dict, Any


def _get_record_dict(data: Any, Model: Type[Any]) -> Dict:
    record_dict = {}

    if data:
        for column in Model.__mapper__.columns:
            # Extract the value of the current column from the data
            column_name = column.key
            column_value = getattr(data, column_name)

            # Adding a key-value pair to a dictionary
            record_dict[column_name] = column_value

    return record_dict


def get_full_record(
    session: Session,
    id: int,
    Model: Type[Any]
) -> Optional[Dict[str, Any]]:
    """
    Dynamically fetch a record with all relationships from a given base model.

    Args:
        session (Session): SQLAlchemy session.
        id (int): Primary key ID to filter the query.
        Model (Type): The SQLAlchemy model representing the primary table.

    Returns:
        Optional[Dict[str, Any]]: Returns a dictionary of all fields
        from joined relationships or None.
    """
    try:
        # Dynamically load relationships for a given model
        query = session.query(Model)

        # Dynamically join relationships for eager loading
        for relationship in Model.__mapper__.relationships:
            query = query.options(joinedload(relationship.key))

        # Filter the query by the given ID
        result = query.filter(Model.id == id).one_or_none()

        if not result:
            return None

        # Convert the SQLAlchemy ORM result into a dictionary
        return _get_record_dict(result, Model)

    except Exception as e:
        logging.error(f"Error occurred while fetching full record: {e}")
        return None
