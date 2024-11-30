from sqlalchemy import DECIMAL, Float, create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from Locations_model import Cities
from ..users.Users_model import Users

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

Base = declarative_base()

# -- Validation MUST be added

# Define Enum types
item_type = Enum('House', 'Apartment', 'Room', name='item_type')


# Define Models
class HousingTypes(Base):
    __tablename__ = 'housingtypes'
    id = Column(Integer, primary_key=True)
    type = Column(item_type, default='Apartment')

class Rules(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule = Column(String, unique=True, nullable=False)

class ItemAddress(Base):
    __tablename__ = 'itemaddress'
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    street = Column(String, nullable=False)
    building = Column(String, nullable=False)
    apartment = Column(String)
    zip_code = Column(String, nullable=False)
    altitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = relationship("Cities")
    
class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    housing_type_id = Column(Integer, ForeignKey('housingtypes.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address_id = Column(Integer, ForeignKey('itemaddress.id'), nullable=False)
    description = Column(String)
    rooms_number = Column(Integer, default=1)
    max_capacity = Column(Integer, default=1)
    price = Column(DECIMAL(10, 2), nullable=False) # Ensures the price has two decimal points
    status = Column(String, default="active")
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    housingtype = relationship("HousingTypes")
    user = relationship("Users")
    address = relationship("ItemAddress")

class RulesPerItem(Base):
    __tablename__ = 'rulesperitem'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    rule_id = Column(Integer, ForeignKey('rules.id'), nullable=False)
    item = relationship("Items")
    rule = relationship("Rules")

class ItemAvailability(Base):
    __tablename__ = 'itemavailability'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    date_available_from = Column(Date, nullable=False)
    date_available_to = Column(Date, nullable=False)
    time_checkin = Column(String, nullable=False)
    time_checkout = Column(String, nullable=False)
    item = relationship("Items")

class ItemsImage(Base):
    __tablename__ = 'itemsimage'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    src = Column(String, nullable=False)
    item = relationship("Items")

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
