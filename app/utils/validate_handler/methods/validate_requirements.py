from typing import Callable
from utils.error_handler import ValidationError


def validate_requirements(
    field: str,
    is_valid: Callable,
    message: str
) -> None:
    if not is_valid(field):
        err = f"{field} doesn't meet the required format: {message}"
        raise ValidationError(err)
