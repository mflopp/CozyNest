from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey('amenities_categories.id'),
        nullable=False
    )

    name = Column(String, nullable=False)

    amenities_category = relationship(
        "AmenitiesCategory", back_populates='amenity'
    )
    accommodation_amenity = relationship(
        "AccommodationAmenity", back_populates='amenity'
    )

    def __repr__(self) -> str:
        return (f"<Amenity(id={self.id}, name={repr(self.name)}, "
                f"category_id={self.category_id})>")
