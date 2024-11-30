from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

Base = declarative_base()

# -- Validation MUST be added

# Define Enum types
currency_type = Enum('USD', 'EUR', 'ILS/NIS', 'RUB', name='currency_type')
language_type = Enum('ENG', 'RU', 'HEB', name='language_type')

# Define Models
class UserRoles(Base):
    __tablename__ = 'userroles'
    id = Column(Integer, primary_key=True)
    role = Column(String, unique=True, nullable=False)
    description = Column(String)

class Genders(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True)
    gender = Column(String, unique=True, nullable=False)
    description = Column(String)

class UserSettings(Base):
    __tablename__ = 'usersettings'
    id = Column(Integer, primary_key=True)
    currency = Column(currency_type, default='USD')
    language = Column(language_type, default='ENG')

class UserInfos(Base):
    __tablename__ = 'userinfos'
    id = Column(Integer, primary_key=True)
    gender_id = Column(Integer, ForeignKey('genders.id'), nullable=False)
    user_settings_id = Column(Integer, ForeignKey('usersettings.id'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthdate = Column(Date)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    gender = relationship("Genders")
    settings = relationship("UserSettings")

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('userroles.id'), nullable=False)
    info_id = Column(Integer, ForeignKey('userinfos.id'), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    role = relationship("UserRoles")
    info = relationship("UserInfos")

# Initialize the database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Your database operations here 

# Commit the session (if there are transactions to commit)
session.commit() 
# Close the session 
session.close()

print("Connected and created tables")
