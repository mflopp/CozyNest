from sqlalchemy import DECIMAL, Float, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from models import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

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
    
    def __init__(self, **kwargs):
        from .Locations_model import Cities  # Local import within the class
        self.city = kwargs.get('city')
    
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
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
    housingtype = relationship("HousingTypes")
    user = relationship("Users")
    address = relationship("ItemAddress")

    def __init__(self, **kwargs):
        from models.users.Users_model import Users  # Local import within the class
        self.user = kwargs.get('user')
        
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

