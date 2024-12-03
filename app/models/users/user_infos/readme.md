# User Infos Module 📝

The **User Infos Module** is a Python package designed to handle various aspects of user information in a system. It includes classes for managing genders, user information, user roles, and user settings, utilizing SQLAlchemy for database interaction.

---

## Description 🎯

This module provides a structured approach to representing and managing user-related data, including:

-   **Gender**: Represents gender details with optional descriptions.
-   **User Information**: Handles user-specific details such as name, birthdate, and gender.
-   **User Role**: Defines user roles with customizable descriptions.
-   **User Settings**: Manages user preferences like language and currency.

Each class corresponds to a database table, facilitating efficient CRUD operations.

---

## Components 📂

### 1. `__init__.py`

Serves as the package initializer, exporting all classes:

```python
from .gender import Gender
from .user_info import UserInfo
from .user_role import UserRole
from .user_settings import UserSettings

__all__ = ['Gender', 'UserInfo', 'UserRole', 'UserSettings']
```

---

### 2. `gender.py`

Defines the **Gender** model:

-   **Attributes**:
    -   `id`: Unique identifier.
    -   `gender`: Name of the gender.
    -   `description`: Optional description.
-   **Table**: `genders`
-   **Example**:
    ```python
    <Gender(id=1, gender='Male', description='A male gender representation')>
    ```

---

### 3. `user_info.py`

Defines the **UserInfo** model:

-   **Attributes**:
    -   `id`: Unique identifier.
    -   `gender_id`: Foreign key to `genders`.
    -   `user_settings_id`: Foreign key to `user_settings`.
    -   `first_name`: User's first name.
    -   `last_name`: User's last name.
    -   `birthdate`: User's date of birth.
    -   `created_at`, `updated_at`: Timestamps for creation and modification.
-   **Table**: `userinfos`
-   **Relationships**:
    -   `gender`: Links to `Gender`.
    -   `settings`: Links to `UserSettings`.
-   **Example**:
    ```python
    <UserInfo(id=1, first_name='John', last_name='Doe', gender_id=1, user_settings_id=2)>
    ```

---

### 4. `user_role.py`

Defines the **UserRole** model:

-   **Attributes**:
    -   `id`: Unique identifier.
    -   `role`: Role name.
    -   `description`: Optional role description.
-   **Table**: `userroles`
-   **Example**:
    ```python
    <UserRole(id=1, role='Admin', description='Administrator role')>
    ```

---

### 5. `user_settings.py`

Defines the **UserSettings** model:

-   **Attributes**:
    -   `id`: Unique identifier.
    -   `currency`: Preferred currency (default: USD).
    -   `language`: Preferred language (default: ENG).
-   **Table**: `user_settings`
-   **Example**:
    ```python
    <UserSettings(id=1, currency='EUR', language='FR')>
    ```

---

## Usage 📦

1. Import the required models from the package:

    ```python
    from user_infos import Gender, UserInfo, UserRole, UserSettings
    ```

2. Use SQLAlchemy to interact with the database:

    - Add a new gender:

        ```python
        gender = Gender(gender='Female', description='A female gender representation')
        session.add(gender)
        session.commit()
        ```

    - Query user information:
        ```python
        user_info = session.query(UserInfo).filter_by(first_name='John').first()
        print(user_info)
        ```

---

## Conclusion 🚀

The **User Infos Module** provides a comprehensive toolkit for managing user data in a structured and efficient manner. With its modular design and database integration, it serves as a robust foundation for user management in any application.
