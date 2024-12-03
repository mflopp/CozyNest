# Users Module 📝

The **Users Module** is a Python package designed to manage users and their related information in a structured and efficient manner. It includes a comprehensive set of models for user data, roles, settings, and additional information. This module uses SQLAlchemy for seamless database interaction.

---

## Structure 📂

The module is organized as follows:

```bash
users/
|---- user_infos/
|     |---- __init__.py
|     |---- gender.py
|     |---- user_info.py
|     |---- user_role.py
|     |---- user_settings.py
|---- __init__.py
|---- user.py
```

---

## Components 🎯

### 1. `user_infos/`

A subpackage containing models for handling various aspects of user-related data. See the [User Infos Module](user_infos/README.md) for details.

### 2. `__init__.py`

This file initializes the **Users Module** by exposing all user-related models:

```python
# User related Models
from .user import User
from .user_infos import *

__all__ = [
    "User",
    *user_infos.__all__
]
```

### 3. `user.py`

Defines the **User** model:

-   **Attributes**:
    -   `id`: Unique identifier.
    -   `role_id`: Foreign key to the `user_roles` table.
    -   `info_id`: Foreign key to the `user_infos` table.
    -   `email`: User's unique email address.
    -   `password`: User's hashed password.
    -   `phone`: User's unique phone number.
    -   `created_at`: Timestamp for creation.
    -   `updated_at`: Timestamp for last modification.
-   **Relationships**:
    -   `role`: Links to `UserRole`.
    -   `info`: Links to `UserInfo`.
-   **Table**: `users`
-   **Example**:
    ```python
    <User(id=1, email='johndoe@example.com', phone='+1234567890', role_id=2, info_id=3)>
    ```

---

## Features ✨

1. **Database Integration**:

    - SQLAlchemy models ensure efficient interaction with relational databases.

2. **Modular Design**:

    - User-related information is organized into manageable components.

3. **Relationships**:
    - Models are linked using foreign keys and relationships to maintain data integrity.

---

## Usage 📦

1. **Import Models**:

    ```python
    from users import User, Gender, UserInfo, UserRole, UserSettings
    ```

2. **Perform Operations**:

    - Add a new user:

        ```python
        user = User(
            email='newuser@example.com',
            password='hashedpassword',
            phone='+1234567890',
            role_id=1,
            info_id=2
        )
        session.add(user)
        session.commit()
        ```

    - Query user details:
        ```python
        user = session.query(User).filter_by(email='johndoe@example.com').first()
        print(user)
        ```

---

## Conclusion 🚀

The **Users Module** provides a robust framework for managing user data and its related entities, making it a vital component for any application requiring user management functionality.
Its modularity, database integration, and structured design enable efficient and scalable solutions.
