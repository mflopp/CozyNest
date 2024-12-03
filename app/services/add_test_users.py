import logging
from .create_funcs import create_gender, create_role, create_setting
from .create_funcs import create_user, create_user_info

logging.basicConfig(level=logging.INFO)


def get_test_roles(session):
    """Returns predefined roles."""
    return {
        "admin": create_role(session, "Admin", "Administrator role"),
        "owner": create_role(session, "Owner", "Owner of the property role"),
        "user": create_role(session, "User", "Regular user role")
    }


def get_test_genders(session):
    """Returns predefined genders."""
    return {
        "male": create_gender(session, "Male", "Male gender"),
        "female": create_gender(session, "Female", "Female gender")
    }


def get_test_settings(session):
    """Returns predefined user settings."""
    return {
        "usd_eng": create_setting(session, "USD", "ENG"),
        "eur_ru": create_setting(session, "EUR", "RU")
    }


def get_test_user_infos(session):
    """
    Returns predefined user information records.
    Combines genders and settings for creating user info.
    """
    genders = get_test_genders(session)
    settings = get_test_settings(session)

    return {
        "john": create_user_info(
            session,
            genders["male"], settings["usd_eng"],
            "John", "Smith", "1980-01-20"
        ),
        "jane": create_user_info(
            session,
            genders["female"], settings["usd_eng"],
            "Sarah", "Connor", "1970-01-30"
        ),
        "donald": create_user_info(
            session,
            genders["male"], settings["usd_eng"],
            "Donald", "Trump", "1960-01-22"
        ),
    }


def test_users_create(session):
    """Adds predefined users with their roles and information."""
    try:
        roles = get_test_roles(session)
        infos = get_test_user_infos(session)

        test_users = {
            "john": create_user(
                session,
                roles["admin"], infos["john"],
                "john@ma.il", "qweQWE1!", "123-456-7890"
            ),
            "jane": create_user(
                session,
                roles["owner"], infos["jane"],
                "sarah@ma.il", "qweQWE1!", "098-765-4321"
            ),
            "donald": create_user(
                session,
                roles["user"], infos["donald"],
                "donaldh@ma.il", "qweQWE1!", "123-777-5555"
            ),
        }

        logging.info("Test users added successfully.")
        return test_users
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to add test data: {str(e)}")
    finally:
        session.close()
