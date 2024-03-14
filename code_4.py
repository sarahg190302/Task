import json

# JSON data
json_data = [{'name': 'John', 'age': 25, 'id': 1}, 
             {'name': 'Jane', 'age': 22, 'id': 2}, 
             {'name': 'Mike', 'age': 28, 'id': 3}, 
             {'name': 'Emma', 'age': 30, 'id': 4}]

# Save JSON data to a file
with open('data.json', 'w') as f:
    json.dump(json_data, f, indent=4)

# Print or save JSON data as required
print(json_data)