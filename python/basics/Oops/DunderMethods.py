class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self): #__str__ decides how the object looks when printed.
        return f"{self.brand} - {self.model}"
    
c = Car("Tata", "Nexon")
print(c)


class Book:
    def __init__(self, pages):
        self.pages = pages
    def __len__(self): #__len__ tells python how to treat len() for an object.
        return self.pages
    
b = Book(330)
print(len(b))


class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

b = Number(30)
a = Number(20)
print(b + a)
