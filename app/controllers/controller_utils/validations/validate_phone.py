import re
from .validate_requirements import validate_requirements


def is_valid_mobile_number(phone_number: str) -> bool:
    """
    Validates whether a given phone number is a valid mobile phone number
    from Israel, USA, or Russia.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid for one of the countries,
        False otherwise.
    """
    # Regular expression for Israeli, USA, and Russian mobile phone numbers
    patterns = [
        re.compile(r"^(?:\+9725|05)\d{8}$"),  # Israel
        re.compile(r"^\+1\d{10}$"),           # USA
        re.compile(r"^\+7\d{10}$")            # Russia
    ]

    # Check if the phone number matches any of the patterns
    return any(pattern.match(phone_number) for pattern in patterns)


def validate_phone(phone_number: str) -> None:
    """
    Validates if the provided phone number fits the required format.

    Args:
        phone_number (str): The phone number to validate.

    Raises:
        ValidationError: If the phone number is invalid.
    """
    validate_requirements(phone_number, is_valid_mobile_number)
