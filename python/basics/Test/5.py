class Secret:
    def __init__(self, password):
        self.__password = password   # private

    def get_password(self):
        print("Password:", self.__password)

c = Secret(4376)
c.get_password()