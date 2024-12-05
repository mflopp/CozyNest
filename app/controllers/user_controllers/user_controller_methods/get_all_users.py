from sqlalchemy.orm import Session
import logging
from flask import abort

from models.users import User, UserInfo, UserRole, Gender, UserSettings

def fetch_users(db: Session):
    try:
        # Use SQLAlchemy to query all users and their related information
        users = db.query(
            User.id.label("user_id"),
            User.email,
            User.password,
            UserInfo.first_name,
            UserInfo.last_name,
            UserInfo.birthdate,
            Gender.gender,
            User.phone,
            UserRole.role.label("user_role"),
            UserInfo,
            UserSettings,
            User.created_at,
            User.updated_at
        ).join(UserInfo, User.info_id == UserInfo.id)\
         .join(Gender, UserInfo.gender_id == Gender.id)\
         .join(UserRole, User.role_id == UserRole.id)\
         .join(UserSettings, UserInfo.user_settings_id == UserSettings.id)\
         .all()

        # Transform data to the desired format
        user_data = [
            {
                "id": user.user_id,
                "email": user.email,
                "password": user.password,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "birthdate": user.birthdate.strftime("%d.%m.%Y") if user.birthdate else None,
                "gender": user.gender,
                "phone": user.phone,
                "role": user.user_role,
                "user_settings": {
                    "currency": user.UserInfo.settings.currency,
                    "language": user.UserInfo.settings.language
                },
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
            for user in users
        ]

        logging.info(f"{len(user_data)} users found in the DB")
        return user_data
    except Exception as e:
        logging.error(str(e))
        abort(500)
