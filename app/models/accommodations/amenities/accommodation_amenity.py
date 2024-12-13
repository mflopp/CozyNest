from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationAmenity(Base):
    __tablename__ = 'accommodation_amenities'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )
    amenities_id = Column(
        Integer,
        ForeignKey('amenities.id'),
        nullable=False
    )

    amenity = relationship(
        "Amenity", back_populates='accommodation_amenity'
    )
    accommodation = relationship(
        "Accommodation", back_populates='accommodation_amenity'
    )

    def __repr__(self) -> str:
        return (f"<AccommodationAmenity(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"amenities_id={self.amenities_id})>")
