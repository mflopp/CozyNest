import logging
from models.users import UserRole, Gender, UserSettings, UserInfo, User
from models.addresses import Country

from .create_user_test import session

from .create_funcs import (
    create_gender, create_role, create_setting,
    create_user, create_user_info, create_country
)


def get_first_record_by_criteria(
    Model: type,
    filter_criteria: dict
) -> object | None:
    """Retrieve the first record from the database that matches
    the given criteria."""
    return session.query(Model).filter_by(**filter_criteria).first()


def record_exists(Model: type, filter_criteria: dict) -> bool:
    """Check if a record exists in the database for the given criteria."""
    return get_first_record_by_criteria(Model, filter_criteria) is not None


def create_role_if_not_exists(role: str, desc: str) -> None:
    """Create a role if it does not already exist."""
    if not record_exists(UserRole, {"role": role}):
        create_role(session, role, desc)


def create_gender_if_not_exists(gender: str, desc: str) -> None:
    """Create a gender entry if it does not already exist."""
    if not record_exists(Gender, {"gender": gender}):
        create_gender(session, gender, desc)


def create_setting_if_not_exists(currency: str, lang: str) -> None:
    """Create a user setting if it does not already exist."""
    if not record_exists(
        UserSettings, {"currency": currency, "language": lang}
    ):
        create_setting(session, currency, lang)


def create_info_if_not_exists(
    f_name: str, l_name: str, gender: str,
    currency: str, lang: str, b_date: str
) -> None:
    """Create user info if it does not already exist."""
    if not record_exists(
        UserInfo, {"first_name": f_name, "last_name": l_name}
    ):
        gender_obj = get_first_record_by_criteria(Gender, {"gender": gender})
        setting_obj = get_first_record_by_criteria(
            UserSettings, {"currency": currency, "language": lang}
        )
        create_user_info(session, gender_obj, setting_obj,
                         f_name, l_name, b_date)


def create_user_if_not_exists(
    role: str, email: str, pswd: str,
    phone: str, f_name: str, l_name: str
) -> None:
    """Create a user if it does not already exist."""
    if not record_exists(User, {"email": email}):
        role_obj = get_first_record_by_criteria(UserRole, {"role": role})
        info_obj = get_first_record_by_criteria(
            UserInfo, {"first_name": f_name, "last_name": l_name}
        )
        create_user(session, role_obj, info_obj, email, pswd, phone)


def create_country_if_not_exists(
    name: str
) -> None:
    """Create a country if it does not already exist."""
    if not record_exists(Country, {"name": name}):
        create_country(session, name)


def test_users_create_if_not_exist() -> None:
    """Add predefined test users and associated data to the database
    if they do not already exist."""
    try:
        logging.info("Starting to add test data.")

        # Create roles
        create_role_if_not_exists("Admin", "Administrator role")
        # create_role_if_not_exists("Owner", "Owner of the property role")
        create_role_if_not_exists("User", "Regular user role")

        # Create genders
        create_gender_if_not_exists("Male", "Male gender")
        create_gender_if_not_exists("Female", "Female gender")

        # Create settings
        create_setting_if_not_exists("USD", "ENG")
        create_setting_if_not_exists("EUR", "RUS")

        # Create user info
        create_info_if_not_exists(
            "John", "Smith", "Male", "USD", "ENG", "1980-01-20"
        )
        create_info_if_not_exists(
            "Sarah", "Connor", "Female", "USD", "ENG", "1970-01-30"
        )
        create_info_if_not_exists(
            "Donald", "Trump", "Male", "USD", "ENG", "1960-01-22"
        )

        # Create users
        create_user_if_not_exists(
            "Admin", "john@ma.il", "qweQWE1!",
            "123-456-7890", "John", "Smith"
        )
        create_user_if_not_exists(
            "User", "sarah@ma.il", "qweQWE1!",
            "098-765-4321", "Sarah", "Connor"
        )
        create_user_if_not_exists(
            "User", "donaldh@ma.il", "qweQWE1!",
            "123-777-5555", "Donald", "Trump"
        )
        create_country_if_not_exists(
            "Israel"
        )
        create_country_if_not_exists(
            "USA"
        )
        create_country_if_not_exists(
            "France"
        )
        create_country_if_not_exists(
            "Norway"
        )
        create_country_if_not_exists(
            "Ukraine"
        )
        create_country_if_not_exists(
            "Russia"
        )

        logging.info("Test data added successfully.")
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to add test data: {e}")
    finally:
        session.close()
