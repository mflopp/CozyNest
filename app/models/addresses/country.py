from sqlalchemy import Column, Integer, String
from config import Base


class Country(Base):
    """
    Represents a country in the system.

    Attributes:
        id (int): The primary key of the country record.
        name (str): The name of the country, must be unique and not null.

    Example:
        >>> country = Country(name='Germany')
        >>> print(country)
        <Country(id=1, name='Germany')>
    """
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Country(id={self.id}, name='{self.name}')>"
