from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationAvailability(Base):
    """
    Represents the availability of an accommodation item for a specific period.

    Attributes:
        id (int): The primary key of the record.
        accommodation_id (int): A foreign key linking to
                                the 'accommodations' table.
        date_available_from (date): The date from which the accommodation
                                    is available.
        date_available_to (date): The date until which the accommodation
                                  is available.
        time_checkin (str): The time when guests can check-in.
        time_checkout (str): The time when guests must check-out.
        accommodation (Accommodation): A relationship object representing
                                       the associated accommodation.

    Relationships:
        accommodation: Establishes a relationship with the `Accommodation`
                       model.

    Example:
        >>> availability = AccommodationAvailability(
                accommodation_id=1, date_available_from='2024-12-01',
                date_available_to='2024-12-31', time_checkin='14:00',
                time_checkout='11:00'
            )
        >>> print(availability)
        <AccommodationAvailability(id=1, accommodation_id=1,
        date_available_from='2024-12-01', date_available_to='2024-12-31',
        time_checkin='14:00', time_checkout='11:00')>
    """
    __tablename__ = 'accommodation_availability'

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

    accommodation = relationship("Accommodation")

    def __repr__(self):
        return (f"<AccommodationAvailability(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"date_available_from='{self.date_available_from}', "
                f"date_available_to='{self.date_available_to}', "
                f"time_checkin='{self.time_checkin}', "
                f"time_checkout='{self.time_checkout}')>")
