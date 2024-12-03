from sqlalchemy import CheckConstraint, Column, Integer, String
from config import Base


class SleepingPlace(Base):
    """
    Represents a sleeping place (e.g., bed, couch) in an accommodation.

    Attributes:
        id (int): The primary key of the record.
        sleeping_place_type (str): The type of the sleeping place
        (e.g., single bed, double couch, etc.).
        capacity (int): The capacity of the sleeping place, limited to 1 or 2.

    Constraints:
        - capacity must be between 1 and 2 (inclusive).

    Example:
        >>> sleeping_place = SleepingPlace(
                sleeping_place_type="Single Bed",
                capacity=2
            )
        >>> print(sleeping_place)
        <SleepingPlace(id=1, sleeping_place_type='Bed', capacity=2)>
    """
    __tablename__ = 'sleeping_places'

    id = Column(Integer, primary_key=True)

    sleeping_place_type = Column(String(50), nullable=False)
    capacity = Column(
        Integer,
        CheckConstraint('capacity >= 1 AND capacity <= 2'),
        default=1
    )

    def __repr__(self):
        return (f"<SleepingPlace(id={self.id}, "
                f"sleeping_place_type='{self.sleeping_place_type}', "
                f"capacity={self.capacity})>")
