from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.users import UserSettings
from utils import Finder


def fetch_user_settings(session: Session):

    try:
        user_settings = Finder.fetch_records(session, UserSettings)

        return user_settings

    except (Exception, SQLAlchemyError):
        raise
