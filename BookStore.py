from Book import Book, PaperBook, EBook, ShowcaseBook
from Customer import Customer
from datetime import datetime
from extra import ShippingService, MailService

class BookStore:
    def __init__(self):
        self.inventory = dict() # Using a dictionary to store books as {isbn: Book}

    def add_book(self, book: Book):

        # Check if the book is already in the inventory and its a PaperBook then increment stock
        if isinstance(book, PaperBook):
            existing_book = self.inventory.get(book.isbn, None)
            if existing_book:
                existing_book.stock += book.stock
                return

        # Check if the book already exists in the inventory
        if book.isbn in self.inventory:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        
        # If the book is not a PaperBook or does not exist, add it to the inventory
        self.inventory[book.isbn] = book

    def add_books(self, books: list):
        for book in books:
            self.add_book(book)

    def remove_book(self, isbn: str):
        if isbn in self.inventory:
            del self.inventory[isbn]
        else:
            raise ValueError(f"Book with ISBN {isbn} does not exist in the inventory.")
        
    def remove_outdated_books(self, max_years_old):
        current_year = datetime.now().year
        removed_books = {}
        for isbn, book in list(self.inventory.items()):
            if book.year + max_years_old < current_year:
                removed_books[isbn] = book
                del self.inventory[isbn]

        return removed_books
    
    
    def checkout(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer.")
        
        if not customer.cart.items:
            raise ValueError("Cart is empty.")
        
        cart_total_price = customer.cart.total_price()
        
        if customer.balance < cart_total_price:
            raise ValueError("Insufficient balance.")
        

        for item in customer.cart.items.values():
            book, quantity = item

            # Check if the book exists in the inventory
            if book.isbn not in self.inventory:
                raise ValueError(f"Book with ISBN {book.isbn} does not exist in the inventory.")
            
            # Check if the book is a PaperBook and has sufficient stock
            if isinstance(book, PaperBook):
                if book.stock < quantity:
                    raise ValueError(f"Insufficient stock for {book.title}.")
                
                if customer.address_exists() is False:
                    raise ValueError("Customer address is required for shipping.")
                
                # If the book is a PaperBook, add shipping if applicable
                if book.shipping_cost > 0:
                    ShippingService.add_shipping(book, quantity, customer.address)

                # Deduct the stock from the book
                book.stock -= quantity

            elif isinstance(book, EBook):
                # For EBooks, we can assume no stock management is needed
                MailService.add_shipping(book, customer.email)

            elif isinstance(book, ShowcaseBook):
                raise ValueError("Showcase books cannot be purchased directly.")

        print("\n")
        # Display Receipt
        print("=" * 40)
        print("🧾 Receipt".center(40))
        print("=" * 40)
        print(f"Customer: {customer.name}")
        print("-" * 40)
        print(f"{'Item':<20}{'Qty':>5}{'Price':>15}")
        print("-" * 40)

        for cart_book, cart_quantity in customer.cart.items.values():
            line_total = cart_book.price * cart_quantity
            print(f"{cart_book.title:<20}{cart_quantity:>5}{line_total:>15.2f}")

        print("-" * 40)
        print(f"{'Total Charged:':<25}${(cart_total_price):>10.2f}")
        print(f"{'Balance After Checkout:':<25}${(customer.balance - cart_total_price):>10.2f}")
        print("=" * 40)
        print("\n")
        
        # Deduct the total price from the customer's balance
        customer.balance -= cart_total_price
        
        # Clear the cart after checkout
        customer.cart.items.clear()
        customer.cart.price = 0.0

    def list_books(self):
        if not self.inventory:
            return "No books available in the inventory."
        
        for isbn, book in self.inventory.items():
            if isinstance(book, PaperBook):
                print(f"ISBN: {isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Price: {book.price}, Type: {book.book_type.value} (Stock: {book.stock}, Shipping Cost: {book.shipping_cost})")
            elif isinstance(book, EBook):
                print(f"ISBN: {isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Price: {book.price}, Type: {book.book_type.value} (File Type: {book.file_type})")
            elif isinstance(book, ShowcaseBook):
                print(f"ISBN: {isbn}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Price: {book.price}, Type: {book.book_type.value}")
            else:
                book_type = "Unknown"

        return self.inventory

    def find_book(self, isbn: str):
        return self.inventory.get(isbn, None)
    




if __name__ == "__main__":
    # Example usage
    bookstore = BookStore()
    
    paper_book = PaperBook("1234567890", "Python Programming", 2026, 29.99, "John Doe", 10, 5.00)
    ebook = EBook("0987654321", "Learning Python", 2026, 19.99, "Jane Smith", "PDF")
    showcase_book = ShowcaseBook("1122334455", "Showcase Book", 2026, 39.99, "Alice Johnson")
    
    bookstore.add_book(paper_book)
    bookstore.add_book(ebook)
    bookstore.add_book(showcase_book)
    
    print(bookstore.list_books())
    print("\n")

    Khaled = Customer("Khaled", "khaled@gmail.com", "123 Main St", 10000.0)

    print(bookstore.remove_outdated_books(2))
    
    print(bookstore.list_books())
    print(bookstore.find_book("1234567890"))

    Khaled.cart.add(paper_book, 2)
    Khaled.cart.add(ebook, 1)
    print("Cart total price:", Khaled.cart.total_price())
    bookstore.checkout(Khaled)
    print("Customer balance after checkout:", Khaled.balance)
    print("Cart after checkout:", Khaled.cart.items)
    print("Inventory after checkout:", bookstore.list_books())