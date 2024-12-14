from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import UserInfo
from utils import Finder


def fetch_user_infos(session: Session):
    try:
        # Fetch all user infos records
        user_infos = Finder.fetch_records(session, UserInfo)

        return user_infos

    except SQLAlchemyError:
        raise

    except Exception:
        raise
