from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    name = Column(String, nullable=False)

    region = relationship("Region", back_populates='city')
    address = relationship("Address", back_populates='city')

    def __repr__(self):
        return (f"<City(id={self.id}, name='{self.name}', "
                f"region_id={self.region_id})>")
