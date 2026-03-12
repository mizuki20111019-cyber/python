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

# ============================
#3. Modify Data
#=============================

print("=== 3. Modify Data ===")

# Increase age by 1
data["age"] = data["age"] + 1
print("Age increased by 1")
print(json.dumps(data, indent = 2))
print()


# Convert JSON string to Python dictionary
data = json.loads(text)

print("Python data:")
print(data)
print("Name:",data["name"])
print()




# =====================
#4. JSON with a list(array)
#======================

print("=== 4. JSON with LIST ===")

users = [
    {"name": "Taro", "age": 13},
    {"name": "Hanako", "age": 14},

]

print (json.dumps(users, indent=2))
print()


print("=== 5. Add New User === ")

new_user = {"name": "Ken", "age": 12}

# Append new dictionary to list
users.append(new_user)

print(json.dumps(users, indent=2))
print()

#===========-=======================
#5. Add New User
#========================

print("=== 5. Add New User === ")

new_user = {"name": "Ken", "age": 12}

# Append new dictionary to list
users.append(new_user)

print(json.dumps(users, indent=2))
print()

