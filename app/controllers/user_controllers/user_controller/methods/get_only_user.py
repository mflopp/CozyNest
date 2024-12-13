import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import User


def fetch_only_user(id: int, session: Session) -> dict:
    try:
        # Query user and related data
        user = get_first_record_by_criteria(
            session,
            User,
            {"id": id}
        )

        if not user:
            return False

        logging.info(f"User found with ID {id}")

        return user
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return {"error": "Database error", "details: ": str(e)}, 500
    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user", "details: ": str(e)}, 500
