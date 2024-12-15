import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import User
from utils import Finder


def fetch_only_user(id: int, session: Session) -> dict:
    try:
        # Query user and related data
        user = Finder.fetch_record(session, User, {"id": id})

        if user:
            logging.info(f"User found with ID {id}")
        else:
            logging.info(f"User with ID {id} not found in the DB")

        return user

    except (Exception, SQLAlchemyError):
        raise
