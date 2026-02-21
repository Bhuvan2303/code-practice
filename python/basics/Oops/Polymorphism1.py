class Animal:
    def sound(self):
        print("Animals makes sound")

class Dog(Animal):
    def sound(self):
        print("Woof Woof")

d = Dog()
d.sound()