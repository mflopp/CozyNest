import re
from utils import ValidationError

from utils.logs_handler import log_info, log_err

CONDITIONS = [
    {
        "pattern": r"^[A-Z]",
        "error": "The name must start with an uppercase letter."
    },
    {
        "pattern": r"^.{2,}",
        "error": "The name must be longer than 2 characters."
    },
    {
        "pattern": r"^.{1,30}$",
        "error": "The name must be less than 30 characters."
    },
    {
        "pattern": r"^[A-Za-z]+(\s[A-Z][a-z]+)*$",
        "error": "The name may contain only letters and spaces, but each word "
        "must start with an uppercase letter."
    },
    {
        "pattern": r"^([A-Z][a-z]*\s){0,2}[A-Z][a-z]*$",
        "error": "The name may contain at most three words separated by "
        "single spaces."
    },
    {
        "pattern": r"^[A-Za-z\s]+$",
        "error": "The name may only include letters and spaces."
    }
]


def validate_name(name: str) -> None:
    log_info('Validation of name started')
    try:
        if not name:
            msg = 'Name cannot be empty'
            log_err(f'validate_name(): {msg}')
            raise ValidationError(msg)

        error_template = f"Name '{name}' doesn't meet the required format: "

        for condition in CONDITIONS:
            if not re.match(condition['pattern'], name):
                error = condition['error']
                msg = f'{error_template}{error}'
                log_err(f'validate_name(): {msg}')
                raise ValidationError(f'{error_template}{error}')

        log_info('Validation of name finished!')

    except ValidationError:
        raise
