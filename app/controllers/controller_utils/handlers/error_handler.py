import logging
from flask import abort


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
