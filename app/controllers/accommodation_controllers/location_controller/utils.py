import logging
from flask import abort
from typing import Union


def throw_error(code: int, description: str):
    """
    Logs an error and aborts the request with the specified code
    and description.

    Args:
        code (int): HTTP status code for the error.
        description (str): Description of the error message.
    """
    logging.error(description)
    abort(code=code, description=description)


def set_filter_criteria(field: str, value: Union[str, int]) -> dict:
    """
    Creates filter criteria for querying the database.

    Args:
        field (str): The name of the field to filter by.
        value (any): The value of the field to filter by.

    Returns:
        dict: Filter criteria as a dictionary.
    """
    return {field: value.strip() if isinstance(value, str) else value}
