from enum import Enum

class BookTypes(Enum):
    PAPER = "Paper"
    EBOOK = "Ebook"
    SHOWCASE = "Showcase"

class Book():
    def __init__(self, isbn: str, title: str, year: int, price: float, author: str, book_type: BookTypes):
        self.isbn = isbn
        self.title = title
        self.year = year
        self.price = price
        self.author = author
        self.book_type = book_type

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

# Getters for Book attributes
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def get_year(self):
        return self.year
    def get_price(self):
        return self.price
    def get_author(self):
        return self.author
    def get_book_type(self):
        return self.book_type


class PaperBook(Book):
    def __init__(self, isbn: str, title: str, year: int, price: float, author: str, stock: int, shipping_cost: float):
        super().__init__(isbn, title, year, price, author, BookTypes.PAPER)
        self.stock = stock
        self.shipping_cost = shipping_cost


class EBook(Book):
    def __init__(self, isbn: str, title: str, year: int, price: float, author: str, file_type: str):
        super().__init__(isbn, title, year, price, author, BookTypes.EBOOK)
        self.file_type = file_type


class ShowcaseBook(Book):
    def __init__(self, isbn: str, title: str, year: int, price: float, author: str):
        super().__init__(isbn, title, year, price, author, BookTypes.SHOWCASE)
