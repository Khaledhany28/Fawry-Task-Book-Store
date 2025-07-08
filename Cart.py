from Book import Book, PaperBook, BookTypes

class Cart:
    def __init__(self):
        self.items = dict() # Using a dictionary to store items as {isbn: (book, quantity)}
        self.price = 0.0

    def add(self, book: Book, quantity: int=1):
        # Check that the product is in the shop's inventory
        if isinstance(book, PaperBook) and book.stock < quantity:
            raise ValueError("Insufficient quantity of product to add to cart.")
        
        # If the product is not in the cart, add it
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        

        # Check if the product is already in the cart
        existing_book = self.items.get(book.get_isbn(), None)
        if existing_book and existing_book[0].get_book_type() == BookTypes.PAPER:
            # If it is, update the quantity
            existing_quantity = existing_book[1]
            if existing_quantity + quantity > book.stock:
                raise ValueError("Insufficient stock to add the requested quantity.")
            self.items[book.get_isbn()] = (book, existing_quantity + quantity)
            self.price += book.get_price() * quantity
            return
        
        # If the product is not in the cart, add it
        if book.get_isbn() in self.items and self.items[book.get_isbn()][0].get_book_type() != BookTypes.PAPER:
            raise ValueError("Product already exists in the cart.")

        self.items[book.get_isbn()] = (book, quantity)
        self.price += book.get_price() * quantity

    def remove_item(self, book: Book, quantity: int=1):

        existing_book = self.items.get(book.get_isbn(), None)
        if not existing_book:
            raise ValueError("Product not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        cart_book, cart_quantity = existing_book


        if cart_quantity < quantity:
            raise ValueError("Insufficient quantity of product in cart to remove.\nCart_quantity is less than the quantity you want to remove.")
                
        if not isinstance(cart_book, PaperBook):
            quantity = 1

        # Adjust the total price
        self.price -= cart_book.get_price() * quantity

        # Adjust the quantity or remove the item from the cart
        if cart_quantity > quantity:
            self.items[cart_book.get_isbn()] = (cart_book, cart_quantity - quantity)
            return
        if cart_quantity == quantity:
            del self.items[cart_book.get_isbn()]
            return

    def total_price(self):
        return self.price

