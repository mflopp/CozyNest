from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class Region(Base):
    """
    Represents a region within a country.

    Attributes:
        id (int): The primary key of the region record.
        country_id (int): A foreign key linking to the 'countries' table.
        name (str): The name of the region.
        country (Country): A relationship object representing
                           the associated country.

    Relationships:
        country: Establishes a relationship with the `Country` model.

    Example:
        >>> region = Region(name='Bavaria', country_id=1)
        >>> print(region)
        <Region(id=1, name='Bavaria', country_id=1)>
    """
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    name = Column(String, nullable=False)

    country = relationship("Country")

    def __repr__(self):
        return (f"<Region(id={self.id}, name='{self.name}', "
                f"country_id={self.country_id})>")
