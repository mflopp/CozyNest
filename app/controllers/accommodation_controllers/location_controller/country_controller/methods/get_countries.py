import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Country
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound

ERR_MSG = "Error occurred while fetching Country records"
TRACEBACK = True


def get_countries(session: Session) -> List[Country]:
    try:
        countries = Finder.fetch_records(session, Country)
        Finder.log_found_amount(countries)
        return countries

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
