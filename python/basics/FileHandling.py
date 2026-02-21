# Writing to a file
file = open("data.txt", "w")
file.write("Hello, this is my firstt file.")
file.close()

# Reading from a file
file = open("data.txt", "r")
content = file.read()
file.close()
print(content)

# Appending to a file
file = open("data.txt", "a")
file.write("\nAdding a new line.")
file.close()

# With statement
with open("data.txt", "w") as f:
    f.write("Hello world")