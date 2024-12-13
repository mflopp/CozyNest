from typing import Callable, List
from utils.error_handler import ValidationError


def validate_requirements(
    value: str,
    is_valid: Callable,
    requirements: List[str]
) -> None:
    if not is_valid(value):
        err = f"{value} doesn't meet the required format: {requirements}"
        raise ValidationError(err)
