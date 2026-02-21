# Constructor(__init__) runs automatically when object is created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Methods (function inside class)
    def greet(self):
        print("Hello, I am", self.name)

# Creating object
p = Person("Bhuvan", 20)
print(p.name)
print(p.age)
# Methods
p.greet()

# Updating object values
p.age = 30
print(p.age)

# Multiple objects
p1 = Person("John", 20)
p2 = Person("Xyz", 40)
p3 = Person("Abc", 23)
people = [p1, p2, p3]
for person in people:
    print(person.name, person.age)