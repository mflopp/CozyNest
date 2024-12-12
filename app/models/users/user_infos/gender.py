from sqlalchemy import Column, Integer, String
from config import Base

from sqlalchemy.orm import relationship


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

    user_info = relationship("UserInfo", back_populates="gender")

    def __repr__(self):
        return (f"<Gender(id={self.id},"
                f" gender='{self.gender}',"
                f"description='{self.description}')>")
