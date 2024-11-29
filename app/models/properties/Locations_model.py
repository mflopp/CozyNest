from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

Base = declarative_base()

# -- Validation MUST be added

# Define Models
class Countries(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Regions(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    name = Column(String, nullable=False)
    country = relationship("Countries")

class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    name = Column(String, nullable=False)
    region = relationship("Regions")
    

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
