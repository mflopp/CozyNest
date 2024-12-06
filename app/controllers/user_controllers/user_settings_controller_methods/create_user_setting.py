import logging
from sqlalchemy.orm import Session
from controllers.general_controllers import add_record
from models.users import UserSettings
from controllers.controller_utils.validations import validate_data

from .get_user_setting import fetch_user_setting

def add_user_setting(user_data: dict, session: Session):
    
    try:
        # Start a new transaction
        session.begin_nested()
        
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
            return {"message": f"currency/language combination {user_data['currency']}/{user_data['language']} already exists in the DB", "id": user_setting.id}, 200
        user_setting = UserSettings(currency=user_data['currency'], language=user_data['language'])
        response, status = add_record(session, user_setting, 'UserSettings')

        return response, status
    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error creating a user setting", "details: ": str(e)}, 500
