from sqlalchemy import Column, Integer, String
from config import Base


class UserRole(Base):
    """
    Represents a user role in the system.

    Attributes:
        id (int): The primary key of the user role.
        role (str): The unique name of the role.
        description (str, optional): A description of the role.
    """
    __tablename__ = 'userroles'

    id = Column(Integer, primary_key=True)
    role = Column(String, unique=True, nullable=False)
    description = Column(String)

    def __repr__(self):
        return (f"<UserRole(id={self.id},"
                f"role='{self.role}',"
                f"description='{self.description}')>")
