from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from ..properties.Items_model import Items
from ..users.Users_model import Users

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

Base = declarative_base()

# -- Validation MUST be added


# Define Models
class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False) # Ensuring rating is between 1 and 5
    comment = Column(String)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    item = relationship("Items")
    user = relationship("Users")

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
