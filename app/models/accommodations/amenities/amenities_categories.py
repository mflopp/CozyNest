from sqlalchemy import Column, Integer, String
from config import Base


class AmenitiesCategory(Base):
    """
    Represents a category for amenities in the database.

    This class defines the schema for the 'amenity_categories' table,
    which stores unique categories of amenities, such as:
        'Pool', 'Gym', or 'Wi-Fi'.
    Each category is identified by a unique ID and a unique name.

    Attributes:
        id (int): The primary key of the category.
                  Automatically generated.
        category (str): The name of the amenity category.
                        Must be unique and cannot be null.

    Example:
        To create a new category:
        >>> new_category = AmenityCategory(category='Pool')
        >>> session.add(new_category)
        >>> session.commit()

        To query a category:
        >>> category = session.query(AmenityCategory)
                       .filter_by(category='Gym').first()
        >>> print(category)
        <AmenityCategory(id=2, category='Gym')>
    """
    __tablename__ = 'amenities_categories'

    id = Column(Integer, primary_key=True)
    category = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return (f"<AmenitiesCategory(id={self.id},"
                f" category='{self.category}')>")
