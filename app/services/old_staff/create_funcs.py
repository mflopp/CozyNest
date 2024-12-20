import logging
from models.users import UserRole, Gender, UserSettings, UserInfo, User
from models.addresses import Country

logging.basicConfig(level=logging.INFO)


def add_record(session, record, entity_name):
    """
    Adds a new record to the database and commits the session.
    Logs success or failure.

    Args:
        record: SQLAlchemy model instance to be added.
        entity_name (str): Name of the database table/entity for
        logging purposes.
    """
    try:
        session.add(record)
        session.commit()
        logging.info(f"{record} successfully added to {entity_name}.")
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to add {record} to {entity_name}: {str(e)}")
        raise


def create_role(session, role_name, description):
    """
    Creates a new user role and adds it to the database.

    Args:
        role_name (str): Name of the role.
        description (str): Description of the role.

    Returns:
        UserRole: The created role instance.
    """
    role = UserRole(role=role_name, description=description)
    add_record(session, role, 'UserRole')
    return role


def create_gender(session, gender_name, description):
    """
    Creates a new gender and adds it to the database.

    Args:
        gender_name (str): Name of the gender.
        description (str): Description of the gender.

    Returns:
        Gender: The created gender instance.
    """
    gender = Gender(gender=gender_name, description=description)
    add_record(session, gender, 'Gender')
    return gender


def create_setting(session, currency, language):
    """
    Creates a new user setting and adds it to the database.

    Args:
        currency (str): Preferred currency.
        language (str): Preferred language.

    Returns:
        UserSettings: The created settings instance.
    """
    setting = UserSettings(currency=currency, language=language)
    add_record(session, setting, 'UserSettings')
    return setting


def create_user_info(session, gender, setting,
                     first_name, last_name, birthdate):
    """
    Creates a new user info record and adds it to the database.

    Args:
        gender (Gender): Gender instance for the user.
        setting (UserSettings): Settings instance for the user.
        first_name (str): User's first name.
        last_name (str): User's last name.
        birthdate (str): User's birth date (YYYY-MM-DD format).

    Returns:
        UserInfo: The created user info instance.
    """
    user_info = UserInfo(
        gender_id=gender.id,
        user_settings_id=setting.id,
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate
    )
    add_record(session, user_info, 'UserInfo')
    return user_info


def create_user(session, role, info, email, password, phone):
    """
    Creates a new user and adds it to the database.

    Args:
        role (UserRole): Role instance for the user.
        info (UserInfo): UserInfo instance for the user.
        email (str): User's email address.
        password (str): User's password.
        phone (str): User's phone number.

    Returns:
        User: The created user instance.
    """
    user = User(
        role_id=role.id,
        info_id=info.id,
        email=email,
        password=password,
        phone=phone
    )
    add_record(session, user, 'Users')
    return user


def create_country(session, name):
    country = Country(
        name=name
    )
    add_record(session, country, 'Countries')
    return country
