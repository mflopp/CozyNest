from sqlalchemy.inspection import inspect
from typing import Type, Any, Dict, List


def parse_record(
    model_instance: Type[Any], include_fields: List[str] = []
) -> Dict[str, Any]:
    if model_instance is None:
        return {}

    # Inspect the model instance for mapped attributes
    inspector = inspect(model_instance)

    # Use a set for fast lookup
    mapped_columns = {attr.key for attr in inspector.attrs}

    result = {}

    if include_fields:
        # Add only the specified fields that exist in the model
        for field in include_fields:
            if field in mapped_columns:
                result[field] = getattr(model_instance, field, None)
    else:
        # Add all mapped fields
        for column in inspector.attrs:
            result[column.key] = getattr(model_instance, column.key)

    return result
