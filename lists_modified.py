# # 1. CREATE
# # Initialising a list of fruits
# fruits = ["apple", "banana", "cherry"]

# # 2. READ
# # Accessing elements using positive and negative indexing
# print(fruits[0])   # Output: apple
# print(fruits[-1])  # Output: cherry (last item)

# # 3. UPDATE
# # Modifying an item at a specific index
# fruits[1] = "blueberry" 

# # Adding items (Append adds to the end, Insert adds at a specific index)
# fruits.append("date")          # ['apple', 'blueberry', 'cherry', 'date']
# fruits.insert(1, "elderberry") # ['apple', 'elderberry', 'blueberry', 'cherry', 'date']

# # 4. DELETE
# # Removing items by value or position
# fruits.remove("cherry")  # Removes the first occurrence of "cherry"
# popped_item = fruits.pop(0)  # Removes and returns item at index 0 ("apple")
# del fruits[1]            # Deletes the item at index 1 directly

# # 5. LIST COMPREHENSIONS
# # A concise syntax to create a new list from an existing collection
# numbers = [1, 2, 3, 4, 5]
# # Syntax: [expression for item in iterable if condition]
# squares_of_evens = [x**2 for x in numbers if x % 2 == 0] 
# print(squares_of_evens)  # Output: [4, 16]


# # CREATE
# # Defining fixed GPS coordinates for London
# london_coordinates = (51.5074, -0.1278)

# # READ
# latitude = london_coordinates[0]
# print(f"Latitude: {latitude}") # Output: Latitude: 51.5074

# # INTENTIONAL ERROR (Demonstrating Immutability)
# try:
#     london_coordinates[0] = 52.0000
# except TypeError as e:
#     print(f"Error: {e}") # Output: 'tuple' object does not support item assignment



# CREATE & AUTOMATIC DE-DUPLICATION
# Duplicates are automatically removed upon creation
visitor_ids = {101, 102, 103, 101, 104, 102}
print(visitor_ids)  # Output: {101, 102, 103, 104}

# UPDATE (Add/Remove)
visitor_ids.add(105)       # Adds a new unique element
visitor_ids.remove(103)    # Removes element 103

# MATHEMATICAL SET OPERATIONS
admin_users = {"Alice", "Bob", "Charlie"}
power_users = {"Bob", "David", "Edward"}

# Intersection (Who is in BOTH sets?)
both = admin_users.intersection(power_users)
print(both)  # Output: {'Bob'}

# Difference (Who is an admin but NOT a power user?)
admins_only = admin_users.difference(power_users)
print(admins_only)  # Output: {'Alice', 'Charlie'}
