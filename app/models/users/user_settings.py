from sqlalchemy import Column, Integer, String
from config import Base


class UserSettings(Base):
    """
    Represents the settings for a user in the system.

    Attributes:
        id (int): The unique identifier for the user settings.
        currency (str): The preferred currency of the user, default is 'USD'.
        language (str): The preferred language of the user, default is 'ENG'.
    """
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True)
    currency = Column(String, default='USD', nullable=False)
    language = Column(String, default='ENG', nullable=False)

    def __repr__(self):
        return (f"<UserSettings(id={self.id},"
                f"currency='{self.currency}',"
                f"language='{self.language}')>")
