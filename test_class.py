from BookStore import BookStore
from Book import *
from Customer import Customer

class TestBookStore:
    def __init__(self):
        self.store = BookStore()
        self.customer = Customer("Khaled Hany", "khaled@gmail.com", "123 street", 10000)
        self.books = {
            "Book1": PaperBook("123456", "Book1", 2020, 10.0, "Author1", 5, 3.0),
            "Book2": EBook("51256652", "Book2", 2021, 15.0, "Author2", "PDF"),
            "Book3": ShowcaseBook("54656812", "Book3", 2024, 20.0, "Author3"),
            "Book4": PaperBook("159753", "Book4", 2025, 25.0,"Author4", 10, 2.5),
            "Book5": EBook("7575432", "Book5", 2024, 30.0, "Author5", "EPUB"),
            "Book6": ShowcaseBook("9842301458", "Book6", 2025, 35.0, "Author6"),
            "Book7": PaperBook("1258", "Book7", 2026, 40.0, "Author7", 15, 5.0),
            "Book8": EBook("95123", "Book8", 2027, 45.0, "Author8","MOBI"),
            "Book9": ShowcaseBook("78542", "Book9", 2028, 50.0, "Author9"),
        }

    def test_add_books(self):
        

        self.store.add_books(self.books.values())
        print("Books added to the store:")
        self.store.list_books()
        print("\n")

    def test_remove_outdated_books(self):
        # Assuming the current year is 2023
        removed_books = self.store.remove_outdated_books(2)
        assert len(removed_books) == 2, "Should remove 2 outdated books"
        print("Removed outdated books:", removed_books, "\n")
    
    def test_checkout(self):
        self.customer.cart.add(self.books["Book4"], 2)  # PaperBook
        self.customer.cart.add(self.books["Book5"], 1)  # EBook
        print("Cart total price before checkout:", self.customer.cart.total_price())
        self.store.checkout(self.customer)
        print("Customer balance after checkout:", self.customer.balance)
    def test_list_books(self):
        self.store.list_books()

    def run_tests(self):
        print("Running tests...")
        self.test_add_books()
        self.test_remove_outdated_books()
        self.test_checkout()
        print("\n\tInventory after checkout:")
        self.test_list_books()
        print("\n\tCustomer's cart after checkout:")
        print("Cart: ", self.customer.cart.items)
        print("All tests passed!")


if __name__ == "__main__":
    test_store = TestBookStore()
    test_store.run_tests()