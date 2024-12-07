import logging
from sqlalchemy.orm import Session
from controllers.general_controllers import add_record
from models.users import UserSettings
from controllers.controller_utils.validations import validate_data

from .get_user_setting import fetch_user_setting

def add_user_setting(user_data: dict, session: Session):
    
    try:
        # Start a new transaction
        # with session.begin_nested():
        
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
        print(f"\033[34m ############# add_user_setting before add_record: {user_setting}\033[0m")
        response, status = add_record(session, user_setting, 'user settings')
        print(f"\033[34m ############# add_user_setting after add_record: {status}\033[0m")
        if status != 200:
            logging.error(f"user setting was not created (add_user_setting), Error: {response}")
            raise Exception(f"Failed to create user setting, Error: {response}")
        
        # commit the transaction after 'with' block
        print(f"\033[34m ############# add_user_setting: {response}\033[0m")
        return response, status
    except Exception as e:
        print(f"\033[34m ############# add_user_setting EXCEPTION: {e}\033[0m")
        session.rollback() # Rollback if there's an error
        logging.error(str(e))
        return {"error": "Error creating a user setting", "details: ": str(e)}, 500
