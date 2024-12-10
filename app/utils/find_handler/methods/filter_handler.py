import logging
from typing import Any, Dict


def set_filter_criteria(field: str, value: Any) -> Dict[str, Any]:
    """
    Creates filter criteria for querying the database.

    Args:
        field (str): The name of the field to filter by.
        value (Any): The value of the field to filter by.

    Returns:
        Dict[str, Any]: Filter criteria as a dictionary.

    Raises:
        ValueError: If the field is empty or invalid.
    """
    # Validate field name
    if not isinstance(field, str) or not field.strip():
        raise ValueError("Field must be a non-empty string.")

    # Validate value
    if value is None:
        raise ValueError("Value cannot be None.")

    # Create filter criteria
    res = {field.strip(): value.strip() if isinstance(value, str) else value}

    logging.debug(f"Filter criteria created for field='{field}': {res}")
    return res
