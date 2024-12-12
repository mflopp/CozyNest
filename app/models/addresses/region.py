from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    name = Column(String, nullable=False)

    country = relationship("Country", back_populates='regions')
    city = relationship("City", back_populates='regions')

    def __repr__(self):
        return (f"<Region(id={self.id}, name='{self.name}', "
                f"country_id={self.country_id})>")
