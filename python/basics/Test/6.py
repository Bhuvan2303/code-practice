class Circle:
    def area(self):
        print("area of Circle")

class Square:
    def area(self):
        print("area of Square")

a = [Circle(), Square()]
for i in a:
    i.area()
