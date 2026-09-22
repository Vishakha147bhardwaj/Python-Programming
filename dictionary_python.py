# Creating a dictionary
user_profile = {
    "username": "coder_dev",
    "login_count": 5,
    "is_admin": True,
    "permissions": ("read", "write")  # Tuples are allowed as keys or values
}

# Accessing values
print(user_profile["username"])       # Output: coder_dev
print(user_profile.get("email", "N/A")) # Output: N/A (Safe way to avoid KeyError)

# Modifying and adding elements
user_profile["login_count"] = 6 
print(user_profile["login_count"])     # Update existing
user_profile["location"] = "Mumbai" 
print(user_profile["location"])       # Add new key-value pair

# Removing elements
user_profile.pop("is_admin")          # Removes "is_admin"
print(user_profile)                    # Output: {'username': 'coder_dev', 'login_count': 6, 'permissions': ('read', 'write'), 'location': 'Mumbai'}

print(user_profile.keys())   # Output: dict_keys(['username', 'login_count', 'permissions', 'location'])
print(user_profile.values()) # Output: dict_values(['coder_dev', 6, ('read', 'write'), 'Mumbai'])
print(user_profile.items())  # Output: dict_items([('username', 'coder_dev'), ('login_count', 6), ('permissions', ('read', 'write')), ('location', 'Mumbai')])


profile = {"name": "Neha", "city": "Mumbai"}

# Update / Merge
profile.update({"city": "Bengaluru", "country": "India"})
print(profile) # Output: {'name': 'Neha', 'city': 'Bengaluru', 'country': 'India'}

# Setdefault (useful for initializing missing keys)
language = profile.setdefault("language", "English")
print(language) # Output: English
print(profile)  # Output: {'name': 'Neha', 'city': 'Bengaluru', 'country': 'India', 'language': 'English'}

cart = {"item": "Laptop", "price": 55000, "discount": 0.1}

# Pop specific item
price = cart.pop("price")
print(price) # Output: 55000

# Pop last inserted item
last_item = cart.popitem()
print(last_item) # Output: ('discount', 0.1)

# Clear everything
cart.clear()
print(cart) # Output: {}
