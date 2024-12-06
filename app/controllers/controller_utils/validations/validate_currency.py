import re
from .validate_requirements import validate_requirements


def is_valid_currency(currency: str) -> bool:
    """
    Validates whether a given currency is a valid code matching ISO 639-3 language codes

    Args:
        currency (str): The currency to validate.

    Returns:
        bool: True if the currency is valid for one of the countries,
        False otherwise.
    """
    # Regular expression for currencies
    patterns = [
        re.compile(r"\b[A-Z]{3}\b")
    ]

    # Check if the currency matches the patterns
    return any(pattern.match(currency) for pattern in patterns)


def validate_currency(currency: str) -> None:
    """
    Validates if the provided currency fits the required format.

    Args:
        phone_number (str): The currency to validate.

    Raises:
        ValidationError: If the currency is invalid.
    """
    validate_requirements(currency, is_valid_currency)
