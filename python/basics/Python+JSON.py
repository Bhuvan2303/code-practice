# Convert python dict -> JSON string
import json
data = {"name": "John", "age": 20}, {"name": "John", "age": 20}
json_data = json.dumps(data)
print(json_data)

# Convert JSON string -> python dict
import json
json_text = '{"name": "John", "age": 20}'
data = json.loads(json_text)
print(data)