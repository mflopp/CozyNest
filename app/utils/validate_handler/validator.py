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
    validate_uniqueness,
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
    def validate_geografic_name(name: Any) -> None:
        validate_geografic_name(name)

    @staticmethod
    def validate_name(name: Any) -> None:
        validate_name(name)

    @staticmethod
    def validate_currency(currency: Any) -> None:
        validate_currency(currency)

    @staticmethod
    def validate_email(email: Any) -> None:
        validate_email(email)

    @staticmethod
    def validate_language(language: Any) -> None:
        validate_language(language)

    @staticmethod
    def validate_phone(phone: Any) -> None:
        validate_phone(phone)

    @staticmethod
    def validate_pswrd(password: Any) -> None:
        validate_password(password)

    @staticmethod
    def validate_requirements(
        field: str, is_valid: Callable, requirements: List[str]
    ) -> None:
        validate_requirements(field, is_valid, requirements)

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
    def validate_uniqueness(
        session: Session,
        Model: Type[Any],
        criteria: Dict[str, Any]
    ) -> None:
        validate_uniqueness(session, Model, criteria)
