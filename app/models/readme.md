# Models Directory 📦

The `models` directory is the central hub for all data models used in the application.
It defines the structure, relationships, and interactions for various entities such as accommodations, addresses, orders, reviews, and users.

## Purpose 🎯

The purpose of this directory is to organize and manage the data models efficiently, ensuring scalability, modularity, and reusability across the application.
Each submodule handles a specific domain of the system.

## Directory Structure 📂

```plaintext
models/
|---- accommodations/
|---- addresses/
|---- orders/
|---- reviews/
|---- users/
|---- __init__.py
```

### Subdirectories and Their Roles:

1. **`accommodations/`**  
   Manages data related to accommodations, including types, amenities, rules, sleeping arrangements, and availability.

2. **`addresses/`**  
   Handles geographical data, such as countries, regions, cities, and specific address details.

3. **`orders/`**  
   Manages booking orders, including guest details, pricing, and booking durations.

4. **`reviews/`**  
   Tracks guest reviews, including ratings, comments, and timestamps.

5. **`users/`**  
   Handles user-related information, such as profiles, roles, and settings.

6. **`__init__.py`**  
   Initializes the `models` package and exposes all submodules for easy import.

## Modules Overview 📝

### 1. Accommodations

See the [Accommodations README](accommodations/README.md) for a detailed breakdown of the `accommodations/` submodule.

### 2. Addresses

The [Addresses README](addresses/README.md) provides a complete guide to the `addresses/` submodule.

### 3. Orders

Refer to the [Orders README](orders/README.md) for details on the `orders/` submodule.

### 4. Reviews

Explore the [Reviews README](reviews/README.md) for an overview of the `reviews/` submodule.

### 5. Users

The [Users README](users/README.md) contains a comprehensive guide to the `users/` submodule.

## How It Works 🔍

Each submodule contains SQLAlchemy ORM models that define the database schema and relationships. The `models/` directory serves as the backbone of the application by ensuring data consistency and efficient interactions.

### Key Features:

-   **Modularity**: Each submodule is self-contained and focuses on a specific domain.
-   **Scalability**: Easily extendable to support additional features.
-   **Reusability**: Models can be reused across different parts of the application.

## Usage 📦

1. **Import Models**:
   Import models from any submodule:

    ```python
    from models import accommodations, addresses, orders, reviews, users
    ```

2. **Access Specific Models**:

    ```python
    from models.accommodations import Accommodation
    from models.orders import Order
    ```

3. **Database Operations**:
    - Create new entries.
    - Query relationships and linked data.
    - Use SQLAlchemy sessions for transactions.

## Example Usage 🌟

### Adding a New Accommodation

```python
from models.accommodations import Accommodation

new_accommodation = Accommodation(name="Ocean View Suite", description="A luxurious suite overlooking the ocean.")
session.add(new_accommodation)
session.commit()
```

### Creating an Order

```python
from models.orders import Order

new_order = Order(
    accommodation_id=1,
    guest_id=2,
    total_price=300.00,
    date_checkin="2024-01-01",
    date_checkout="2024-01-05"
)
session.add(new_order)
session.commit()
```

## Dependencies 📦

-   **SQLAlchemy**: For ORM-based database interactions.
-   **config.Base**: Base declarative class for all models.
-   **Database Support**: Compatible with PostgreSQL, MySQL, SQLite, and more.

## Conclusion 🚀

The `models` directory is the foundation of the application, providing a robust and organized structure for managing data.
Its modular design ensures scalability and maintainability, making it a reliable backbone for the system.
