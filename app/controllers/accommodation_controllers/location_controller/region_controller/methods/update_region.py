import logging
from sqlalchemy.orm import Session

from models import Region
from .get_region import get_region

from utils import Validator, Recorder
from utils.error_handler import ValidationError, NoRecordsFound


def update_region(region_id: int, data: dict, session: Session) -> Region:
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Validate the input data to ensure it meets the model requirements
            Validator.validate_required_fields(['name'], data)

            new_name = data['name']

            Validator.validate_unique_field(session, Region, 'name', new_name)
            Validator.validate_name(new_name)

            # Fetch the existing record
            region = get_region(region_id, session)

            # Attempt to update the record
            Recorder.update(session, region, data)

        logging.info(f"Region with ID {region_id} successfully updated.")

        return region

    except NoRecordsFound as e:
        logging.error({f"No records found for updating: {e}"})
        raise
    except ValidationError as e:
        logging.error(f"Validation Error occured while updating: {e}")
        raise
    except ValueError as e:
        logging.error(f"Value Error occured while updating: {e}")
        raise
    except Exception as e:
        logging.error(
            f"Unexpected error occured while updating: {e}", exc_info=True
        )
        raise
