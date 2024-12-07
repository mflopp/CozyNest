import logging
from sqlalchemy.orm import Session
from .get_user_setting_by_id import fetch_user_setting_by_id
from .create_user_setting import add_user_setting

def update_user_setting(id: int, user_data: dict, session: Session):
    
    try:
        with session.begin_nested():

            # # Chech if UserSettings update needed
            if 'currency' in user_data or 'language' in user_data:
                user_setting = fetch_user_setting_by_id(id, session)
                
                if not user_setting:
                    return False
                if 'currency' not in user_data:
                    user_data['currency'] = user_setting.currency
                if 'language' not in user_data:
                    user_data['language'] = user_setting.language
                # Check if new UserSettings exists in the DB, if not, create it
                response, status = add_user_setting(user_data, session)
                if status != 200:
                    logging.error(f"user setting was not provided from the DB, Error: {response}")
                    raise ValueError(f"User setting was not provided from the DB, Error: {response}")

                user_setting_id = response["id"]
                
                # commit the transaction within 'with' block
                session.flush()
                
                return user_setting_id
            else:
                return False

    except Exception as e:
        logging.error(str(e))
        return {"error": "Error getting a user setting", "details: ": str(e)}, 500
