from sqlalchemy import Column, Integer, ForeignKey
from config import Base
from sqlalchemy.orm import relationship


class AccommodationRule(Base):
    """
    Represents the relationship between accommodations and rules in the system.

    Attributes:
        id (int): The primary key of the record.
        accommodation_id (int): A foreign key linking to the 'accommodations'
                                table.
        rule_id (int): A foreign key linking to the 'rules' table.
        accommodation (Accommodation): A relationship object representing the
                                        associated accommodation.
        rule (Rule): A relationship object representing the associated rule.

    Relationships:
        accommodation: Establishes a relationship with the `Accommodation`
                       model.
        rule: Establishes a relationship with the `Rule` model.

    Example:
        >>> accommodation_rule = AccommodationRule(
                accommodation_id=1,
                rule_id=2
            )
        >>> print(accommodation_rule)
        <AccommodationRule(id=1, accommodation_id=1, rule_id=2)>
    """
    __tablename__ = 'accommodations_rules'

    id = Column(Integer, primary_key=True)

    accommodation_id = Column(
        Integer,
        ForeignKey('accommodations.id'),
        nullable=False
    )
    rule_id = Column(
        Integer,
        ForeignKey('rules.id'),
        nullable=False
    )

    accommodation = relationship("Accommodation")
    rule = relationship("Rule")

    def __repr__(self):
        return (f"<AccommodationRule(id={self.id}, "
                f"accommodation_id={self.accommodation_id}, "
                f"rule_id={self.rule_id})>")
