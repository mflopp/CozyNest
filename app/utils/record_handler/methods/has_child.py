import logging
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.inspection import inspect
from typing import Type, Any


def has_child(record: Type[Any], associated_model: Type[Any]) -> bool:
    try:
        logging.info(
            f"checking if the model {record} has childs in {associated_model}"
        )
        # Check that the record is associated with the SQLAlchemy mapping
        mapper = inspect(record).mapper
    except UnmappedInstanceError:
        logging.error("The passed object is not bound to mapping")
        raise ValueError("The passed object is not bound to mapping.")

    # Finding the relationship between the parent and child model
    for relationship in mapper.relationships.keys():
        related_mapper = mapper.relationships[relationship]
        if related_mapper.mapper.class_ is associated_model:
            # Checking for the presence of child records
            related_items = getattr(record, relationship, None)
            return bool(related_items)

    return False
