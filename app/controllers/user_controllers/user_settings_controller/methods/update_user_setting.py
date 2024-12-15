from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from utils import Validator
from utils.error_handler import ValidationError

from .get_user_setting_by_id import fetch_user_setting_by_id
from .get_user_setting import fetch_user_setting


def update_user_setting(id: int, user_data: dict, session: Session):

    try:
        with session.begin_nested():

            # Chech if UserSettings update needed
            if 'currency' in user_data or 'language' in user_data:
                # getting parameters from the request
                currency_new = user_data.get('currency')
                language_new = user_data.get('language')
                # validating the currency
                if currency_new:
                    Validator.validate_currency(currency_new)
                # validating the language (ISO 639-3 codes are used)
                if language_new:
                    Validator.validate_language(language_new)
                user_setting_current = fetch_user_setting_by_id(id, session)

                # using current values if one of them is missing
                if not currency_new:
                    currency_new = user_setting_current.currency
                    user_data['currency'] = currency_new
                if not language_new:
                    language_new = user_setting_current.language
                    user_data['language'] = language_new
                # Check if new UserSettings exists in the DB
                user_setting = fetch_user_setting(user_data, session)
                if user_setting:
                    return user_setting.id
                else:
                    raise ValueError(
                        f"currency/language pair {currency_new}"
                        f"/{language_new} not found in the DB"
                    )
            else:
                return None

    except (ValueError, ValidationError, SQLAlchemyError, Exception):
        raise
