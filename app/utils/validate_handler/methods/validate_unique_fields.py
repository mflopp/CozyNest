import logging
from sqlalchemy.orm import Session
from typing import Type, Dict, Any

from utils import Finder
from utils.error_handler import ValidationError


def validate_unique_fields(
    session: Session,
    Model: Type[Any],
    fields_values: Dict[str, Any]
) -> None:
    try:
        record = Finder.fetch_record(
            session=session,
            Model=Model,
            criteria=fields_values
        )

        if record:
            msg = f"Duplicate record found with values: {fields_values}."
            logging.warning(msg)
            raise ValidationError(msg)
        else:
            logging.info(
                "No duplicate record found with the given combination "
                f"of values {fields_values}"
            )
    except ValidationError:
        raise
