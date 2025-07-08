from Cart import Cart

class Customer:
    def __init__(self, name: str, email:str, address: str=None, balance: float=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        if email is None or not isinstance(email, str) or '@' not in email:
            raise ValueError("Invalid email address.")
        
        self.name = name
        self.email = email
        self.address = address
        self.balance = balance
        self.cart = Cart()

    def add_balance(self, amount: int):
        if amount <= 0:
            raise ValueError("Cannot add negative balance.")
        self.balance += amount

    def change_address(self, new_address: str):
        if not new_address or not isinstance(new_address, str):
            raise ValueError("Address cannot be empty.")
        self.address = new_address

    def address_exists(self):
        return self.address is not None and isinstance(self.address, str) and len(self.address) > 0