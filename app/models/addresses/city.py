from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a city within a region.

    Attributes:
        id (int): The primary key of the city record.
        region_id (int): A foreign key linking to the 'regions' table.
        name (str): The name of the city.
        region (Region): A relationship object representing
                         the associated region.

    Relationships:
        region: Establishes a relationship with the `Region` model.

    Example:
        >>> city = City(name='Munich', region_id=1)
        >>> print(city)
        <City(id=1, name='Munich', region_id=1)>
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    name = Column(String, nullable=False)

    region = relationship("Region")

    def __repr__(self):
        return (f"<City(id={self.id}, name='{self.name}', "
                f"region_id={self.region_id})>")
