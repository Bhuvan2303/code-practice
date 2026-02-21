class Bird:
    def sound(self):
        print("Chirp")
class Dog:
    def sound(self):
        print("Woof")

animals = [Bird(), Dog()]
for i in animals:
    i.sound()
