from sqlalchemy import Float, Column, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    street = Column(String, nullable=False)
    building = Column(String, nullable=False)
    apartment = Column(String)
    zip_code = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    city = relationship("City", back_populates='addresses')
    accommodation = relationship("Accommodation", back_populates='addresses')

    def __repr__(self):
        return (f"<Address(id={self.id}, street='{self.street}', "
                f"building='{self.building}', zip_code='{self.zip_code}')>")
