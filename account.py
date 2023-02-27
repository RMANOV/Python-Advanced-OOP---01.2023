# Account
# Create a class called Account. Upon initialization, it should receive an id (number), a name (string), 
# and a balance (integer; optional; 0 by default). The class should also have 3 additional instance methods:
# -	credit(amount) - adds the amount to the balance and returns the new balance
# -	debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance. 
# Otherwise, return "Amount exceeded balance"
# -	info() - returns "User {name} with account {id} has {balance} balance"


class Account:
    def __init__(self, id_number, name, balance=0):
        self.id_number = id_number
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id_number} has {self.balance} balance"
