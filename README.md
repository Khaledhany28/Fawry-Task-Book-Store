# 📚 BookStore Management System

A simple yet structured **Python Bookstore Management System** that handles multiple book types, customer shopping carts, inventory operations, and checkout with shipping and emailing services.

---

## ⚙️ Features

### ✉️ Book Types

```python
class BookTypes(Enum):
    PAPER = "Paper"
    EBOOK = "Ebook"
    SHOWCASE = "Showcase"
```

- **PaperBook** includes stock and shipping costs.
- **EBook** is delivered via email.
- **ShowcaseBook** cannot be purchased.

### 👨‍🏠 Customer

```python
class Customer:
    def __init__(self, name: str, email:str, address: str=None, balance: float=0.0):
        self.cart = Cart()
```

- Holds customer data including name, email, address, balance.
- Linked to a `Cart` instance.
- Can add balance and change address.

### 📆 Book Management

```python
class BookStore:
    def __init__(self):
        self.inventory = dict()
```

- Add or remove books from inventory.
- Avoids duplicate ISBNs.
- Supports bulk addition.

### 🛒 Shopping Cart

```python
class Cart:
    def __init__(self):
        self.items = dict()
        self.price = 0.0
```

- Add/remove books.
- Enforces stock constraints.
- Prevents duplicate EBooks or ShowcaseBooks.

### 💳 Checkout Flow

```python
if customer.balance < cart_total_price:
    raise ValueError("Insufficient balance.")
```

```python
if isinstance(book, PaperBook):
    ShippingService.add_shipping(book, quantity, customer.address)
```

```python
elif isinstance(book, EBook):
    MailService.add_shipping(book, customer.email)
```

- Validates cart and balance.
- Deducts stock for PaperBooks.
- Calls shipping or emailing services.


### 🔧 Testing

```python
class TestBookStore:
    def run_tests(self):
        self.test_add_books()
        self.test_remove_outdated_books()
        self.test_checkout()
```

- Adds books to store.
- Removes outdated books.
- Performs a checkout.
- Displays final inventory and cart.

---

## 📁 Project Structure

```
Book.py                     # Book classes
Cart.py                     # Shopping cart logic
Customer.py                 # Customer class
extra.py                    # Services
BookStore.py                # Inventory and checkout
main/test_bookstore.py      # Testing suite
```

---

### 📸 Sample Output

![Output screenshot](screenshots\test_output.png)

---

## ✨ Author

**Khaled Hany**