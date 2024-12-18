from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.users import Gender
from utils import Finder


def fetch_genders(session: Session):

    try:
        # Fetch all genders records
        genders = Finder.fetch_records(session, Gender)

        return genders

    except (SQLAlchemyError, Exception):
        raise
