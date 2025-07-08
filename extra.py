from Book import Book, PaperBook, BookTypes

class ShippingService:
    def __init__(self):
        self.shipments = []

    
    @staticmethod
    def add_shipping(book: Book, quantity: int, address: str):
        pass

class MailService:
    def __init__(self):
        self.shipments = []

    @staticmethod
    def add_shipping(book: Book, email: str):
        pass