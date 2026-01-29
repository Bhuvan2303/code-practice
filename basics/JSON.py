import json

# Save dictionary to a JSON file
data = {"name": "John", "age": 21}
with open("info.json", "w") as f:
    json.dump(data, f)

# Read from JSON file
with open("info.json", "r") as f:
    data = json.load(f)
print(data)

# Save a list of dictionaries
contacts = [
    {"name": "Aman", "phone": "9999"},
    {"name": "Riya", "phone": "8888"}
]

with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=4)