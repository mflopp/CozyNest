# README.md 📚

## Overview 📝

The `accommodations` directory contains structured submodules for managing various aspects of accommodations in a relational database.
This setup uses SQLAlchemy to handle data for accommodations, their amenities, rules, sleeping places, and associated information such as availability, images, and types.

## Purpose 🎯

The purpose of this directory is to provide modularized components for handling all aspects of accommodations efficiently.
Each subdirectory contains models that represent specific features of accommodations, ensuring scalability and reusability across different parts of the project.

## Directory Structure 📂

```plaintext
accommodations/
|---- accommodation_infos/
|---- amenities/
|---- rules/
|---- sleeping_places/
|---- __init__.py
|---- accommodation.py
```

### Subdirectories and Files:

1. **`accommodation_infos/`**

    - Contains models for accommodation-related details such as images, types, and availability periods.
    - Models: `AccommodationImage`, `AccommodationType`, `AccommodationAvailability`.

2. **`amenities/`**

    - Manages data related to amenities offered in accommodations.
    - Models: `AmenityCategory`, `Amenity`, `AccommodationAmenity`.

3. **`rules/`**

    - Defines rules and their associations with accommodations.
    - Models: `Rule`, `AccommodationRule`.

4. **`sleeping_places/`**

    - Handles sleeping place details, types, and their links to accommodations.
    - Models: `SleepingPlace`, `AccommodationSleepingPlace`.

5. **`accommodation.py`**

    - Defines the core `Accommodation` model, which other modules reference.
    - Represents general information about accommodations such as name, description, and location.

6. **`__init__.py`**
    - Imports and exposes all submodules and models for seamless integration.

## How It Works 🔍

The directory is organized into submodules that correspond to specific features of accommodations.
Each submodule contains models that define the database schema and relationships using SQLAlchemy.

### Key Relationships:

1. **Accommodation**:

    - Central model connecting to `AccommodationImage`, `AccommodationType`, `AccommodationAvailability`, `AccommodationAmenity`, and `AccommodationSleepingPlace`.

2. **Submodules**:
    - Models in `accommodation_infos/` provide detailed information for accommodations.
    - `amenities/` models define the features available in accommodations.
    - `rules/` models manage the rules governing accommodations.
    - `sleeping_places/` models organize sleeping arrangements in accommodations.

## Usage 📦

### 1. Import Necessary Models:

```python
from accommodations import (
    Accommodation,
    AccommodationImage,
    AccommodationType,
    AccommodationAvailability,
    AmenityCategory,
    Amenity,
    AccommodationAmenity,
    Rule,
    AccommodationRule,
    SleepingPlace,
    AccommodationSleepingPlace
)
```

### 2. Create and Query Data:

-   Add a new accommodation:

    ```python
    new_accommodation = Accommodation(name="Cozy Cottage", description="A quiet retreat in the woods.")
    session.add(new_accommodation)
    session.commit()
    ```

-   Add an image to the accommodation:

    ```python
    image = AccommodationImage(accommodation_id=1, src="path/to/image.jpg")
    session.add(image)
    session.commit()
    ```

-   Assign a rule to an accommodation:

    ```python
    rule = AccommodationRule(accommodation_id=1, rule_id=2)
    session.add(rule)
    session.commit()
    ```

-   Add an amenity:

    ```python
    amenity = Amenity(name="Wi-Fi", category_id=1)
    session.add(amenity)
    session.commit()
    ```

-   Link sleeping places:
    ```python
    sleeping_place = AccommodationSleepingPlace(accommodation_id=1, sleeping_place_id=3)
    session.add(sleeping_place)
    session.commit()
    ```

## Dependencies 📦

-   **SQLAlchemy**: For ORM-based database interactions.
-   **config.Base**: Declarative base class for all models.
-   **Relational Database**: Supports PostgreSQL, MySQL, SQLite, etc.

## Conclusion 🚀

The `accommodations` directory offers a comprehensive structure for managing accommodation data and related features.
Its modular design ensures that each aspect, from images and amenities to rules and sleeping places, is handled efficiently and independently.
This structure supports seamless integration with larger systems, making it a robust solution for managing accommodation-related data.
