from sqlalchemy import Column, Integer, String
from config import Base


class Gender(Base):
    """
    Represents a gender in the system.

    Attributes:
        id (int): The unique identifier for the gender.
        gender (str): The name of the gender.
        description (str, optional): A description of the gender.
    """
    __tablename__ = 'genders'

    id = Column(Integer, primary_key=True)
    gender = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return (f"<Gender(id={self.id},"
                f" gender='{self.gender}',"
                f"description='{self.description}')>")
