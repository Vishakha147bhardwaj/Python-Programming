# 'discount' has a default value of 0.0 (no discount)
def calculate_invoice(price, tax=0.18, discount=0.0):
    subtotal = price + (price * tax)
    final_total = subtotal - (subtotal * discount)
    return round(final_total, 2)

# Case A: Omiting optional arguments (uses 18% tax and 0% discount)
print("Standard Billing:", calculate_invoice(1000)) 

# Case B: Overriding tax, omitting discount
print("Duty-Free Billing:", calculate_invoice(1000, tax=0.0))

# Case C: Overriding all arguments (18% tax, 10% discount applied)
print("Loyalty Program Billing:", calculate_invoice(1000, 0.18, 0.10))


# The asterisk (*) packs all loose incoming positional items into a tuple named 'items'
def build_sandwich_order(bread_type, *items):
    print(f"Baking a fresh {bread_type} loaf...")
    print(f"Type of *args under the hood: {type(items)}")
    
    if not items:
        print("Warning: You ordered an empty bread sandwich!")
    else:
        print("Layering ingredients:")
        for layer_number, ingredient in enumerate(items, start=1):
            print(f"  {layer_number}. Adding {ingredient}")
    print("-" * 30)

# Run 1: Sending 3 ingredients
build_sandwich_order("Sourdough", "Cheese", "Tomato", "Lettuce")

# Run 2: Sending 1 ingredient
build_sandwich_order("Rye", "Smoked Salmon")


# The double asterisk (**) packs all named key=value arguments into a dictionary named 'profile'
def create_game_character(name, **profile):
    print(f"Initializing character asset: {name}")
    print(f"Type of **kwargs under the hood: {type(profile)}")
    
    # We can inspect and iterate through the dictionary safely
    for trait, score in profile.items():
        print(f"  -> Trait [{trait.upper()}]: {score}")
    print("-" * 30)

# Run 1: Setting warrior characteristics
create_game_character("Thorin", class_type="Warrior", strength=95, stamina=80)

# Run 2: Setting wizard characteristics 
create_game_character("Gandalf", class_type="Mage", intelligence=99, mana=150, agility=40)


# A traditional function to check if a number is even
def is_even_classic(num):
    return num % 2 == 0

# The exact same logic condensed into a nameless Lambda function assigned to a variable
is_even_lambda = lambda num: num % 2 == 0

print("Classic Function Verification:", is_even_classic(8))
print("Lambda Function Verification:", is_even_lambda(8))

# Common use-case: Inline sorting key for complex structural layouts
coordinate_points = [(1, 5), (9, 2), (4, 8), (3, 1)]

# Sort the pairs based on the Y-coordinate value (index 1 of each tuple)
coordinate_points.sort(key=lambda coordinate: coordinate[1])
print("Sorted by Y-Value:", coordinate_points)



def adding_machine_with_print(a, b):
    result = a + b
    print(f"[Inside Print Machine] Visual output only: {result}")
    # Missing explicit return statement! Python defaults to returning None.

def adding_machine_with_return(a, b):
    result = a + b
    return result # Handing data back to the software architecture

# --- THE TEST ---
output_1 = adding_machine_with_print(10, 20)
output_2 = adding_machine_with_return(10, 20)

print("\n--- Memory Capture Audit ---")
# This fails to do math because output_1 is literally holding nothing (None)
print(f"Value stored in output_1 variable: {output_1}") 

# This works perfectly because output_2 holds the physical integer 30
print(f"Value stored in output_2 variable: {output_2}")
print(f"Using returned data in a new calculation (30 * 2): {output_2 * 2}")
