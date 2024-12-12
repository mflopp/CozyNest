import logging
from sqlalchemy.orm import Session
from typing import Type, Dict, List, Any

from utils import Finder
from utils.error_handler import ValidationError


def validate_unique_fields(
    session: Session,
    Model: Type[Any],
    fields: List[str],
    fields_values: Dict[str, Any]
) -> None:
    """
    Validates the uniqueness of multiple fields in a database model.

    Args:
        session (Session): The SQLAlchemy session to use for validation.
        Model (Type[Base]): The ORM model class to validate against.
        fields (List[str]): A list of fields to validate.
        fields_values (Dict[str, Any]): A dictionary of field names and their
                                        corresponding values.

    Raises:
        ValueError: If the fields list is empty, or if a field is missing
                    in `fields_values`.
        Any: If `validate_unique_field` raises an exception.
    """
    if not fields:
        raise ValueError("The fields list cannot be empty.")

    # maybe this block must be deleted
    for field in fields:
        if field not in fields_values:
            raise ValueError(f"Field '{field}' is missing in fields_values.")

    try:

        # Fetch any existing record with the same combination of field values
        record = Finder.fetch_combination_record(
            session=session,
            Model=Model,
            criteria=fields_values
        )

        # Log if a duplicate is found
        if record:
            msg = f"Duplicate record found with values: {fields_values}."
            # logging.warning(msg)
            raise ValidationError(msg)
        else:
            # Log successful validation when no duplicate is found
            logging.info(
                "No duplicate record found with the given combination "
                f"of values {fields_values}"
            )
    except ValidationError:
        raise

    except Exception as e:
        # Log any exception that occurs during the database query
        # or validation process
        # logging.error(f"An error occurred during uniqueness validation: {e}")
        raise Exception(
            f"An error occurred during unique validation of '{fields}': {e}"
        )
