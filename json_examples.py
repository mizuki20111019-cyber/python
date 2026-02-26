import json


# =====================-
#1. Convert a dictionary to JSON
# =====================

print("=== 1. Dictionary to JSON ===")

user = {
    "name":"Taro",
    "age":13,
    "is_student":True,
}

# Conver Python dictionary to JSON string
json_text = json.dumps(user, indent=2)

print("JSON string:")
print(json_text)
print()


# =====================
#2. Convert JSON to a dictionary
# =====================

print("=== 2. JSON to Dictionary ===")

text = '''
{
    "name": "Hanako",
    "age": 14,
    "is_student": true
}
'''

# Convert JSON string to Python dictionary
data = json.loads(text)

print("Python data:")
print(data)
print("Name:",data["name"])
print()


# =====================
#3. Save JSON to a file
# =====================

print("=== 3. Modify Data ===")

# Increase age by 1
data["age"] = data["age"] + 1

print("Age increased by 1")
print(json.dumps(data, indent = 2))
print()

