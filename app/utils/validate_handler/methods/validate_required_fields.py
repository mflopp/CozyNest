import logging

from typing import List, Dict
from utils.error_handler import ValidationError


def validate_required_field(
    field: str,
    data: Dict[str, str]
) -> None:
    if not bool(data.get(field)):
        err = f"Field '{field}' is required and cannot be empty."
        raise ValidationError(err)

    logging.info('Required field are given!')


def validate_required_fields(
    fields: List[str],
    data: Dict[str, str]
) -> None:
    for field in fields:
        validate_required_field(field, data)

    logging.info('All required fields are given!')
