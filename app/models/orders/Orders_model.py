from sqlalchemy import DECIMAL, create_engine, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
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
class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # -- payment_id ?????
    total_price = Column(DECIMAL(10, 2), nullable=False) # Ensures the total_price has two decimal points
    date_checkin = Column(Date, nullable=False)
    date_checkout = Column(Date, nullable=False)
    people_amount = Column(Integer, default=1)
    confirmation_code = Column(String)
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
