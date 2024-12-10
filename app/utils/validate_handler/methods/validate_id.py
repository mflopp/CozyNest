from utils.error_handler import ValidationError


def is_valid_id(id_value: int):
    """
    Validates if the given id is a positive integer.

    Args:
        id_value (int): The id to validate.

    Returns:
        bool: `True` if the id is a positive integer, otherwise `False`.
    """
    # Check if the id is an integer and positive
    if not (isinstance(id_value, int) and id_value > 0):
        raise ValidationError('ID must be positive integer')


def validate_id(id_value: int) -> None:
    """
    Validates if the provided id is a positive integer.

    Args:
        id_value (int): The id to validate.

    Raises:
        ValidationError: If the id is invalid.
    """
    is_valid_id(id_value)
