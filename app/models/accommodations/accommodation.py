from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey, TIMESTAMP
from config import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Accommodation(Base):
    """
    Represents an accommodation entity in the system.

    Attributes:
        id (int): The primary key of the accommodation record.
        accommodation_type_id (int): A foreign key linking to
                                     the 'accommodation_types' table.
        owner_id (int): A foreign key linking to the 'users' table (owner of
                        the accommodation).
        address_id (int): A foreign key linking to the 'addresses' table.
        description (str): A description of the accommodation.
        rooms_number (int): The number of rooms in the accommodation.
                            Defaults to 1.
        max_capacity (int): The maximum capacity of people the accommodation
                            can hold. Defaults to 1.
        price (Decimal): The price per accommodation, with two decimal points
                         precision.
        status (str): The status of the accommodation (e.g., 'active').
                      Defaults to 'active'.
        created_at (TIMESTAMP): The timestamp when the accommodation
                                was created.
        updated_at (TIMESTAMP): The timestamp when the accommodation was last
                                updated.
        accommodation_type (AccommodationType): A relationship object
                                                representing the associated
                                                accommodation type.
        owner (User): A relationship object representing the associated owner.
        address (Address): A relationship object representing
                           the accommodation's address.

    Relationships:
        accommodation_type: Establishes a relationship with
                            the `AccommodationType` model.
        owner: Establishes a relationship with the `User` model.
        address: Establishes a relationship with the `Address` model.

    Example:
        >>> accommodation = Accommodation(
            description='Cozy apartment', price=100.00, rooms_number=2
            )
        >>> print(accommodation)
        <Accommodation(id=1, description='Cozy apartment',
        price=100.00, rooms_number=2)>
    """
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True)

    accommodation_type_id = Column(
        Integer,
        ForeignKey('accommodation_types.id'),
        nullable=False
    )
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)

    description = Column(String)
    rooms_number = Column(Integer, default=1)
    max_capacity = Column(Integer, default=1)
    price = Column(DECIMAL(10, 2), nullable=False)  # type: ignore
    status = Column(String, default="active")
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    accommodation_type = relationship("AccommodationType")
    owner = relationship("User")
    address = relationship("Address")

    def __repr__(self):
        return (f"<Accommodation(id={self.id}, "
                f"description='{self.description}', "
                f"price={self.price}, "
                f"rooms_number={self.rooms_number}, "
                f"max_capacity={self.max_capacity}, "
                f"status='{self.status}')>")
