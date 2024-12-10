import logging
from sqlalchemy.orm import Session

from models import UserSettings
from utils import Finder, Validator


def fetch_user_setting(data: dict, session: Session):
    try:
        # Validate that user_data contains 'currency' and 'language' keys
        fields = {'currency', 'language'}

        Validator.validate_required_fields(fields, data)

        user_setting = Finder.fetch_record_by_criteria(
            session=session,
            Model=UserSettings,
            criteria={"currency": data['currency'], "language": data['language']}
        )

        return user_setting
    except Exception as e:
        session.rollback()
        logging.error(f"Error getting a user setting: {str(e)}")
        raise
