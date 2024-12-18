from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Region
from utils import Finder
from utils.error_handler import ValidationError, NoRecordsFound
from .parse_full_region import parse_full_region
from utils.logs_handler import log_info


def get_regions(session: Session) -> List:
    log_info('Regionss fetching started')
    try:
        regions = Finder.fetch_records(session, Region)
        Finder.log_found_amount(regions)

        result = [parse_full_region(region) for region in regions]

        log_info('Regions fetching successfully finished')
        return result

    except (NoRecordsFound, ValidationError, SQLAlchemyError, Exception):
        raise
