from sqlalchemy import CheckConstraint, Column, Integer, String, Date, ForeignKey, Enum, TIMESTAMP
from models import Base
from sqlalchemy.orm import relationship

# -- Validation MUST be added


# Define Models
class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False) # Ensuring rating is between 1 and 5
    comment = Column(String)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    item = relationship("Items")
    user = relationship("Users")

    def __init__(self, **kwargs):
        from ..properties.Items_model import Items  # Local import within the class
        from ..users.Users_model import Users  # Local import within the class
        self.item = kwargs.get('item')
        self.user = kwargs.get('user')
