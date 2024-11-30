from sqlalchemy import Column, Integer, String, ForeignKey
from models import Base
from sqlalchemy.orm import relationship


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

    def __init__(self, **kwargs):
        from .Items_model import Items  # Local import within the class
        self.item = kwargs.get('item')

