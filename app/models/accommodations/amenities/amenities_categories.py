from sqlalchemy import Column, Integer, String
from config import Base
from sqlalchemy.orm import relationship


class AmenitiesCategory(Base):

    __tablename__ = 'amenities_categories'

    id = Column(Integer, primary_key=True)
    category = Column(String, unique=True, nullable=False)

    amenity = relationship(
        "Amenity", back_populates='amenities_category'
    )

    def __repr__(self):
        return (f"<AmenitiesCategory(id={self.id},"
                f" category='{self.category}')>")
