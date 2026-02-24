class Vehical:
    def start(self):
        print("Some sound")

class Bike(Vehical):
    def start(self):
        print("Bike started")

c = Bike()
c.start()