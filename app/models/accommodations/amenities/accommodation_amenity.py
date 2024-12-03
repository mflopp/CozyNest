from sqlalchemy import Column, Integer, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class AccommodationAmenity(Base):
    """
    Represents the assignment of an amenity to a specific accommodation
    in the database.

    This class defines the schema for the 'accommodation_amenities' table,
    which links accommodations (e.g., rooms, properties) with their
    respective amenities.

    Attributes:
        id (int): The primary key of the record.
        accommodation_id (int): Foreign key referencing the 'accommodations'
                                table.
        amenities_id (int): Foreign key referencing the 'amenities' table.
        accommodation (Accommodation): The related accommodation object.
        amenity (Amenity): The related amenity object.

    Table:
        Name: 'accommodation_amenities'
        Columns:
            - id: Primary key, Integer, Not Null
            - accommodation_id: Foreign key to 'accommodations.id',
                                Integer, Not Null
            - amenities_id: Foreign key to 'amenities.id', Integer, Not Null

    Example:
        To assign an amenity to an accommodation:
        >>> assignment = AccommodationAmenity(
                accommodation_id=1,
                amenities_id=2
            )
        >>> session.add(assignment)
        >>> session.commit()

        To query accommodation amenities:
        >>> assignments = session.query(AccommodationAmenity)
                            .filter_by(accommodation_id=1).all()
        >>> for a in assignments:
        >>>     print(a)
        <AccommodationAmenity(id=1, accommodation_id=1, amenities_id=2)>
    """
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
