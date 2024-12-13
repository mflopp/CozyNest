from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationImage(Base):
    __tablename__ = 'accommodation_images'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )

    src = Column(String, nullable=False)

    accommodation = relationship(
        "Accommodation", back_populates='accommodation_image'
    )

    def __repr__(self):
        return (f"<AccommodationImage(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"src='{self.src}')>")
