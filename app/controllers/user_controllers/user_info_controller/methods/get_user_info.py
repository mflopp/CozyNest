from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import UserInfo
from utils import Finder


def fetch_user_info(id: int, session: Session):
    try:
        # Fetch the user info record
        user_info = Finder.fetch_record(
            session=session,
            Model=UserInfo,
            criteria={'id': id}
        )

        return user_info

    except SQLAlchemyError:
        raise

    except Exception:
        raise
