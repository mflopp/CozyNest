from sqlalchemy import Float, Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class Address(Base):
    """
    Represents the address details of an entity, including its geographical
    location.

    Attributes:
        id (int): The primary key of the address record.
        city_id (int): A foreign key linking to the 'cities' table.
        street (str): The name of the street.
        building (str): The building number or identifier.
        apartment (str, optional): The apartment number.
        zip_code (str): The postal code of the address.
        latitude (float): The latitude of the address location.
        longitude (float): The longitude of the address location.
        city (City): A relationship object representing the associated city.

    Relationships:
        city: Establishes a relationship with the `City` model.

    Example:
        >>> address = Address(
        ...     city_id=1,
        ...     street='Main Street',
        ...     building='123',
        ...     apartment='4A',
        ...     zip_code='12345',
        ...     latitude=40.7128,
        ...     longitude=-74.0060
        ... )
        >>> print(address)
        <Address(id=1, street='Main Street', building='123', zip_code='12345')>
    """
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    street = Column(String, nullable=False)
    building = Column(String, nullable=False)
    apartment = Column(String)
    zip_code = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    city = relationship("City")

    def __repr__(self):
        return (f"<Address(id={self.id}, street='{self.street}', "
                f"building='{self.building}', zip_code='{self.zip_code}')>")
