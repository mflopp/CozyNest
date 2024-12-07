from typing import List, Dict

from utils.api_error import ValidationError


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


def validate_required_fields(
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
    if not fields:
        raise ValueError("Fields list cannot be empty.")

    for field in fields:
        if is_field_missing_or_empty(field, user_data):
            details = {
                'title': 'Validation failed',
                'message': f"Field '{field}' is required and cannot be empty.",
                'code': 400
            }
            raise ValidationError(details)
