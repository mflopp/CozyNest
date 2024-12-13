from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from config import Base
from sqlalchemy.sql import func


class UserInfo(Base):
    """
    Represents user information in the system.

    Attributes:
        id (int): The unique identifier for the user info.
        gender_id (int): The ID of the user's gender, referencing
                         the Genders table.
        user_settings_id (int): The ID of the user's settings,
                                referencing the UserSettings table.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        birthdate (date, optional): The user's birthdate.
        created_at (timestamp): The timestamp of when the record was created.
        updated_at (timestamp): The timestamp of the last update to the record.
        gender (Genders): The gender object related to the user.
        settings (UserSettings): The settings object related to the user.
    """
    __tablename__ = 'user_infos'

    id = Column(
        Integer,
        primary_key=True
    )

    gender_id = Column(
        Integer,
        ForeignKey('genders.id'),
        nullable=False
    )

    user_settings_id = Column(
        Integer,
        ForeignKey('user_settings.id'),
        nullable=False
    )

    first_name = Column(
        String,
        nullable=False
    )

    last_name = Column(
        String,
        nullable=False
    )

    birthdate = Column(Date)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        onupdate=func.now()
    )

    gender = relationship("Gender", back_populates="user_info")
    settings = relationship("UserSettings", back_populates="user_info")
    user = relationship("User", back_populates="user_info")

    def __repr__(self):
        return (
            f"<UserInfo(id={self.id},"
            f"first_name='{self.first_name}',"
            f"last_name='{self.last_name}',"
            f"gender_id={self.gender_id},"
            f"user_settings_id={self.user_settings_id},"
            f"birthdate={self.birthdate})>"
        )
