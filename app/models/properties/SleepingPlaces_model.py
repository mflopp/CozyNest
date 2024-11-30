from sqlalchemy import CheckConstraint, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from models import Base
from sqlalchemy.orm import relationship

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

    def __init__(self, **kwargs):
        from .Items_model import Items  # Local import within the class
        self.item = kwargs.get('item')
