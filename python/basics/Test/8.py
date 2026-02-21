class Bank:
    bank_name = "SBI"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        print(self.name)
        print(self.balance)

a = Bank("Bhuvan", 3984)
b = Bank("John", 4987)
print(a.bank_name)
print(b.bank_name)
a.show()