student = {
    "name": "John",
    "age": 20,
    "marks": 88
}
print(student["name"])
print(student["marks"])

# Adding new key-value pairs
student["grade"] = "A"

# Updating values
student["marks"] = 92

# Removing items
student.pop("age")

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through keys
for key, value in student.items():
    print(key, value)