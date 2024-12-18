from sqlalchemy.orm import Session
from typing import Type, Dict, Any

from utils import Finder
from utils.error_handler import ValidationError
from utils.logs_handler import log_info, log_err


def validate_uniqueness(
    session: Session,
    Model: Type[Any],
    criteria: Dict[str, Any]
) -> None:
    try:
        log_info("Validation of unique values started")

        record = Finder.fetch_record(
            session=session,
            Model=Model,
            criteria=criteria
        )

        if record:
            msg = f"Duplicate record found with values: {criteria}."
            log_err(f"validate_uniqueness(): {msg}")
            raise ValidationError(msg)

        log_info("Validation of unique values passed")

    except ValidationError:
        raise
