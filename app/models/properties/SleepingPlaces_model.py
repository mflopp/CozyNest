from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from Items_model import Items

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

Base = declarative_base()

# -- Validation MUST be added

# Define Enum types
place_type = Enum('single bed', 'double bed', 'single sofa', 'double sofa', 'king bed', name='place_type')


# Define Models
class SleepingPlaces(Base):
    __tablename__ = 'sleepingplaces'
    id = Column(Integer, primary_key=True)
    type = Column(place_type)
    capacity = Column(Integer, CheckConstraint('capacity >= 1 AND capacity <= 2'), default=1) # Ensuring rating is between 1 and 5

class SleepingPlacesPerItem(Base):
    __tablename__ = 'sleepingplacesperitem'
    id = Column(Integer, primary_key=True)
    sleeping_place_id = Column(Integer, ForeignKey('sleepingplaces.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    place = relationship("SleepingPlaces")
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
