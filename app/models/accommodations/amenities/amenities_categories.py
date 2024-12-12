from sqlalchemy import Column, Integer, String
from config import Base


class AmenitiesCategory(Base):

    __tablename__ = 'amenities_categories'

    id = Column(Integer, primary_key=True)
    category = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return (f"<AmenitiesCategory(id={self.id},"
                f" category='{self.category}')>")
