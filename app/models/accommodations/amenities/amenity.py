from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey('amenities_categories.id'),
        nullable=False
    )

    name = Column(String, nullable=False)
    category = relationship("AmenitiesCategory")

    def __repr__(self) -> str:
        return (f"<Amenity(id={self.id}, name={repr(self.name)}, "
                f"category_id={self.category_id})>")
