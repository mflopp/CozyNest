from sqlalchemy.orm import Session
from typing import Type, Dict, List, Any

from .validate_unique_field import validate_unique_field


def validate_unique_fields(
    session: Session,
    Model: Type[Any],
    fields: List[str],
    fields_values: Dict[str, Any]
) -> None:
    """
    Validates the uniqueness of multiple fields in a database model.

    Args:
        session (Session): The SQLAlchemy session to use for validation.
        Model (Type[Base]): The ORM model class to validate against.
        fields (List[str]): A list of fields to validate.
        fields_values (Dict[str, Any]): A dictionary of field names and their
                                        corresponding values.

    Raises:
        ValueError: If the fields list is empty, or if a field is missing
                    in `fields_values`.
        Any: If `validate_unique_field` raises an exception.
    """
    if not fields:
        raise ValueError("The fields list cannot be empty.")

    for field in fields:
        if field not in fields_values:
            raise ValueError(f"Field '{field}' is missing in fields_values.")
        try:
            validate_unique_field(session, Model, field, fields_values[field])
        except Exception as e:
            data = f"'{fields_values[field]}': {e}"
            raise ValueError(
                f"Validation failed for field '{field}' with value '{data}"
            )
