'''
You are building a small data utility that demonstrates your understanding of JSON structure, validation, serialisation, and parsing in Python.

Tasks
Task 1 — Create and Serialise a Nested JSON Object Create a Python dictionary representing a 
student with keys: name, age, passed (boolean), marks (list of three numbers), and a nested address
object containing city and pincode. Convert it to a formatted JSON string using json.dumps() with 
indent=4 and print the result.

Task 2 — Parse JSON and Access Values Using json.loads(), parse the JSON string from Task 1 
back into a Python dictionary. Print the student's name, the second marks value, and the city from 
the nested address.

Task 3 — Identify and Fix Invalid JSON The following JSON string contains two syntax errors. 
Identify them in a comment, fix the string, parse it using json.loads(), and print the result.
\n\npython\nbad_json = '{ name: \"Raj\", \"score\": 88, \"active\": true, }'\n

Task 4 — Build a JSON Array of Objects Create a Python list of three dictionaries, 
each representing a product with keys product_name, price, and in_stock (boolean). 
Convert the list to a JSON string with indent=2 and print it.

'''



import json

# Task 1 — Create and Serialise a Nested JSON Object
student = {
    "name": "Chakri",
    "age": 19,
    "passed": True,
    "marks": [85, 90, 78],
    "address": {
        "city": "Tirupathi",
        "pincode": "501107"
    }
}

# Convert to formatted JSON string
json_string = json.dumps(student, indent=4)
print("Task 1 Output:")
print(json_string)


# Task 2 — Parse JSON and Access Values
parsed_data = json.loads(json_string)

print("\nTask 2 Output:")
print("Name:", parsed_data["name"])
print("Second Marks:", parsed_data["marks"][1])
print("City:", parsed_data["address"]["city"])


# Task 3 — Identify and Fix Invalid JSON
# Errors:
# 1. Keys must be in double quotes → name is not quoted
# 2. Trailing comma after last key-value pair is not allowed

bad_json = '{ "name": "Chakri", "score": 88, "active": true }'

fixed_data = json.loads(bad_json)

print("\nTask 3 Output:")
print(fixed_data)


# Task 4 — Build a JSON Array of Objects
products = [
    {"product_name": "Laptop", "price": 55000, "in_stock": True},
    {"product_name": "Mouse", "price": 500, "in_stock": True},
    {"product_name": "Keyboard", "price": 1500, "in_stock": False}
]

products_json = json.dumps(products, indent=2)

print("\nTask 4 Output:")
print(products_json)