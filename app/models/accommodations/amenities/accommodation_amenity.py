from sqlalchemy import Column, Integer, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


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

    accommodation = relationship("Accommodation")
    amenity = relationship("Amenity")

    def __repr__(self) -> str:
        return (f"<AccommodationAmenity(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"amenities_id={self.amenities_id})>")
