import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models import UserInfo


def add_user_info(user_data: dict, gender_id: int,
                  user_settings_id: int, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():

            # Create UserInfo
            user_info = UserInfo(
                gender_id=gender_id,
                user_settings_id=user_settings_id,
                first_name=user_data.get('first_name', 'first_name'),
                last_name=user_data.get('last_name', 'last_name'),
                birthdate=user_data.get('birthdate', None),
                created_at=func.now(),
                updated_at=func.now()
            )

            response, status = add_record(session, user_info, 'user info')
            if status != 200:
                logging.error(f"user info was not created, Err: {response}")
                raise Exception(f"Failed to create user info, Err: {response}")

        session.flush()
        response = user_info.id
        return response, status
    except Exception as e:
        logging.error(str(e))
        return ({"error": "Error creating a user info", "details: ": str(e)},
                500)
