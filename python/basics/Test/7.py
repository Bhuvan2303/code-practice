class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks}"
    
    def __len__(self):
        return len(self.marks)
    
a = Student("Bhuvan", [45, 23, 20])
print(len(a))
print(a)