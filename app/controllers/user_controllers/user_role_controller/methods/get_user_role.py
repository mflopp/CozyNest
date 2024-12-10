import logging
from sqlalchemy.orm import Session
from models.users import UserRole

from sqlalchemy.exc import SQLAlchemyError
from typing import Any


def fetch_user_role(
    field: str,
    value: Any,
    session: Session
) -> UserRole:

    valid_fields = {'id', 'name', 'role'}

    validate_field(field, valid_fields)
    validate_value(value, field)
    validate_id(value, field)

    try:
        # Build filter criteria
        filter_criteria = set_filter_criteria(field, value)
        logging.debug(f"Filter criteria created: {filter_criteria}")

        # Retrieve the record
        user_role = fetch_record(
            session=session,
            Model=UserRole,
            criteria=filter_criteria,
            model_name='user role'
        )

        return user_role

    except SQLAlchemyError as e:
        raise SQLAlchemyError(
            {f"DB error occurred while querying country by {field}: {e}"}, 500
        )

    except Exception as e:
        raise Exception(
            {f"Unexpected error while getting a user role: {e}"}, 500
        )
