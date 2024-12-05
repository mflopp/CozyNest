from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from flask import abort, Response
from collections import OrderedDict
import json

from models.users import User, UserInfo, UserRole, Gender, UserSettings


def fetch_user(id: int, db: Session) -> dict:
    """
    Fetches user data from the database by ID, including related information.

    Args:
        id (int): User ID.
        db (Session): SQLAlchemy database session.

    Returns:
        dict: User data including personal details, role, and settings.

    Raises:
        404: If user is not found.
        500: For other server errors.
    """
    try:
        # Query user and related data
        user = db.query(
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
            User.created_at,
            User.updated_at
        ).join(UserInfo, User.info_id == UserInfo.id)\
         .join(Gender, UserInfo.gender_id == Gender.id)\
         .join(UserRole, User.role_id == UserRole.id)\
         .join(UserSettings, UserInfo.user_settings_id == UserSettings.id)\
         .filter(User.id == id)\
         .first()

        if not user:
            abort(404, description="User not found")

        # Transform data to the desired format
        user_data = OrderedDict([
            ("user_id", user.user_id),
            ("email", user.email),
            ("password", user.password),  # Consider excluding sensitive data
            ("first_name", user.first_name),
            ("last_name", user.last_name),
            ("birthdate", user.birthdate.strftime("%d.%m.%Y") if user.birthdate else None),
            ("gender", user.gender),
            ("phone", user.phone),
            ("role", user.user_role),
            ("user_settings", OrderedDict([
                ("currency", user.currency),
                ("language", user.language)
            ])),
            ("created_at", user.created_at),
            ("updated_at", user.updated_at)
        ])
        
        # user_data = {
        #     "user_id": user.user_id,
        #     "email": user.email,
        #     "password": user.password,  # Consider excluding sensitive data
        #     "first_name": user.first_name,
        #     "last_name": user.last_name,
        #     "birthdate": user.birthdate.strftime("%d.%m.%Y") if user.birthdate else None,
        #     "gender": user.gender,
        #     "phone": user.phone,
        #     "role": user.user_role,
        #     "user_settings": {
        #         "currency": user.currency,
        #         "language": user.language
        #     },
        #     "created_at": user.created_at,
        #     "updated_at": user.updated_at
        # }

        logging.info(f"User found with ID {id}")

        # Use json.dumps to ensure order and return a Response
        response = Response(
            response=json.dumps(user_data, default=str),
            status=200,
            mimetype='application/json'
        )
        return response
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        abort(500, description="Database error")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        abort(500, description="An unexpected error occurred")
