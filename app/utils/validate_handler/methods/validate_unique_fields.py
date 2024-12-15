import logging
from sqlalchemy.orm import Session
from typing import Type, Dict, Any

from utils import Finder
from utils.error_handler import ValidationError


def validate_uniqueness(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any]
) -> None:
    try:
        logging.info("Validation of unique values started")

        record = Finder.fetch_record(
            session=session,
            Model=Model,
            criteria=criteria
        )

        if record:
            msg = f"Duplicate record found with values: {criteria}."
            logging.warning(msg)
            raise ValidationError(msg)
        else:
            logging.info(
                "No duplicate record found with the given combination "
                f"of values {criteria}"
            )

    except ValidationError:
        raise
