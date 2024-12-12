from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationAvailability(Base):
    __tablename__ = 'accommodation_availabilities'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )

    date_available_from = Column(Date, nullable=False)
    date_available_to = Column(Date, nullable=False)
    time_checkin = Column(String, nullable=False)
    time_checkout = Column(String, nullable=False)

    accommodation = relationship(
        "Accommodation", back_populates='accommodation_availabilities'
    )

    def __repr__(self):
        return (f"<AccommodationAvailability(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"date_available_from='{self.date_available_from}', "
                f"date_available_to='{self.date_available_to}', "
                f"time_checkin='{self.time_checkin}', "
                f"time_checkout='{self.time_checkout}')>")
