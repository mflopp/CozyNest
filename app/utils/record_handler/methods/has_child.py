from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.inspection import inspect
from typing import Type, Any

from utils.logs_handler import log_info, log_err


def has_child(record: Type[Any], associated_model: Type[Any]) -> bool:
    log_info(f"checking if {record} has associations in {associated_model}")
    try:
        mapper = inspect(record).mapper

        # Finding the relationship between the parent and child model
        for relationship in mapper.relationships.keys():
            related_mapper = mapper.relationships[relationship]
            if related_mapper.mapper.class_ is associated_model:
                # Checking for the presence of child records
                related_items = getattr(record, relationship, None)
                log_info(f"{record} has associations in {associated_model}")
                return bool(related_items)

        log_info(f"{record} has no associations in {associated_model}")
        return False

    except UnmappedInstanceError:
        msg = "The passed object is not bound to mapping"
        log_err(f'has_child(): {msg}')
        raise ValueError(msg)

    except ValueError:
        msg = "Value error occured"
        log_err(f'has_child(): {msg}')
        raise ValueError(msg)

    except Exception:
        msg = "Unknown common error occurred"
        log_err(f'has_child(): {msg}')
        raise
