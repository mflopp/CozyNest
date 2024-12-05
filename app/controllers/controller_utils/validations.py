from sqlalchemy.orm import Session
from .find_handler import get_first_record_by_criteria
from typing import List, Dict

from utils.api_error import ValidationError


def validate_unique_field(
    session: Session,
    Model,
    field: str,
    field_value: str
) -> None:
    """
    Check if a value for a given field in a model is unique in the database.

    Args:
        session (Session): The database session to interact with.
        Model: The model class to query.
        field (str): The name of the field to check for uniqueness.
        field_value (str): The value to check for uniqueness.

    Raises:
        ValidationError: If a record with the given field value already exists.
    """
    record = get_first_record_by_criteria(session, Model, {field: field_value})
    if record:
        msg = f"{field.capitalize()} '{field_value}' already exists"
        raise ValidationError(msg)


def is_field_missing_or_empty(field: str, user_data: Dict[str, str]) -> bool:
    """
    Checks if a field is missing or empty in the user data.

    Args:
        field (str): The name of the field to check.
        user_data (dict): The dictionary containing user data.

    Returns:
        bool: True if the field is missing or empty, otherwise False.
    """
    return not bool(user_data.get(field))


def validate_user_required_fields(
    fields: List[str],
    user_data: Dict[str, str]
) -> None:
    """
    Validates that all required fields are present and not empty
    in the user data.

    Args:
        fields (list): A list of field names that are required.
        user_data (dict): A dictionary containing user data to be validated.

    Raises:
        ValidationError: If any required field is missing or empty
        in user_data.
    """
    for field in fields:
        if is_field_missing_or_empty(field, user_data):
            msg = f"Field '{field}' is required and cannot be empty."
            raise ValidationError(msg)
