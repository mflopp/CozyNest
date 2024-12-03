from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AccommodationImage(Base):
    """
    Represents an image associated with an accommodation in the system.

    Attributes:
        id (int): The primary key of the record.
        accommodation_id (int): A foreign key linking to the 'accommodations'
                                table.
        src (str): The source URL or path to the image file.
        accommodation (Accommodation): A relationship object representing
                                       the associated accommodation.

    Relationships:
        accommodation: Establishes a relationship with the `Accommodation`
                       model.

    Example:
        >>> accommodation_image = AccommodationImage(
            accommodation_id=1,
            src="path/to/image.jpg"
            )
        >>> print(accommodation_image)
        <AccommodationImage(id=1, accommodation_id=1, src='path/to/image.jpg')>
    """
    __tablename__ = 'accommodation_images'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )

    src = Column(String, nullable=False)

    accommodation = relationship("Accommodation")

    def __repr__(self):
        return (f"<AccommodationImage(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"src='{self.src}')>")
