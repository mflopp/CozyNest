from typing import Type, Dict, List, Any
from sqlalchemy.orm import Session
from models.users import User, UserSettings

from .validate_unique import validate_unique_fields
from .validate_required_fields import validate_required_fields
from .validate_pswrd import validate_password
from .validate_phone import validate_phone
from .validate_email import validate_email
from .validate_currency import validate_currency
from .validate_language import validate_language


def validate_data(
    session: Session,
    Model: Type[Any],
    data: Dict[str, Any],
    required_fields: List[str],
    unique_fields: List[str] = []
) -> None:
    """
    Validates input data for a given model, checking required fields,
    uniqueness, and additional validations for specific models.

    Args:
        session (Session): SQLAlchemy session for database queries.
        Model (Type[Any]): The model class to validate data against.
        data (Dict[str, Any]): Input data for validation.
        required_fields (List[str]): Fields that must be present in data.
        unique_fields (List[str]): Fields that must be unique in the database.

    Raises:
        ValidationError: If validation fails for any reason.
    """
    # Validate required fields
    if required_fields:
        validate_required_fields(required_fields, data)

    # Validate unique fields in the database
    if unique_fields:
        validate_unique_fields(session, Model, unique_fields, data)

    # Model-specific validations
    if issubclass(Model, User):
        phone = data.get('phone', '')
        email = data.get('email', '')
        password = data.get('password', '')

        if phone:
            validate_phone(phone)
        if email:
            validate_email(email)
        if password:
            validate_password(password)

    if issubclass(Model, UserSettings):
        currency = data.get('currency', '')
        language = data.get('language', '')

        if currency:
            validate_currency(currency)
        if language:
            validate_language(language)
