# Reviews Directory 📦

The `reviews` directory provides the implementation of the `Review` model, which represents guest reviews for accommodations.
It includes features like ratings, comments, and timestamps to track feedback on accommodations.

## Directory Structure 📂

```plaintext
reviews/
|---- __init__.py
|---- review.py
```

## Modules Overview 📝

### 1. `__init__.py`

The initializer for the `reviews` module, enabling the `Review` class to be imported directly.

**Exports**:

-   `Review`

**Example**:

```python
from reviews import Review
```

### 2. `review.py`

Defines the `Review` class, which models reviews provided by guests.

**Features**:

-   Links reviews to guests (`User`) and accommodations (`Accommodation`) via foreign keys.
-   Captures review details such as rating, comment, and creation timestamp.

**Attributes**:

-   `id`: Primary key of the review.
-   `accommodation_id`: Foreign key referencing the `accommodations` table.
-   `guest_id`: Foreign key referencing the `users` table.
-   `rating`: Rating given by the guest (1 to 5).
-   `comment`: Optional feedback text.
-   `created_at`: Timestamp indicating when the review was created.

**Relationships**:

-   `accommodation`: Links to the `Accommodation` model.
-   `guest`: Links to the `User` model.

**Constraints**:

-   `rating` must be between 1 and 5.

**Example**:

```python
review = Review(
    accommodation_id=1,
    guest_id=2,
    rating=5,
    comment="Amazing stay!"
)
print(review)
# Output: <Review(id=1, accommodation_id=1, guest_id=2, rating=5,
# comment='Amazing stay!', created_at=2024-12-01)>
```

## How to Use This Module 🚀

1. **Import the Review Class**:

    ```python
    from reviews import Review
    ```

2. **Create a Review**:

    ```python
    new_review = Review(
        accommodation_id=1,
        guest_id=3,
        rating=4,
        comment="Great location, but the room was a bit small."
    )
    session.add(new_review)
    session.commit()
    ```

3. **Query Existing Reviews**:
    ```python
    reviews = session.query(Review).all()
    for review in reviews:
        print(review)
    ```

## Dependencies 📦

-   SQLAlchemy
-   `config.Base`: Base declarative class for defining database schemas.

## Conclusion 🎯

The `reviews` directory provides a powerful structure for managing guest feedback on accommodations.
It ensures comprehensive tracking of ratings, comments, and timestamps, fostering transparency and quality improvement in the booking system.
