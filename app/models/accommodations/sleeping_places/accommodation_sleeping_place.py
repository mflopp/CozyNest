from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationSleepingPlace(Base):
    """
    Represents the relationship between accommodations and sleeping places
    in the system.

    This model defines the relationship between accommodations
    and sleeping places, linking them together in
    the 'accommodation_sleeping_places' table.

    Attributes:
        id (int): The primary key of the record.
        sleeping_place_id (int): Foreign key referencing the 'sleeping_places'
                                 table.
        accommodation_id (int): Foreign key referencing the 'accommodations'
                                table.
        sleeping_place (SleepingPlace): A relationship object representing
                                        the associated sleeping place.
        accommodation (Accommodation): A relationship object representing
                                       the associated accommodation.

    Example:
        >>> accommodation_sleeping_place = AccommodationSleepingPlace(
                sleeping_place_id=1,
                accommodation_id=2
            )
        >>> print(accommodation_sleeping_place)
        <AccommodationSleepingPlace(id=1, sleeping_place_id=1,
        accommodation_id=2)>
    """
    __tablename__ = 'accommodation_sleeping_places'

    id = Column(Integer, primary_key=True)

    sleeping_place_id = Column(
        Integer,
        ForeignKey('sleeping_places.id'),
        nullable=False
    )
    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )

    sleeping_place = relationship("SleepingPlace")
    accommodation = relationship("Accommodation")

    def __repr__(self):
        return (f"<AccommodationSleepingPlace(id={self.id}, "
                f"sleeping_place_id={self.sleeping_place_id}, "
                f"accommodation_id={self.accommodation_id})>")
