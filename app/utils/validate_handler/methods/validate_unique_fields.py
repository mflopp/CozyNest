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
            logging.error(f"validate_uniqueness(): {msg}", exc_info=True)
            raise ValidationError(msg)

        logging.info("Validation of unique values passed")

    except ValidationError:
        raise
