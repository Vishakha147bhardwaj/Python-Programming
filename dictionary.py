import copy

# squared_nums = {x:x**2 for x in range(6)}
# print(squared_nums)
# Base dictionary to start our examples
# user_profile = {"username": "codex_99", "role": "developer", "status": "active"}

# # 1. get() - Safely retrieves a value without raising a KeyError
# role = user_profile.get("role")  # Returns 'developer'
# plan = user_profile.get("plan", "Free")  # Returns 'Free' (fallback value)

# # 2. keys() - Returns a view object of all keys
# all_keys = user_profile.keys()  # dict_keys(['username', 'role', 'status'])

# # 3. values() - Returns a view object of all values
# all_vals = user_profile.values()  # dict_values(['codex_99', 'developer', 'active'])

# # 4. items() - Returns a view object of key-value tuples
# all_items = user_profile.items()  # dict_items([('username', 'codex_99'), ...])

# # 5. update() - Merges another dictionary or iterable into the current one
# user_profile.update({"status": "idle", "points": 120})
# # Current dict: {'username': 'codex_99', 'role': 'developer', 'status': 'idle', 'points': 120}

# # 6. setdefault() - Returns value if key exists; if not, inserts key with specified value
# current_role = user_profile.setdefault("role", "guest")  # Returns 'developer' (no change)
# theme_preference = user_profile.setdefault("theme", "dark")  # Inserts 'theme': 'dark' and returns it

# # 7. pop() - Removes the specified key and returns its corresponding value
# removed_status = user_profile.pop("status")  # Removes 'status', returns 'idle'
# # Fallback prevents errors if key is missing:
# missing_item = user_profile.pop("age", None)  # Returns None

# # 8. popitem() - Removes and returns the last inserted key-value pair as a tuple
# last_item = user_profile.popitem()  # Removes and returns ('theme', 'dark')

# # 9. copy() - Creates a shallow copy of the dictionary
# profile_backup = user_profile.copy()

# # 10. fromkeys() - Class method that builds a new dictionary using a sequence of keys
# default_keys = ["health", "mana", "stamina"]
# new_character_stats = dict.fromkeys(default_keys, 100)
# # Result: {'health': 100, 'mana': 100, 'stamina': 100}

# # 11. clear() - Completely empties the target dictionary
# user_profile.clear()  # Result: {}
profile = {'username': 'Vishakha', 'role': 'developer', 'points': 120, 'status': 'active'}
deep = copy.deepcopy(profile)
deep.update({'status':'idle'})
print(deep)
print(profile)
