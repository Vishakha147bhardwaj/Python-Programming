def my_func():
    local_var = "I am local"
    print(local_var)

my_func()
# print(local_var)  # ❌ NameError: 'local_var' is not defined outside the function


def outer_func():
    outer_var = "I am in the outer function"
    
    def inner_func():
        print(outer_var)

    inner_func()

outer_func()

global_var = "I am global"

def check_global():
    print(global_var)  # Works! Reads from global scope

check_global()


counter = 0

def increment():
    global counter  # Tells Python to use the top-level 'counter'
    counter += 1

increment()
print(counter)  # Output: 1

def outer():
    count = 0
    def inner():
        nonlocal count  # Targets the 'count' in outer()
        count += 1
    inner()
    print(count)  # Output: 1

outer()


