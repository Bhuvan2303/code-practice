class Student:
    school = "ABC School"
    def __init__(self, name):
        self.name = name

s = Student("John")
r = Student("Bhuvan")
print(s.school)
print(r.school)