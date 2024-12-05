from models.users import UserInfo, UserRole, Gender, UserSettings
from sqlalchemy.sql import func
import logging

def init_reserved_records(session):
    """
    Initialize the database by creating all tables defined in the models.
    This function will create the tables if they don't exist already.
    It will also insert default values into the specified tables.
    """
    try:
        
        # Create tables
        # Base.metadata.create_all(bind=engine)
        # print("Connected and tables created.")
        
        # Start a new transaction
        session.begin_nested()
        
        # Create UserRoles
        user_role_admin = UserRole(
            role="Admin",
            description="Administrator role"
        )
        user_role_owner = UserRole(
            role="Owner",
            description="Owner of the property role"
        )
        user_role_user = UserRole(
            role="User",
            description="Regular user role"
        )
        session.add(user_role_admin)
        session.add(user_role_owner)
        session.add(user_role_user)
        session.commit()
        logging.info(f"Default user roles created")
        
        # Create Genders
        gender_male = Gender(
            gender="Male",
            description="Male gender"
        )
        gender_female = Gender(
            gender="Female",
            description="Female gender"
        )
        gender_other = Gender(
            gender="Other",
            description="Other gender"
        )
        session.add(gender_male)
        session.add(gender_female)
        session.add(gender_other)
        session.commit()
        logging.info(f"Default genders created")

        # Create UserSettings
        user_settings = UserSettings(
            currency='USD',
            language='ENG',
        )
        session.add(user_settings)
        session.commit()
        logging.info(f"Default user settings created")
        
        # Create UserInfo
        user_info = UserInfo(
            gender_id=1,
            user_settings_id=1,
            first_name='first_name',
            last_name='last_name',
            birthdate = "01.01.1900",
            created_at=func.now(),
            updated_at=func.now()
        )
        session.add(user_info)
        session.commit()
        logging.info(f"Default user info created")
        
    except Exception as e:
        print(f"Error inserting default values (User roles, user settings, user info, genders): {e}")

