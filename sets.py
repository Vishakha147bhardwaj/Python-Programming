# Creation (Duplicates are ignored)
unique_numbers = {1, 2, 3, 3, 4}  # Stores as {1, 2, 3, 4}
print(unique_numbers)
# # # Modification
unique_numbers.add(5)
print(unique_numbers)
unique_numbers.remove(1)
print(unique_numbers)
# # # # Core Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.intersection(set_b)) 
print(set_a.union(set_b))