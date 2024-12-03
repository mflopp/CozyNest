from sqlalchemy import DECIMAL, Integer, String, Date
from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from config import Base


class Order(Base):
    """
    Represents an order in the booking system.
    This model defines an order placed by a guest for a specific accomodation.

    Attributes:
        id (int): The primary key of the record.

        accomodation_id (int): Foreign key referencing the 'accomodations'
                               table.
        guest_id (int): Foreign key referencing the 'users' table (guests).

        total_price (DECIMAL): The total price of the order.
        date_checkin (Date): The check-in date for the order.
        date_checkout (Date): The check-out date for the order.
        people_amount (int): The number of people included in the order.
        confirmation_code (str): A unique code for order confirmation.

        accomodation (Accomodation): A relationship object representing
                                     the associated accomodation.
        guest (User): A relationship object representing the guest who
        placed the order.

    Constraints:
        - people_amount must be greater than 0.

    Example:
        >>> order = Order(
            item_id=1, guest_id=2,
            total_price=100.00, date_checkin="2023-01-01",
            date_checkout="2023-01-10", people_amount=2,
            confirmation_code="ABC123"
            )
        >>> print(order)
        <Order(id=1, item_id=1, guest_id=2, total_price=100.00,
        dates=(2023-01-01 to 2023-01-10), people=2)>
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )

    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    total_price: Column[DECIMAL] = Column(DECIMAL(10, 2), nullable=False)
    date_checkin = Column(Date, nullable=False)
    date_checkout = Column(Date, nullable=False)
    people_amount = Column(
        Integer,
        CheckConstraint('people_amount > 0'),
        default=1
    )
    confirmation_code = Column(String(50))

    accommodation = relationship("Accommodation")
    guest = relationship("User")

    def __repr__(self):
        return (f"<Order(id={self.id},"
                f"accommodation_id={self.accommodation_id},"
                f"guest_id={self.guest_id}, "
                f"total_price={self.total_price}, "
                f"dates=({self.date_checkin} to {self.date_checkout}), "
                f"people={self.people_amount})>")
