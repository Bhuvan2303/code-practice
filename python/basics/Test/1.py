class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

c1 = Car("Tata", "cd345", 2025)
c2 = Car("Tata", "er245", 2025)
c3 = Car("Tata", "fe457", 2025)

c = [c1, c2, c3]
for i in c:
    i.details()