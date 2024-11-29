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


# Define Models
class AmenitiesCategories(Base):
    __tablename__ = 'amenitiescategories'
    id = Column(Integer, primary_key=True)
    category = Column(String, unique=True, nullable=False)

class Amenities(Base):
    __tablename__ = 'amenities'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('amenitiescategories.id'), nullable=False)
    name = Column(String, nullable=False)
    category = relationship("AmenitiesCategories")

class AmenitiesPerItem(Base):
    __tablename__ = 'amenitiesperitem'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    amenities_id = Column(Integer, ForeignKey('amenities.id'), nullable=False)
    name = Column(String, nullable=False)
    item = relationship("Items")
    amenity = relationship("Amenities")
    

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
