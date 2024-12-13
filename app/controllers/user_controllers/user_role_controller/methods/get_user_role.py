from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

from utils import Finder, Validator
from models.users import UserRole
from utils.error_handler import ValidationError


def fetch_user_role(
    field: str,
    value: Any,
    session: Session
) -> UserRole:

    try:
        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'role' parameter exists in user request
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the user role record
        user_role = Finder.fetch_record(
            session=session,
            Model=UserRole,
            criteria=filter_criteria
        )

        return user_role

    except SQLAlchemyError as e:
        raise SQLAlchemyError(
            {f"DB error occurred while querying user role by {field}: {e}"},
            500
        )

    except ValidationError:
        raise

    except Exception:
        raise
