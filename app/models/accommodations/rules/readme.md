# Rules Directory 🛡️

This directory contains modules for managing rules and their relationships with accommodations in a database.
It defines the schema and logic for handling rules and their associations.

## Directory Structure 📂

```plaintext
    rules/
    |---- __init__.py
    |---- accommodation_rule.py
    |---- rule.py
```

## Modules Overview 📝

### 1. `__init__.py`

This file initializes the `rules` module, making its classes (`Rule` and `AccommodationRule`) available for import.

**Exports**:

-   `Rule`
-   `AccommodationRule`

---

### 2. `accommodation_rule.py`

Defines the `AccommodationRule` class, which represents the relationship between accommodations and rules.

**Features**:

-   Links accommodations to their respective rules.
-   Establishes relationships with the `Accommodation` and `Rule` models.

**Attributes**:

-   `id`: Primary key.
-   `accommodation_id`: Foreign key referencing the `accommodations` table.
-   `rule_id`: Foreign key referencing the `rules` table.

**Relationships**:

-   `accommodation`: Links to the `Accommodation` model.
-   `rule`: Links to the `Rule` model.

**Example**:

```python
accommodation_rule = AccommodationRule(accommodation_id=1, rule_id=2)
print(accommodation_rule)
# Output: <AccommodationRule(id=1, accommodation_id=1, rule_id=2)>
```

### 3. `rule.py`

Defines the `Rule` class, which represents a set of rules stored in the database.

**Features**:

-   Stores unique textual descriptions of rules.

**Attributes**:

-   `id`: Primary key.
-   `rule_text`: Unique text describing the rule.

**Example**:

```python
new_rule = Rule(rule_text='No smoking in the building')
print(new_rule)
# Output: <Rule(id=1, rule_text='No smoking in the building')>
```

## How to Use This Module 🚀

1. **Import the Module**:
   Import the necessary classes from the `rules` package:

    ```python
    from rules import Rule, AccommodationRule
    ```

2. **Create a New Rule**:

    ```python
    new_rule = Rule(rule_text="No loud music after 10 PM")
    session.add(new_rule)
    session.commit()
    ```

3. **Assign a Rule to an Accommodation**:

    ```python
    accommodation_rule = AccommodationRule(accommodation_id=1, rule_id=2)
    session.add(accommodation_rule)
    session.commit()
    ```

4. **Query Rules**:
    ```python
    rules = session.query(Rule).all()
    for rule in rules:
        print(rule)
    ```

## Dependencies 📦

-   SQLAlchemy
-   `config.Base`: The base declarative class for defining the schema.

## Conclusion 🎯

The `rules` module provides a structured and scalable way to manage rules and their relationships with accommodations.
Use these classes to maintain and query rule-related data efficiently.
