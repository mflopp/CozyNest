# amenities Directory 📂

## Description 📝

The `amenities` directory contains the models related to amenities, including categories, individual amenities, and their associations with accommodations.
These models are defined using SQLAlchemy and provide a structured way to store and interact with data related to amenities, such as swimming pools, gyms, and other features available in accommodations.

The directory includes:

1. **AmenityCategory**: Represents categories for amenities (e.g., Laundry, Kitchen).
2. **Amenity**: Represents specific amenities within each category (e.g., Washing Maschine, Stove).
3. **AccommodationAmenity**: Represents the assignment of an amenity to a specific accommodation.

## Purpose 🎯

The purpose of the `amenities` directory is to manage and organize data related to amenities offered in accommodations.
The directory contains models that enable:

1. Categorization of amenities (e.g., Laundry, Kitchen).
2. Detailed information about specific amenities (e.g., Washing Maschine, Stove).
3. Association between accommodations and their available amenities.

These models allow seamless data interaction, including adding, querying, and managing amenities and their categories in an accommodation database.

## Structure 📂

The directory contains the following files:

-   **`__init__.py`**: This file imports and exposes the necessary models for use elsewhere in the project.
-   **`accommodation_amenity.py`**: Defines the `AccommodationAmenity` model that links accommodations and amenities.
-   **`amenities_categories.py`**: Contains the `AmenitiesCategory` model that defines various categories of amenities.
-   **`amenity.py`**: Defines the `Amenity` model for specific amenities that belong to a category.

## How It Works 🔍

### Models:

1. **AccommodationAmenity** (`accommodation_amenity.py`):

    - Represents the link between accommodations and amenities.
    - Contains foreign keys to the `accommodations` and `amenities` tables.
    - Establishes relationships with the `Accommodation` and `Amenity` models.

2. **AmenityCategory** (`amenities_categories.py`):

    - Represents categories of amenities (e.g., Laundry, Kitchen).
    - Each category is unique and stored in the `amenities_categories` table.

3. **Amenity** (`amenity.py`):
    - Represents specific amenities (e.g., Washing Maschine, Stove).
    - Each amenity belongs to a specific `AmenityCategory`.

### Relationships:

-   **AccommodationAmenity** links an accommodation to an amenity.
-   **Amenity** is linked to **AmenityCategory**, organizing amenities into categories.

## Output 📜

The models interact with the database and querying them would produce data such as:

-   **AccommodationAmenity**:

    ```python
    <AccommodationAmenity(id=1, accommodation_id=1, amenities_id=2)>
    ```

-   **AmenityCategory**:

    ```python
    <AmenityCategory(id=1, category='Kitchen')>
    ```

-   **Amenity**:

    ```python
    <Amenity(id=1, name='Stove', category_id=1)>
    ```

## Usage 📦

1. **Import the necessary models in your code**:
    ```python
    from amenities import AmenityCategory, Amenity, AccommodationAmenity
    ```
2. **Create a new category**:
    ```python
    new_category = AmenityCategory(category='Kitchen')
    session.add(new_category)
    session.commit()
    ```
3. **Create a new amenity**:
    ```python
    new_amenity = Amenity(category_id=1, name='Stove')
    session.add(new_amenity)
    session.commit()
    ```
4. **Assign an amenity to an accommodation**:

    ```python
    assignment = AccommodationAmenity(accommodation_id=1, amenities_id=1)
    session.add(assignment)
    session.commit()
    ```

5. **Query amenities assigned to an accommodation**:

    ```python
    assignments = session.query(AccommodationAmenity).filter_by(accommodation_id=1).all()
    for a in assignments:
        print(a)
    ```

## Conclusion 🚀

The `amenities` directory provides a clear and organized structure for managing amenities and their categories.
Using SQLAlchemy, it allows to easily assign amenities to accommodations, manage different types of amenities, and categorize them efficiently.
This setup ensures scalability and flexibility for dealing with various accommodation features, improving the overall management and accessibility of amenities data.
