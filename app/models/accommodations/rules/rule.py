from sqlalchemy import Column, Integer, String
from config import Base
from sqlalchemy.orm import relationship


class Rule(Base):
    """
    Represents a set of rules stored in the database.

    This class defines the schema for the 'rules' table,
    which contains unique textual descriptions of rules.

    Attributes:
        id (int): The primary key of the rule record.
        rule_text (str): The textual description of the rule, must be unique.

    Table:
        Name: 'rules'
        Columns:
            - id: Primary key, Integer, Not Null
            - rule_text: Text of the rule, String, Unique, Not Null

    Example:
        To create a new rule:
        >>> new_rule = Rule(rule_text='No smoking in the building')
        >>> session.add(new_rule)
        >>> session.commit()

        To query rules:
        >>> rules = session.query(Rule).all()
        >>> for rule in rules:
        >>>     print(rule)
        <Rule(id=1, rule_text='No smoking in the building')>
    """
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    rule_text = Column(String, unique=True, nullable=False)

    accommodation_rule = relationship(
        "AccommodationRule", back_populates='rule'
    )
    
    def __repr__(self) -> str:
        return f"<Rule(id={self.id}, rule_text='{self.rule_text}')>"
