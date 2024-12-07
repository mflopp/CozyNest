from .utils import throw_error
from typing import Set, Any


def validate_field(field_name: str, valid_fields: Set[str]) -> None:
    """
    Validates if the given field name is valid.

    Args:
        field_name (str): The name of the field to validate.
        valid_fields (Set[str]): A set of valid field names.

    Raises:
        ValueError: If the field name is not in the set of valid fields.
    """
    if field_name not in valid_fields:
        throw_error(
            400,
            f"Invalid field name: '{field_name}'. "
            f"Must be one of {', '.join(valid_fields)}."
        )


def validate_value(value: Any, field_name: str) -> None:
    """
    Validates the value for a given field.

    Args:
        value (str | int | None): The value to validate.
        field_name (str): The name of the field.

    Raises:
        ValueError: If the value is None or an empty string.
    """
    if value is None or (isinstance(value, str) and not value.strip()):
        throw_error(400, f"Invalid value for field '{field_name}': {value}")


def validate_id(value: Any, field_name: str) -> None:
    """
    Validates that the value for the 'id' field is an integer.

    Args:
        value (int): The value to validate.
        field_name (str): The name of the field.

    Raises:
        ValueError: If the field is 'id' and the value is not an integer.
    """
    if field_name == "id" and not isinstance(value, int):
        throw_error(
            400,
            f"Field 'id' must be an integer. Got: {type(value).__name__}."
        )
