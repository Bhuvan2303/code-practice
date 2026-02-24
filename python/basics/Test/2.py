class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def show_balance(self):
        print("Balance", self.balance)

c = BankAccount("Bhuvan", 4355)
print(c.name)

c.deposit(345)
c.withdraw(4000)
c.show_balance()