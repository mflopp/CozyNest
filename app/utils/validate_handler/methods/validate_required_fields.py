from typing import List, Dict

from utils.error_handler import ValidationError


def is_not_field(field: str, data: Dict[str, str]) -> bool:
    return not bool(data.get(field))


def validate_required_field(
    field: str,
    data: Dict[str, str]
) -> None:
    if not field:
        raise ValidationError("Field cannot be empty.")

    if is_not_field(field, data):
        err = f"Field '{field}' is required and cannot be empty."
        raise ValidationError(err)


def validate_required_fields(
    fields: List[str],
    data: Dict[str, str]
) -> None:
    if not fields:
        raise ValidationError("Fields list cannot be empty.")

    for field in fields:
        validate_required_field(field, data)
