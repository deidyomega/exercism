from threading import Lock

class BankAccount:
    closed_msg = "Account is closed"

    def __init__(self):
        self.state = "closed"
        self.balance = 0
        self.lock = Lock()

    def get_balance(self):
        if self.state == "closed":
            raise ValueError(self.closed_msg)
        return self.balance

    def open(self):
        if self.state == "open":
            raise ValueError("Account is open already.")
        self.state = "open"

    def deposit(self, amount):
        if self.state == "closed":
            raise ValueError(self.closed_msg)            
        if amount < 0:
            raise ValueError("Can not withdrawal neg. values.  To deposit, use deposit().")
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if self.state == "closed":
            raise ValueError(self.closed_msg)            
        if amount < 0:
            raise ValueError("Can not withdrawal neg. values.  To deposit, use deposit().")
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        with self.lock:
            self.balance -= amount

    def close(self):
        if self.state == "closed":
            raise ValueError("Account already closed")
        self.state = "closed"
        self.balance = 0
