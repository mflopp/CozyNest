from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config import Base


class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        role_id (int): Foreign key referencing the UserRoles table.
        info_id (int): Foreign key referencing the UserInfos table.
        email (str): User's unique email address.
        password (str): User's hashed password.
        phone (str): User's unique phone number.
        created_at (TIMESTAMP): Timestamp of when the record was created.
        updated_at (TIMESTAMP): Timestamp of the last update to the record.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('user_roles.id'), nullable=False)
    info_id = Column(Integer, ForeignKey('user_infos.id'), nullable=False)

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    role = relationship("UserRole")
    info = relationship("UserInfo")

    def __repr__(self):
        return (
            f"<User(id={self.id},"
            f"email='{self.email}',"
            f"phone='{self.phone}', "
            f"role_id={self.role_id},"
            f"info_id={self.info_id})>"
        )
