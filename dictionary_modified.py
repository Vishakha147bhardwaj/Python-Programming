# # 1. Creating a dictionary
# user_profile = {
#     "username": "coder_99",
#     "followers": 1250,
#     "is_premium": True
# }

# # 2. Accessing values using a key
# print(user_profile["username"])   # Output: coder_99

# # 3. Adding a new key-value pair
# user_profile["location"] = "India"

# # 4. Modifying an existing value
# user_profile["followers"] = 1251

# # 5. Deleting a key-value pair
# del user_profile["is_premium"]

# print(user_profile)
# # Output: {'username': 'coder_99', 'followers': 1251, 'location': 'India'}

# employee = {"name": "Sara", "role": "Developer"}

# # Safe retrieval with .get()
# salary = employee.get("salary", 0) 
# print(salary)  # Output: 0 (Returns 0 instead of throwing a KeyError)

# # View components
# print(list(employee.keys()))    # Output: ['name', 'role']
# print(list(employee.values()))  # Output: ['Sara', 'Developer']
# print(list(employee.items()))   # Output: [('name', 'Sara'), ('role', 'Developer')]

# device = {"brand": "Apple", "model": "iPhone 15"}

# # Merging / Updating data
# device.update({"model": "iPhone 16 PRO", "storage": "256GB"})
# print(device)
# # Output: {'brand': 'Apple', 'model': 'iPhone 16 PRO', 'storage': '256GB'}

# # Using setdefault
# device.setdefault("color", "Black")
# print(device["color"]) # Output: Black
# print(device)

cart = {"item": "Laptop", "quantity": 1, "price": 85000}

# Remove specific key and capture its value
removed_price = cart.pop("price")
print(removed_price)  # Output: 85000

# Remove the last added item
last_item = cart.popitem()
print(last_item)      # Output: ('quantity', 1)

# Empty everything
cart.clear()
print(cart)           # Output: {}
