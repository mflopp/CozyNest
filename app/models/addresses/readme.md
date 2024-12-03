# Addresses Module 📍

The `addresses` module is designed to provide a structured approach to managing geographical and address-related data.
This module includes models for **countries**, **regions**, **cities**, and **addresses**, all connected in a logical hierarchy.

## Purpose 🎯

The module's main goal is to provide a scalable, extensible, and maintainable solution for handling location-based data in applications, particularly those that involve hierarchical geographical relationships.

## Structure 📂

The module consists of the following files:

-   **`__init__.py`**: Initializes the module and defines the exports.
-   **`address.py`**: Defines the `Address` model.
-   **`city.py`**: Defines the `City` model.
-   **`region.py`**: Defines the `Region` model.
-   **`country.py`**: Defines the `Country` model.

### Relationships 🔗

1. **Country** → **Region** → **City** → **Address**  
   Each entity is linked to the next to form a complete address system.

## Models 🔍

### 1. Address 🏠

-   Represents the full address details, including street, building, apartment, and geographical coordinates.
-   **Relationships**: Connected to a `City`.

### 2. City 🌆

-   Represents a city within a region.
-   **Relationships**: Connected to a `Region`.

### 3. Region 🌍

-   Represents a region within a country.
-   **Relationships**: Connected to a `Country`.

### 4. Country

-   Represents a country. Each country has a unique name.

## Usage 📦

1. **Initialize the Models**:
   Import the module and utilize its components for geographical data handling:

    ```python
    from addresses import Country, Region, City, Address
    ```

2. **Create an Address**:

    ```python
    from addresses import Address

    new_address = Address(
        city_id=1,
        street='Main Street',
        building='123',
        apartment='4A',
        zip_code='12345',
        latitude=40.7128,
        longitude=-74.0060
    )
    print(new_address)
    ```

3. **Set Up Database Relationships**:
   Ensure all models are linked correctly through foreign keys.

## Example 🌟

### Adding a New Address

```python
from addresses import Country, Region, City, Address

# Define a country
germany = Country(name='Germany')

# Define a region
bavaria = Region(name='Bavaria', country_id=germany.id)

# Define a city
munich = City(name='Munich', region_id=bavaria.id)

# Define an address
address = Address(
    city_id=munich.id,
    street='Maximilianstraße',
    building='10',
    zip_code='80539',
    latitude=48.1391,
    longitude=11.5802
)

print(address)
```

## Conclusion 🚀

The `addresses` module provides a robust foundation for managing geographical data in a structured manner.
It ensures easy extensibility, scalability, and integration into various applications.
