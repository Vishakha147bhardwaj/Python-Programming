# # --- CREATE ---
# # Initialising a list with elements or creating an empty one
# fruits = ["apple", "banana", "cherry"]
# empty_list = []

# # --- READ ---
# # Accessing elements using positive index (starts at 0) or negative index (starts from the end)
# first_fruit = fruits[0]      # "apple"
# last_fruit = fruits[-1]      # "cherry"
# sub_list = fruits[0:2]       # ["apple", "banana"] (Slicing)

# # --- UPDATE ---
# # Changing a specific element or adding new elements
# fruits[1] = "blueberry"      # Modifies index 1: ["apple", "blueberry", "cherry"]
# fruits.append("date")        # Adds to the end: ["apple", "blueberry", "cherry", "date"]
# fruits.insert(1, "mango")    # Inserts at index 1: ["apple", "mango", "blueberry", "cherry", "date"]

# # --- DELETE ---
# # Removing elements from the list
# fruits.remove("mango")       # Removes specific item by value
# popped_item = fruits.pop()   # Removes and returns the last item ("date")
# del fruits[0]                # Removes item at index 0 using the del keyword
# fruits.clear()               # Empties the entire list: []


number_tuple = ('num1','num2','num3')
print(number_tuple[0]) 
print(number_tuple[0:2])