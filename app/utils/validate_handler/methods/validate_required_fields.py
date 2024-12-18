from typing import List, Dict

from utils.error_handler import ValidationError
from utils.logs_handler import log_info, log_err


def validate_required_field(
    field: str,
    data: Dict[str, str]
) -> None:
    if not bool(data.get(field)):
        err = f"Field '{field}' is required and cannot be empty."
        log_err(f'validate_required_field(): {err}')
        raise ValidationError(err)

    log_info(f"Required field '{field}' are given!")


def validate_required_fields(
    fields: List[str],
    data: Dict[str, str]
) -> None:
    log_info('Validation of required fields started.')

    for field in fields:
        validate_required_field(field, data)

    log_info('All required fields are given!')
