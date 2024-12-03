# Orders Directory 📦

The `orders` directory implements the `Order` model, which manages guest orders for accommodations in the booking system.
This model tracks essential details such as pricing, dates, and guest information.

## Directory Structure 📂

```plaintext
orders/
|---- __init__.py
|---- order.py
```

## Modules Overview 📝

### 1. `__init__.py`

The module initializer for the `orders` package. It exports the `Order` class for direct import from the package.

**Exports**:

-   `Order`

**Example**:

```python
from orders import Order
```

### 2. `order.py`

Defines the `Order` class, which models a guest order in the booking system.

**Features**:

-   Links orders to guests (`User`) and accommodations (`Accommodation`) via foreign keys.
-   Tracks important details such as pricing, stay dates, and guest count.

**Attributes**:

-   `id`: Primary key of the order.
-   `accomodation_id`: Foreign key referencing the `accomodations` table.
-   `guest_id`: Foreign key referencing the `users` table.
-   `total_price`: Total price for the booking.
-   `date_checkin`: Check-in date for the order.
-   `date_checkout`: Check-out date for the order.
-   `people_amount`: Number of people included in the booking.
-   `confirmation_code`: A unique confirmation code for the booking.

**Relationships**:

-   `accomodation`: Links to the `Accomodation` model.
-   `guest`: Links to the `User` model.

**Constraints**:

-   `people_amount` must be greater than 0.

**Example**:

```python
order = Order(
    accomodation_id=1,
    guest_id=2,
    total_price=250.00,
    date_checkin="2024-12-10",
    date_checkout="2024-12-15",
    people_amount=3,
    confirmation_code="CONF12345"
)
print(order)
# Output: <Order(id=1, accomodation_id=1, guest_id=2, total_price=250.00,
# dates=(2024-12-10 to 2024-12-15), people=3)>
```

## How to Use This Module 🚀

1. **Import the Order Class**:

    ```python
    from orders import Order
    ```

2. **Create an Order**:

    ```python
    new_order = Order(
        accomodation_id=5,
        guest_id=7,
        total_price=350.00,
        date_checkin="2024-01-01",
        date_checkout="2024-01-05",
        people_amount=2,
        confirmation_code="ABC123"
    )
    session.add(new_order)
    session.commit()
    ```

3. **Query Existing Orders**:
    ```python
    orders = session.query(Order).all()
    for order in orders:
        print(order)
    ```

## Dependencies 📦

-   SQLAlchemy
-   `config.Base`: Base declarative class for defining database schemas.

## Conclusion 🎯

The `orders` directory provides a structured implementation for managing guest bookings in the system.
With its comprehensive tracking of order details, it facilitates efficient booking management and enhances the overall user experience.
