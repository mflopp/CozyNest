from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy import CheckConstraint, Column, ForeignKey
from config import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Review(Base):
    """
    Represents a review left by a guest for a specific accommodation.

    Attributes:
        id (int): Primary key of the review.
        accommodation_id (int): Foreign key referencing the 'accommodations'
                                table.
        guest_id (int): Foreign key referencing the 'users' table (guests).
        rating (int): Rating provided by the guest (1 to 5).
        comment (str): Optional textual feedback from the guest.
        created_at (TIMESTAMP): Timestamp when the review was created.
        accommodation (Accommodation): Relationship object for
                                       the accommodation being reviewed.
        guest (User): Relationship object for the guest leaving the review.

    Constraints:
        - Rating must be between 1 and 5.

    Example:
        >>> review = Review(
            accommodation_id=1, guest_id=2,
            rating=5, comment="Amazing stay!"
            )
        >>> print(review)
        <Review(id=1, accommodation_id=1, guest_id=2,
        rating=5, comment='Amazing stay!')>
    """
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    rating = Column(
        Integer,
        CheckConstraint('rating >= 1 AND rating <= 5'),
        nullable=False
    )
    comment = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())

    accommodation = relationship("Accommodation", back_populates="review")
    user = relationship("User", back_populates="review")

    def __repr__(self):
        return (f"<Review(id={self.id},"
                f"accommodation_id={self.accommodation_id}, "
                f"guest_id={self.guest_id}, rating={self.rating}, "
                f"comment='{self.comment}', created_at={self.created_at})>")
