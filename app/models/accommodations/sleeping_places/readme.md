# Sleeping Places Directory 🛏️

This directory provides a structured way to manage sleeping places and their relationships with accommodations.
It includes models for sleeping places, the accommodations they belong to, and the connections between them.

## Directory Structure 📂

```plaintext
sleeping_places/
|---- accommodation_sleeping_place.py
|---- __init__.py
|---- sleeping_place.py
```

## Modules Overview 📝

### 1. `__init__.py`

Initializes the `sleeping_places` module and makes its key classes available for import.

**Exports**:

-   `SleepingPlace`
-   `AccommodationSleepingPlace`

**Example**:

```python
from sleeping_places import SleepingPlace, AccommodationSleepingPlace
```

### 2. `accommodation_sleeping_place.py`

Defines the `AccommodationSleepingPlace` class, which represents the relationship between accommodations and sleeping places.

**Features**:

-   Maps sleeping places to their respective accommodations.
-   Establishes relationships with the `Accommodation` and `SleepingPlace` models.

**Attributes**:

-   `id`: Primary key.
-   `sleeping_place_id`: Foreign key referencing the `sleeping_places` table.
-   `accommodation_id`: Foreign key referencing the `accommodations` table.

**Relationships**:

-   `sleeping_place`: Links to the `SleepingPlace` model.
-   `accommodation`: Links to the `Accommodation` model.

**Example**:

```python
accommodation_sleeping_place = AccommodationSleepingPlace(
    sleeping_place_id=1,
    accommodation_id=2
)
print(accommodation_sleeping_place)
# Output: <AccommodationSleepingPlace(id=1, sleeping_place_id=1, accommodation_id=2)>
```

### 3. `sleeping_place.py`

Defines the `SleepingPlace` class, representing sleeping arrangements such as beds or couches.

**Features**:

-   Stores the type and capacity of sleeping places.

**Attributes**:

-   `id`: Primary key.
-   `sleeping_place_type`: Type of the sleeping place (e.g., single bed, double couch).
-   `capacity`: Number of people the sleeping place can accommodate (1 or 2).

**Constraints**:

-   `capacity` must be between 1 and 2.

**Example**:

```python
sleeping_place = SleepingPlace(sleeping_place_type="Single Bed", capacity=2)
print(sleeping_place)
# Output: <SleepingPlace(id=1, sleeping_place_type='Single Bed', capacity=2)>
```

## How to Use This Module 🚀

1. **Import the Module**:
   Import the necessary classes:

    ```python
    from sleeping_places import SleepingPlace, AccommodationSleepingPlace
    ```

2. **Create a Sleeping Place**:

    ```python
    new_sleeping_place = SleepingPlace(sleeping_place_type="Queen Bed", capacity=2)
    session.add(new_sleeping_place)
    session.commit()
    ```

3. **Link a Sleeping Place to an Accommodation**:

    ```python
    accommodation_sleeping_place = AccommodationSleepingPlace(
        sleeping_place_id=1,
        accommodation_id=2
    )
    session.add(accommodation_sleeping_place)
    session.commit()
    ```

4. **Query Sleeping Places**:
    ```python
    sleeping_places = session.query(SleepingPlace).all()
    for place in sleeping_places:
        print(place)
    ```

## Dependencies 📦

-   SQLAlchemy
-   `config.Base`: The base declarative class for defining the schema.

## Conclusion 🎯

The `sleeping_places` module simplifies the management of sleeping arrangements and their relationships with accommodations.
It provides an efficient and organized approach to handling sleeping places in your system.
