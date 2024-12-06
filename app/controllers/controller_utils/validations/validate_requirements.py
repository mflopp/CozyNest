from utils.api_error import ValidationError, get_details
from typing import Callable


def validate_requirements(field: str, is_valid: Callable) -> None:
    if not is_valid(field):
        details = get_details(
            "Validation Error",
            f"{field} doesn't meet the required format!",
            400
        )
        raise ValidationError(details)
