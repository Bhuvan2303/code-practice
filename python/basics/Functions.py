#Function wihtout parameters
def greet():
    print("Hello")
greet()


#Function with parameters
def add(a,b):
    return a + b
print(add(5, 5))                                         


#Default arguments
def greet(name="Guest"):
    print("Hello, name")
greet()


#keyword arguments
print(add(b=5, a=2))


#*args -> unlimited arguments
def total(*num):
    return sum(num)
print(total(2,3,4,10))


#**kwargs -> unlimited keyword arguments
def info(**details):
    print(details)
info(name="Bhuvan", age=20)


#Return multiple values
def calc(a, b):
    return a+b, a-b, a*b
x, y, z = calc(10, 4)
print(x, y, z)


#Local vs Global variable
x = 10
def test():
    x = 5
    print(x)
test()
print(x)