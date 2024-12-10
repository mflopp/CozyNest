from sqlalchemy.orm import Session
from models import Gender


from controllers.controller_utils import (
    Validator,
    CRUDHelper
)


def add_gender(gender_data: dict, session: Session):

    fields = ['gender', 'description']
    Validator.validate_required_fields(fields, gender_data)
    Validator.validate_unique_fields(session, Gender, fields, gender_data)

    gender = Gender(
        gender=gender_data['gender'],
        description=gender_data['description']
    )

    return CRUDHelper.add(session, gender)
