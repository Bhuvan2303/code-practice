class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, ",", "Age:", self.age)
    
class Employee(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary

    def show_employee(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Job:", self.job)
        print("Salary:", self.salary)

e = Employee("Bhuvan", 20, "Student", 0)
e.show()
e.show_employee()