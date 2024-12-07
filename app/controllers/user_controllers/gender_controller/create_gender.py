from sqlalchemy.orm import Session
from models.users import Gender


from controllers.controller_utils.validations import validate_data

from general_controllers import add_record


def add_gender(gender_data: dict, session: Session):

    fields = ['gender', 'description']

    validate_data(
        session=session,
        Model=Gender,
        data=gender_data,
        required_fields=fields,
        unique_fields=fields
    )

    gender = Gender(
        gender=gender_data['gender'],
        description=gender_data['description']
    )

    return add_record(session, gender, 'Gender')
