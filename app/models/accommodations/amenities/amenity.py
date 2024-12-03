from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class Amenity(Base):
    """
    Represents an individual amenity in the database.

    This class defines the schema for the 'amenities' table,
    which stores information about specific amenities, such as:
        'Swimming Pool', 'Gym', or 'Parking'.
    Each amenity is linked to a category via a foreign key.

    Attributes:
        id (int): The primary key of the amenity. Automatically generated.
        category_id (int): The foreign key linking to the category
                            of the amenity.
        name (str): The name of the amenity. Cannot be null.
        category (AmenityCategory): The category object associated with
                                    this amenity.

    Table:
        Name: 'amenities'
        Columns:
            - id: Primary key, Integer, Not Null
            - category_id: Foreign key to 'amenity_categories.id',
                           Integer, Not Null
            - name: Name of the amenity, String, Not Null
            - category: Relationship to AmenityCategory

    Example:
        To create a new amenity:
        >>> new_amenity = Amenity(category_id=1, name='Swimming Pool')
        >>> session.add(new_amenity)
        >>> session.commit()

        To query an amenity:
        >>> amenity = session.query(Amenity).filter_by(name='Gym').first()
        >>> print(amenity)
        <Amenity(id=2, name='Gym', category_id=1)>
    """
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey('amenities_categories.id'),
        nullable=False
    )

    name = Column(String, nullable=False)
    category = relationship("AmenitiesCategory")

    def __repr__(self) -> str:
        return (f"<Amenity(id={self.id}, name={repr(self.name)}, "
                f"category_id={self.category_id})>")
