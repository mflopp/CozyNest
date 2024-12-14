from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.users import UserRole
from utils import Finder


def fetch_user_roles(session: Session):

    try:
        # get user roles list
        user_roles = Finder.fetch_records(session, UserRole)

        return user_roles

    except SQLAlchemyError:
        raise

    except Exception:
        raise
