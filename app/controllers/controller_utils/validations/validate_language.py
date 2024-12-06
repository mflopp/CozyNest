import re
from .validate_requirements import validate_requirements


def is_valid_language(language: str) -> bool:
    """
    Validates whether a given language is a valid code

    Args:
        language (str): The language to validate.

    Returns:
        bool: True if the language is valid for one of the countries,
        False otherwise.
    """
    # Regular expression for language
    patterns = [
        re.compile(r"\b[A-Z]{3}\b")
    ]

    # Check if the language matches the patterns
    return any(pattern.match(language) for pattern in patterns)


def validate_language(language: str) -> None:
    """
    Validates if the provided language fits the required format.

    Args:
        phone_number (str): Thelanguage to validate.

    Raises:
        ValidationError: If the language is invalid.
    """
    validate_requirements(language, is_valid_language)
