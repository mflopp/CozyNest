from sqlalchemy import DECIMAL, Column, Integer, String, Date, ForeignKey
from models import Base
from sqlalchemy.orm import relationship

# -- Validation MUST be added


# Define Models
class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # -- payment_id ?????
    total_price = Column(DECIMAL(10, 2), nullable=False) # Ensures the total_price has two decimal points
    date_checkin = Column(Date, nullable=False)
    date_checkout = Column(Date, nullable=False)
    people_amount = Column(Integer, default=1)
    confirmation_code = Column(String)
    item = relationship("Items")
    user = relationship("Users")

    def __init__(self, **kwargs):
        from ..properties.Items_model import Items  # Local import within the class
        from ..users.Users_model import Users  # Local import within the class
        self.item = kwargs.get('item')
        self.user = kwargs.get('user')

