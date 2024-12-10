import logging
from sqlalchemy.orm import Session
from models.users import UserSettings

from .get_user_setting import fetch_user_setting


def add_user_setting(user_data: dict, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():
        
            # ISO 639-3 language codes are used
            fields = ['currency', 'language']

            validate_data(
                session=session,
                Model=UserSettings,
                data=user_data,
                required_fields=fields,
                unique_fields=[]  # ???
            )
            # Check if default UserSettings exists, if not, create it
            user_setting = fetch_user_setting(user_data, session)
            if user_setting:
                logging.info(f"currency/language combination {user_data['currency']}/{user_data['language']} already exists in the DB")
                return {"message": f"currency/language combination {user_data['currency']}/{user_data['language']} already exists in the DB", "id": user_setting.id}, 200
            # Create new UserSettings record
            user_setting = UserSettings(currency=user_data['currency'], language=user_data['language'])
            response, status = add_record(session, user_setting, 'user settings')
            if status != 200:
                logging.error(f"user setting was not created (add_user_setting), Error: {response}")
                raise Exception(f"Failed to create user setting, Error: {response}")
            
        session.commit()
        return response, status
    except Exception as e:
        logging.error(str(e))
        return {"error": "Error creating a user setting", "details: ": str(e)}, 500
