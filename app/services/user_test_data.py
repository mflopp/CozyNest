import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UserRoles, Genders, UserSettings, UserInfos, Users
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

# Initialize the database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_test_users():
    try:
        # Add test data to UserRoles
        user_role_admin = UserRoles(role="Admin", description="Administrator role")
        user_role_owner = UserRoles(role="Owner", description="Owner of the property role")
        user_role_user = UserRoles(role="User", description="Regular user role")
        session.add(user_role_admin)
        session.add(user_role_owner)
        session.add(user_role_user)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserRoles")
                     
        # Add test data to Genders
        gender_male = Genders(gender="Male", description="Male gender")
        gender_female = Genders(gender="Female", description="Female gender")
        session.add(gender_male)
        session.add(gender_female)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to Genders")
        
        # Add test data to UserSettings
        user_setting_usd_eng = UserSettings(currency="USD", language="ENG")
        user_setting_eur_ru = UserSettings(currency="EUR", language="RU")
        session.add(user_setting_usd_eng)
        session.add(user_setting_eur_ru)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserSettings")

        # Add test data to UserInfos
        user_info_john = UserInfos(gender_id=gender_male.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="John", last_name="Smith",
                                   birthdate="1980-01-20")
        user_info_jane = UserInfos(gender_id=gender_female.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="Sarah", last_name="Connor",
                                   birthdate="1970-01-30")
        user_info_user = UserInfos(gender_id=gender_male.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="Donald", last_name="Trump",
                                   birthdate="1960-01-22")
        session.add(user_info_john)
        session.add(user_info_jane)
        session.add(user_info_user)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserInfos")

        # Add test data to Users
        user_john = Users(role_id=user_role_admin.id,
                          info_id=user_info_john.id,
                          email="john@ma.il",
                          password="qweQWE1!",
                          phone="123-456-7890")
        user_jane = Users(role_id=user_role_owner.id,
                          info_id=user_info_jane.id,
                          email="sarah@ma.il",
                          password="qweQWE1!",
                          phone="098-765-4321")
        user_user = Users(role_id=user_role_user.id,
                          info_id=user_info_user.id,
                          email="donaldh@ma.il",
                          password="qweQWE1!",
                          phone="123-777-5555")
        session.add(user_john)
        session.add(user_jane)
        session.add(user_user)
        logging.info("Test data added to Users")

        # Commit the session to save changes
        session.commit()
        print("Test data added successfully")
    except Exception as e:
        session.rollback()
        print(f"Failed to add test data: {str(e)}")
    finally:
        session.close()

# -- Another function with existance checks to restore deleted users
def add_test_users_check_if():
    try:
        # Check for existing roles and add if not present
        if not session.query(UserRoles).filter_by(role="Admin").first():
            session.add(UserRoles(role="Admin", description="Administrator role"))
        if not session.query(UserRoles).filter_by(role="Owner").first():
            session.add(UserRoles(role="Owner", description="Owner of the property role"))
        if not session.query(UserRoles).filter_by(role="User").first():
            session.add(UserRoles(role="User", description="Regular user role"))
        session.commit()  # Commit to generate IDs
        logging.info("Test data added to UserRoles")

        # Check for existing genders and add if not present
        if not session.query(Genders).filter_by(gender="Male").first():
            session.add(Genders(gender="Male", description="Male gender"))
        if not session.query(Genders).filter_by(gender="Female").first():
            session.add(Genders(gender="Female", description="Female gender"))
        session.commit()  # Commit to generate IDs
        logging.info("Test data added to Genders")

        # Check for existing user settings and add if not present
        if not session.query(UserSettings).filter_by(currency="USD", language="ENG").first():
            session.add(UserSettings(currency="USD", language="ENG"))
        if not session.query(UserSettings).filter_by(currency="EUR", language="RU").first():
            session.add(UserSettings(currency="EUR", language="RU"))
        session.commit()  # Commit to generate IDs
        logging.info("Test data added to UserSettings")

        # Add test data to UserInfos if not present
        if not session.query(UserInfos).filter_by(first_name="John", last_name="Smith").first():
            gender_male = session.query(Genders).filter_by(gender="Male").first()
            user_setting_usd_eng = session.query(UserSettings).filter_by(currency="USD", language="ENG").first()
            user_info_john = UserInfos(gender_id=gender_male.id,
                                       user_settings_id=user_setting_usd_eng.id,
                                       first_name="John", last_name="Smith",
                                       birthdate="1980-01-20")
            session.add(user_info_john)
        if not session.query(UserInfos).filter_by(first_name="Sarah", last_name="Connor").first():
            gender_female = session.query(Genders).filter_by(gender="Female").first()
            user_setting_usd_eng = session.query(UserSettings).filter_by(currency="USD", language="ENG").first()
            user_info_jane = UserInfos(gender_id=gender_female.id,
                                       user_settings_id=user_setting_usd_eng.id,
                                       first_name="Sarah", last_name="Connor",
                                       birthdate="1970-01-30")
            session.add(user_info_jane)
        if not session.query(UserInfos).filter_by(first_name="Donald", last_name="Trump").first():
            gender_male = session.query(Genders).filter_by(gender="Male").first()
            user_setting_usd_eng = session.query(UserSettings).filter_by(currency="USD", language="ENG").first()
            user_info_user = UserInfos(gender_id=gender_male.id,
                                       user_settings_id=user_setting_usd_eng.id,
                                       first_name="Donald", last_name="Trump",
                                       birthdate="1960-01-22")
            session.add(user_info_user)
        session.commit()  # Commit to generate IDs
        logging.info("Test data added to UserInfos")

        # Add test data to Users if not present
        if not session.query(Users).filter_by(email="john@ma.il").first():
            user_role_admin = session.query(UserRoles).filter_by(role="Admin").first()
            user_info_john = session.query(UserInfos).filter_by(first_name="John", last_name="Smith").first()
            user_john = Users(role_id=user_role_admin.id,
                              info_id=user_info_john.id,
                              email="john@ma.il",
                              password="qweQWE1!",
                              phone="123-456-7890")
            session.add(user_john)
        if not session.query(Users).filter_by(email="sarah@ma.il").first():
            user_role_owner = session.query(UserRoles).filter_by(role="Owner").first()
            user_info_jane = session.query(UserInfos).filter_by(first_name="Sarah", last_name="Connor").first()
            user_jane = Users(role_id=user_role_owner.id,
                              info_id=user_info_jane.id,
                              email="sarah@ma.il",
                              password="qweQWE1!",
                              phone="098-765-4321")
            session.add(user_jane)
        if not session.query(Users).filter_by(email="donaldh@ma.il").first():
            user_role_user = session.query(UserRoles).filter_by(role="User").first()
            user_info_user = session.query(UserInfos).filter_by(first_name="Donald", last_name="Trump").first()
            user_user = Users(role_id=user_role_user.id,
                              info_id=user_info_user.id,
                              email="donaldh@ma.il",
                              password="qweQWE1!",
                              phone="123-777-5555")
            session.add(user_user)
        session.commit()
        logging.info("Test data added to Users")

        print("Test data added successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to add test data: {str(e)}")
    finally:
        session.close()
        
if __name__ == "__main__":
    add_test_users()
