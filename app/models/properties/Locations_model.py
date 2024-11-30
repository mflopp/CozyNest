from sqlalchemy import Column, Integer, String, ForeignKey
from models import Base
from sqlalchemy.orm import relationship

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
