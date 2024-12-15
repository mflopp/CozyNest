import re
from .validate_requirements import validate_requirements
from utils.error_handler import ValidationError


def is_valid_pswrd(password: str) -> bool:
    """
    Validates a password against predefined requirements
    using regular expressions.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password meets all requirements, False otherwise.
    """
    checks = [
        len(password) >= 8,  # Minimum length

        # At least one uppercase letter
        re.search(r"[A-Z]", password) is not None,

        # At least one lowercase letter
        re.search(r"[a-z]", password) is not None,

        # At least one digit
        re.search(r"\d", password) is not None,

        # At least one special character
        re.search(r"[@$!%*?&]", password) is not None
    ]
    return all(checks)


def validate_password(password: str) -> None:
    """
    Validates the password and raises an exception if it
    does not meet requirements.

    Args:
        password (str): The password to validate.

    Raises:
        ValidationError: If the password does not meet the requirements.
    """
    reqs = ["min 8 symbols, 1 digit, 1 upper, 1 lower case, 1 of @$!%*?&"]
    try:
        validate_requirements(password, is_valid_pswrd, reqs)
    except ValidationError:
        raise
