import psycopg2
import os
from dotenv import load_dotenv

global DATABASE_URL
def init_db():
    global DATABASE_URL
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL", "*")
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
    print("Connected and created tables")
    

def get_db_conn():
    return  psycopg2.connect(DATABASE_URL, sslmode='require')