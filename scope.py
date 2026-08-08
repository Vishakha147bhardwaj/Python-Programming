# def my_function():
#     local_var = "I am inside!"
#     print(local_var)

# my_function()
# print(local_var)

# def outer_function():
#     outer_var = "Outer"

#     def inner_function():
#         nonlocal outer_var
#         outer_var = 'Modified Outer'
#     inner_function()
#     print(outer_var)
# outer_function()

# count = 10 

# def increment():
#     global count
#     # count  = 2
#     count = count + 1
#     print(count)

# increment()
# print(count) 
# print(len("Python"))
# variable overshadowing
# x = "Global"

# def test():
#     x = "Local" # Shadows the global x
#     print("Inside:", x)

# test()          # Prints: Inside: Local
# print("Outside:", x)

# # 1. Define the function
# def greet():
#     print("Hello, World!")

# # 2. Call the function
# greet()  # Prints: Hello, World!

# def greet_user(name):  # 'name' is a parameter
#     print(f"Hello, {name}!")

# greet_user("Alice") 

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)

# def power(base, exponent=2):
#     return base ** exponent

# print(power(4))    
# print(power(4, 3))

# def describe_pet(animal, name):
#     print(f"I have a {animal} named {name}.")

# describe_pet(name="Whiskers", animal="cat")
def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4))  # Prints: 10

def user_profile(**info):
    print(info)

user_profile(username="dev_jon", role="admin")  # Prints: {'username': 'dev_jon', 'role': 'admin'}

# *args
# **kwargs

# Syntax: lambda parameters: expression
# square = lambda x: x * x
# print(square(5)) 

# def square(a):
#     return a*a
