import json

# A sample Python dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the Python dictionary to a JSON string
json_string = json.dumps(x)

# Print the JSON string
print(json_string)