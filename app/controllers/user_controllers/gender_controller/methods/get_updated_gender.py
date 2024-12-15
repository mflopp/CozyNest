from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from .get_gender import fetch_gender


def get_updated_gender(user_data: dict, session: Session):

    try:
        with session.begin_nested():

            # Chech if Gender update needed
            if 'gender' in user_data:
                gender_new = user_data["gender"]
                # Fetch Gender
                gender = fetch_gender(
                    'gender',
                    {"gender": gender_new},
                    session
                )
                if gender:
                    # return new gender id
                    return gender.id
                else:
                    raise ValueError(
                        f"Gender {gender_new} not found in the DB"
                    )
            else:
                return None

    except (ValueError, SQLAlchemyError, Exception):
        raise
