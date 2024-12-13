import logging
from sqlalchemy.orm import Session
from typing import Type, Any

from utils import Finder
from utils.error_handler import ValidationError


def validate_unique_field(
    session: Session,
    Model: Type[Any],
    field: str,
    value: Any
) -> None:
    try:
        # Log the initiation of the uniqueness check
        logging.info(
            f"Checking uniqueness for value '{value}' in field '{field}'."
        )

        # Attempt to fetch any existing record with the same value in
        # the given field
        record = Finder.fetch_record(
            session=session,
            Model=Model,
            criteria={field: value}
        )

        # Log if a duplicate is found
        if record:
            msg = f"Duplicate value '{value}' found in field '{field}'."
            logging.warning(msg)
            raise ValidationError(msg)
        else:
            # Log successful validation when no duplicate is found
            logging.info("No duplicate found.")

    except ValidationError:
        raise
