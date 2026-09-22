def calculate_area(width, height):
    if width <= 0 or height <= 0:
        return "Invalid dimensions"  # Exits early
    
    area = width * height
    return area  # Returns value to the caller

result = calculate_area(5, 4)
print(result)  # Output: 20

# default arguments
# Right way to handle mutable defaults
def append_to_list(element, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2] (Independent and safe)

# arbitrary positional arguments
def sum_all_numbers(*args):
    print(type(args))  # Output: <class 'tuple'>
    return sum(args)

print(sum_all_numbers(10, 20, 30, 40))  # Output: 100

# keyword arbitrary arguments
def build_user_profile(username, **kwargs):
    print(type(kwargs))  # Output: <class 'dict'>
    profile = {"user": username}
    profile.update(kwargs)
    return profile

print(build_user_profile("johndoe", email="john@test.com", role="Admin"))
# Output: {'user': 'johndoe', 'email': 'john@test.com', 'role': 'Admin'}

# lambda function

# Standard Function
def square_num(x):
    return x ** 2

# Equivalent Lambda Function
square_lambda = lambda x: x ** 2

print(square_num(5))      # Output: 25
print(square_lambda(5))   # Output: 25

# Practical Use Case: Custom Sorting
coordinates = [(1, 5), (3, 2), (2, 8)]
# Sort the list of tuples based on the second item (index 1)
coordinates.sort(key=lambda item: item[1])
print(coordinates)  # Output: [(3, 2), (1, 5), (2, 8)]

