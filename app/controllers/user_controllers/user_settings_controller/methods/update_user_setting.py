import logging
from sqlalchemy.orm import Session
from .get_user_setting_by_id import fetch_user_setting_by_id


def update_user_setting(id: int, user_data: dict, session: Session):

    try:
        with session.begin_nested():

            # # Chech if UserSettings update needed
            if 'currency' in user_data or 'language' in user_data:
                user_setting_current = fetch_user_setting_by_id(id, session)

                if 'currency' not in user_data:
                    user_data['currency'] = user_setting_current.currency
                if 'language' not in user_data:
                    user_data['language'] = user_setting_current.language
                # Check if new UserSettings exists in the DB, if not, create it
                user_setting = fetch_user_setting(user_data, session)
                if user_setting:
                    return user_setting.id
                else:
                    raise Exception(f"currency/language pair {user_data['currency']}/{user_data['language']} not found in the DB")
            else:
                return False

    except Exception:
        raise
