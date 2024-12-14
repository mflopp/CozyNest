import logging
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models import UserInfo

from datetime import datetime
from .get_user_info import fetch_user_info


def update_user_info(
    id: int,
    user_data: dict,
    gender_id: int,
    user_settings_id: int,
    session: Session
):
    try:
        # Start a new transaction
        with session.begin_nested():

            # required fields
            fields = ['first_name', 'last_name']

            validate_data(
                session=session,
                Model=UserInfo,
                data=user_data,
                required_fields=fields,
                unique_fields=[]  # ???
            )

            # Fetch existing user info from the database
            user_info = fetch_user_info(id, session)
            if not user_info:
                raise Exception(f"Can't fetch user info with ID {id}: not found")
            # Update fields only if they are provided in user_data
            user_info.gender_id = gender_id
            user_info.user_settings_id = user_settings_id
            user_info.first_name = user_data.get('first_name', user_info.first_name)
            user_info.last_name = user_data.get('last_name', user_info.last_name)
            # Handle birthdate format
            birthdate_str = user_data.get('birthdate', None)
            if birthdate_str:
                try:
                    user_info.birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
                except ValueError:
                    raise Exception(f"Incorrect birthdate format: {birthdate_str}")
            else:
                user_info.birthdate = user_info.birthdate
            user_info.updated_at = func.now()

        # commit the transaction after 'with' block
        session.flush()
        return {"user info successfully updated"}, 200
    except Exception as e:
        logging.error(str(e))
        return {"error": "Error updating a user info", "details: ": str(e)}, 500
