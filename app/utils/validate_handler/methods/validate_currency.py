import re
from .validate_requirements import validate_requirements


def is_valid_currency(currency: str) -> bool:
    # Regular expression for currencies
    patterns = [
        re.compile(r"\b[A-Z]{3}\b")
    ]

    # Check if the currency matches the patterns
    return any(pattern.match(currency) for pattern in patterns)


def validate_currency(currency: str) -> None:
    validate_requirements(currency, is_valid_currency, ["XXX"])
