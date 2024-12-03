from sqlalchemy import Column, Integer, String
from config import Base


class AccommodationType(Base):
    """
    Represents different types of accommodation options available.

    This class defines the schema for the 'accommodation_types' table,
    which stores information about various accommodation categories,
    such as 'Apartment', 'House', 'Villa', etc.

    Attributes:
        id (int): The primary key for the accommodation type.
        accommodation_type (str): The type of accommodation,
                                  defaulting to 'Apartment'.

    Table:
        Name: 'accommodation_types'
        Columns:
            - id: Primary key, Integer, Not Null
            - accommodation_type: Name of the accommodation type, String,
                                  Not Null, Unique

    Example:
        To create a new accommodation type:
        >>> new_type = accommodationType(accommodation_type='Villa')
        >>> session.add(new_type)
        >>> session.commit()

        To query accommodation types:
        >>> accommodation_types = session.query(accommodationType).all()
        >>> for ht in accommodation_types:
        >>>     print(ht)
        <accommodationType(id=1, accommodation_type='Apartment')>
    """
    __tablename__ = 'accommodation_types'

    id = Column(Integer, primary_key=True)
    accommodation_type = Column(
        String,
        unique=True,
        nullable=False,
        default='Apartment'
    )

    def __repr__(self) -> str:
        return (f"<accommodationType(id={self.id},"
                f" accommodation_type='{self.accommodation_type}')>")
