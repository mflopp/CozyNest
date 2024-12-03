# accommodation_infos Directory 📂

## Description 📝

This directory contains models related to accommodations, including images, types, and availability, using SQLAlchemy and a relational database schema.
These models allow easy handling and querying of accommodation-related data, such as accommodation images, types, and availability periods.

## Purpose 🎯

The purpose of this directory is to manage accommodation-related data in a structured and efficient manner.
It defines the following models:

1. **AccommodationImage**: Represents an image associated with an accommodation.
2. **AccommodationType**: Represents different types of accommodations (e.g., Apartment, Villa, House).
3. **AccommodationAvailability**: Represents the availability details of an accommodation for a specific period.

These models allow for seamless interaction with the database, enabling CRUD (Create, Read, Update, Delete) operations for accommodation information.

## Structure 📂

The directory contains the following files:

-   **`__init__.py`**: This file imports and exposes the models for use elsewhere in the project.
-   **`accommodation_image.py`**: Contains the `AccommodationImage` model, which stores image data for accommodations.
-   **`accommodation_type.py`**: Defines the `AccommodationType` model, which stores different accommodation types.
-   **`accommodation_availability.py`**: Defines the `AccommodationAvailability` model, which stores availability information for accommodations.

## How It Works 🔍

### Models:

1. **AccommodationImage** (`accommodation_image.py`):

    - Represents an image associated with an accommodation.
    - Has a foreign key to the `accommodations` table and a `src` field for the image URL or path.
    - Establishes a relationship with the `Accommodation` model.

2. **AccommodationType** (`accommodation_type.py`):

    - Represents the type of accommodation (e.g., Apartment, House).
    - Each accommodation type is unique and stored in the `accommodation_types` table.

3. **AccommodationAvailability** (`accommodation_availability.py`):
    - Represents the availability of an accommodation for a specific period, including check-in and check-out times.
    - Links to the `accommodations` table and defines availability start and end dates.

### Relationship between Models:

-   **AccommodationImage** and **AccommodationAvailability** are linked to the `Accommodation` model, allowing for easy queries across related tables.

## Output 📜

The models interact with a database, and querying them would produce data such as:

-   **AccommodationImage**:
    ```python
    <AccommodationImage(id=1, accommodation_id=1, src='path/to/image.jpg')>
    ```
-   **AccommodationType**:

    ```python
    <AccommodationType(id=1, accommodation_type='Apartment')>
    ```

-   **AccommodationAvailability**:
    ```python
    <AccommodationAvailability(id=1, accommodation_id=1, date_available_from='2024-12-01', date_available_to='2024-12-31', time_checkin='14:00', time_checkout='11:00')>
    ```

## Usage 📦

1. Import the necessary models in your code:
    ```python
    from accommodation_infos import AccommodationImage, AccommodationType, AccommodationAvailability
    ```
2. Create an instance of any model and add it to the database:

    ```python
    accommodation_image = AccommodationImage(accommodation_id=1, src="path/to/image.jpg")
    session.add(accommodation_image)
    session.commit()

    accommodation_type = AccommodationType(accommodation_type="Villa")
    session.add(accommodation_type)
    session.commit()

    availability = AccommodationAvailability(
        accommodation_id=1,
        date_available_from="2024-12-01",
        date_available_to="2024-12-31",
        time_checkin="14:00",
        time_checkout="11:00"
    )
    session.add(availability)
    session.commit()
    ```

## Conclusion 🚀

The `accommodation_infos` directory provides well-structured models for handling accommodation-related data.
By using SQLAlchemy's ORM, these models allow to easily create, query, and manage data for accommodation images, types, and availability.
Integrating these models into application helps streamline the handling of accommodation information for any related system.
