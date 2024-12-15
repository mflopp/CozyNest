from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

from models.users import User, UserInfo, UserRole, Gender, UserSettings


def fetch_user(id: int, session: Session) -> dict:
    """
    Fetches user data from the database by ID, including related information.

    Args:
        id (int): User ID.
        session (Session): SQLAlchemy database session.

    Returns:
        dict: User data including personal details, role, and settings.

    Raises:
        404: If user is not found.
        500: For other server errors.
    """
    try:
        # Query user and related data
        user = session.query(
            User.id.label("user_id"),
            User.email,
            User.password,
            UserInfo.first_name,
            UserInfo.last_name,
            UserInfo.birthdate,
            Gender.gender,
            User.phone,
            UserRole.role.label("user_role"),
            UserSettings.currency.label("currency"),
            UserSettings.language.label("language"),
            User.deleted,
            User.created_at,
            User.updated_at
        ).join(UserInfo, User.info_id == UserInfo.id)\
         .join(Gender, UserInfo.gender_id == Gender.id)\
         .join(UserRole, User.role_id == UserRole.id)\
         .join(UserSettings, UserInfo.user_settings_id == UserSettings.id)\
         .filter(User.id == id)\
         .first()

        if not user:
            logging.info(f"User with ID {id} not found")
            return False

        logging.info(f"User found with ID {id}")

        return user

    except (Exception, SQLAlchemyError):
        raise
