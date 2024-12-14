from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

from models import Gender
from utils import Finder, Validator
from utils.error_handler import ValidationError


# def fetch_gender(id: int, session: Session) -> Dict:
def fetch_gender(
    field: str,
    value: Any,
    session: Session
) -> Gender:
    try:

        # if field == id create filter for the DB request
        if field == "id":
            filter_criteria = {field: value}
        else:
            # else check if 'gender' parameter exists in user request
            Validator.validate_required_field(field, value)
            filter_criteria = Finder.extract_required_data([field], value)

        # Fetch the gender record
        gender = Finder.fetch_record(
            session=session,
            Model=Gender,
            criteria=filter_criteria
        )

        return gender

    except SQLAlchemyError as e:
        raise SQLAlchemyError(
            {f"DB error occurred while querying gender by {field}: {e}"}, 500
        )

    except ValidationError:
        raise

    except Exception:
        raise
