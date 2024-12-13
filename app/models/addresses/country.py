from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    region = relationship("Region", back_populates='country')

    def __repr__(self):
        return f"<Country(id={self.id}, name='{self.name}')>"
