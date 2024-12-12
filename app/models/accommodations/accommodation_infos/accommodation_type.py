from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base


class AccommodationType(Base):
    __tablename__ = 'accommodation_types'

    id = Column(Integer, primary_key=True)
    accommodation_type = Column(
        String,
        unique=True,
        nullable=False,
        default='Apartment'
    )

    accommodation = relationship(
        "Accommodation", back_populates='accommodation_types'
    )

    def __repr__(self) -> str:
        return (f"<accommodationType(id={self.id},"
                f" accommodation_type='{self.accommodation_type}')>")
