class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

c = Animal("Tommy")
d = Dog(c.name, 'Labrador')
print(d.name, d.breed)