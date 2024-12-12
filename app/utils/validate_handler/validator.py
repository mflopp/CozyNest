from sqlalchemy.orm import Session
from typing import Any, Callable, Dict, List, Type
from .methods import (
    validate_requirements,
    validate_email,
    validate_currency,
    validate_phone,
    validate_password,
    validate_language,
    validate_required_fields,
    validate_required_field,
    validate_unique_field,
    validate_unique_fields,
    validate_geografic_name,
    validate_name,
    validate_id
)


class Validator:
    """
    A collection of static methods for validating various types of input data.
    """
    @staticmethod
    def validate_id(id: int) -> None:
        validate_id(id)

    @staticmethod
    def validate_geografic_name(name: str) -> None:
        validate_geografic_name(name)

    @staticmethod
    def validate_name(name: str | Any | None) -> None:
        validate_name(name)

    @staticmethod
    def validate_currency(currency: str) -> None:
        validate_currency(currency)

    @staticmethod
    def validate_email(email: str) -> None:
        validate_email(email)

    @staticmethod
    def validate_language(language: str) -> None:
        validate_language(language)

    @staticmethod
    def validate_phone(phone: str) -> None:
        validate_phone(phone)

    @staticmethod
    def validate_pswrd(password: str) -> None:
        validate_password(password)

    @staticmethod
    def validate_requirements(field: str, is_valid: Callable) -> None:
        validate_requirements(field, is_valid)

    @staticmethod
    def validate_required_field(field: str, data: Dict[str, Any]) -> None:
        validate_required_field(field, data)

    @staticmethod
    def validate_required_fields(
        fields: List[str], data: Dict[str, Any]
    ) -> None:
        validate_required_fields(fields, data)

    @staticmethod
    def validate_unique_field(
        session: Session,
        Model: Type[Any],
        field: str,
        value: Any
    ) -> None:
        validate_unique_field(session, Model, field, value)

    @staticmethod
    def validate_unique_fields(
        session: Session,
        Model: Type[Any],
        fields: List[str],
        fields_values: Dict[str, Any]
    ) -> None:
        validate_unique_fields(session, Model, fields, fields_values)
