class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"

account = Account(input("Owner: "), float(input("Initial balance: ")))
account.deposit(float(input("Deposit: ")))
account.withdraw(float(input("Withdraw: ")))
print(account)
