import re
import logging
from utils import ValidationError

CONDITIONS = [
    {
        "pattern": r"^[A-Z]",
        "error": "The name must start with an uppercase letter."
    },
    {
        "pattern": r"^.{3,}",
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
    logging.info('Validation of geografic name started!')
    try:
        if not name:
            raise ValidationError('Name cannot be empty')

        error_template = f"Name '{name}' doesn't meet the required format: "

        for condition in CONDITIONS:
            if not re.match(condition['pattern'], name):
                error = condition['error']
                raise ValidationError(f'{error_template}{error}')

        logging.info('Validation of geografic name finished!')
    except ValidationError:
        raise
