from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models import Base  # Import the shared Base from your base.py
# import psycopg2
# Import all models to ensure they are registered with Base
from models import Users, UserInfos, UserRoles, Genders, UserSettings
from models import HousingTypes, Rules, ItemAddress, Items, RulesPerItem, ItemAvailability, ItemsImage
from models import AmenitiesCategories, Amenities, AmenitiesPerItem
from models import Cities, Countries, Regions
from models import SleepingPlaces, SleepingPlacesPerItem
from models import Orders
from models import Reviews


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

# Initialize the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize the database by creating all tables.
    """
    Base.metadata.create_all(bind=engine)
    print("Connected and created tables")

def get_db():
    """
    Dependency to get a SQLAlchemy session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -- Older version:

# global DATABASE_URL
# def init_db():
#     global DATABASE_URL
#     load_dotenv()
#     DATABASE_URL = os.getenv("DATABASE_URL", "*")

#     # Initialize the database
#     engine = create_engine(DATABASE_URL)
#     Base.metadata.create_all(engine)  # Create all tables


    # connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        

#     with psycopg2.connect(DATABASE_URL, sslmode='require') as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
# BEGIN;

# DROP TABLE IF EXISTS Users;
# DROP TABLE IF EXISTS UserRoles;
# DROP TABLE IF EXISTS UserInfos;
# DROP TABLE IF EXISTS Genders;
# DROP TABLE IF EXISTS UserSettings;


# -- Drop and create ENUM types
# DROP TYPE IF EXISTS currency_type CASCADE;
# CREATE TYPE currency_type AS ENUM ('USD', 'EUR', 'ILS/NIS', 'RUB');

# DROP TYPE IF EXISTS language_type CASCADE;
# CREATE TYPE language_type AS ENUM ('ENG', 'RU', 'HEB');

# -- Create Tables
# CREATE TABLE IF NOT EXISTS UserRoles (
#     id SERIAL PRIMARY KEY,
#     role TEXT UNIQUE NOT NULL,
#     description TEXT
# );

# CREATE TABLE IF NOT EXISTS Genders (
#     id SERIAL PRIMARY KEY,
#     gender TEXT UNIQUE NOT NULL,
#     description TEXT
# );

# CREATE TABLE IF NOT EXISTS UserSettings (
#     id SERIAL PRIMARY KEY,
#     currency currency_type DEFAULT 'USD',
#     language language_type DEFAULT 'ENG'
# );

# CREATE TABLE IF NOT EXISTS UserInfos (
#     id SERIAL PRIMARY KEY,
#     gender_id INTEGER NOT NULL,
#     user_settings_id INTEGER NOT NULL,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     birthdate DATE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_settings_id) REFERENCES UserSettings(id),
#     FOREIGN KEY (gender_id) REFERENCES Genders(id)
# );

# CREATE TABLE IF NOT EXISTS Users (
#     id SERIAL PRIMARY KEY,
#     role_id INTEGER NOT NULL,
#     info_id INTEGER NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     password TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     phone TEXT UNIQUE NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (role_id) REFERENCES UserRoles(id),
#     FOREIGN KEY (info_id) REFERENCES UserInfos(id)
# );

# COMMIT;
#  """)
  
#         conn.commit()
#     print("Connected and created tables")
    

# def get_db_conn():
#     return  psycopg2.connect(DATABASE_URL, sslmode='require')