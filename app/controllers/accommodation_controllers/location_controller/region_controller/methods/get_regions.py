import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Region
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while fetching Region records"
TRACEBACK = True


def get_countries(session: Session) -> List[Region]:
    try:
        regions = Finder.fetch_records(session, Region)
        Finder.log_found_amount(regions)
        return regions

    except NoRecordsFound as e:
        logging.warning(e, exc_info=TRACEBACK)
        raise

    except ValidationError as e:
        logging.error(
            f"Validation {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except SQLAlchemyError as e:
        logging.error(
            f"Data Base {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected {ERR_MSG}: {e}", exc_info=TRACEBACK
        )
        raise
