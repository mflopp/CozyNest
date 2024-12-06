import re
from .validate_requirements import validate_requirements


def is_valid_email(email: str) -> bool:
    """
    Validates an email address against patterns for Israeli, USA, and
    Russian emails.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email matches any of the patterns, False otherwise.
    """
    # Regular expressions for validating email addresses
    patterns = [
        re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.il$"),  # Israel
        re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net|org|us)$"),
        re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.ru$")   # Russia
    ]

    # Strip any extra whitespace and validate against patterns
    email = email.strip()
    return any(pattern.match(email) for pattern in patterns)


def validate_email(email: str) -> None:
    """
    Raises a validation error if the email is not valid.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email address is invalid.
    """
    validate_requirements(email, is_valid_email)
