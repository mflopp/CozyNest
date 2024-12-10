import re
from typing import Any

from utils import ValidationError
from .validate_requirements import validate_requirements


def is_valid_name(name: str):
    # Regular expression to validate the name
    pattern = re.compile(r"^[A-Z][a-z]{1,24}(-[a-z]+)?(\s[A-Z][a-z]{2,25})?$")

    return bool(pattern.match(name))


def validate_name(name: str | Any | None) -> None:
    try:
        message = 'Name does not fit the requirements'
        validate_requirements(name, is_valid_name, message)
    except ValidationError:
        raise
