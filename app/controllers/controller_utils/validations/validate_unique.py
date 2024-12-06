from sqlalchemy.orm import Session
from typing import List, Type, Dict, Any

from utils.api_error import ValidationError
from ..handlers import get_first_record_by_criteria


def validate_unique_field(
    session: Session,
    Model: Type[Any],
    field: str,
    field_value: Any
) -> None:
    """
    Check if a value for a given field in a model is unique in the database.

    Args:
        session (Session): The database session to interact with.
        Model (Type[Any]): The model class to query.
        field (str): The name of the field to check for uniqueness.
        field_value (Any): The value to check for uniqueness.

    Raises:
        ValidationError: If a record with the given field value already exists.
    """
    record = get_first_record_by_criteria(session, Model, {field: field_value})
    if record:
        details = {
            'title': 'Validation Failed',
            'message': f"{field.capitalize()} '{field_value}' already exists.",
            'code': 400
        }
        raise ValidationError(details)


def validate_unique_fields(
    session: Session,
    Model: Type[Any],
    fields: List[str],
    fields_values: Dict[str, Any]
) -> None:
    """
    Validates if a set of fields in a model have unique values
    in the database.

    Args:
        session (Session): The database session to interact with.
        Model (Type[Any]): The model class to query.
        fields (List[str]): The list of fields to check.
        fields_values (Dict[str, Any]): A dictionary containing field names
        as keys and their values to validate.

    Raises:
        ValidationError: If a record with the given field
                         values already exists.
        ValueError: If fields list is empty.
    """
    if not fields:
        raise ValueError("Fields list cannot be empty.")

    for field in fields:
        if field not in fields_values:
            raise ValueError(f"Field '{field}' is missing in fields_values.")
        validate_unique_field(session, Model, field, fields_values[field])
