print("--- Bakery System Starting ---")
with open('grandmas_cake_recipe.txt','w') as recipe:
    recipe.write('🧁 We want to make a cake recepie, and we have to use flour, butter, coco powder, and vanilla essence for it \n')
    recipe.write('We mix the dry ingredients first flour, baking powder, and powdered sugar, and then mix wet ingredients\n')
    recipe.write('after this we mix, vanilla essence, melted butter, and milk, and put it in oven, and after 30min our cake is ready 🎂 \n')

try:
    print("Attempting to load the secret recipe...")
    
    with open("grandmas_cake_recipe.txt", "r") as recipe_file:
        instructions = recipe_file.read()
        print("Recipe loaded successfully!")
        print(instructions)

except FileNotFoundError:
    print("⚠️ Alert: The recipe file is missing! Using default vanilla cake recipe instead.")

except PermissionError:
    print("🔒 Alert: You do not have administrator permissions to open this file.")

finally:
    print("System Cleaned: Temporary memory cleared.")
    print("--- Bakery System Ready for Customers ---")
