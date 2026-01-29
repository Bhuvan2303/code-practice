class Bank:
    def __init__(self, balance):
        self.__balance = balance # __ is used to make variables private

    def show(self):
        print("Balance:", self.__balance)

obj = Bank(5000)
obj.show()
print(obj.__balance) #Error because private variable can not accessable from outside
