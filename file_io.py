my_file = open("shopping_list.txt", "w")

my_file.write("Apple\n")  # "\n" means "hit the Enter key" to start a new line
my_file.write("Milk\n")

my_file.close() 
# my_file = open("fruits.txt", "w")

# my_file.write("Banana\n")  # "\n" means "hit the Enter key" to start a new line
# my_file.write("Pear\n")

# my_file.close() 
my_file = open("shopping_list.txt", "a")
my_file.write("Banana\n")
my_file.close() 

my_file = open("shopping_list.txt", "r")

content = my_file.read()
print('The values of content that were read from shopping_list file \n', content) 
my_file.close()


with open("save_data.txt", "w") as game_file:
    game_file.write("Player Level: 5\n")
    game_file.write("Coins: 120\n")

with open("save_data.txt", "r") as game_file:
    saved_content = game_file.read()
    print(saved_content)

# try:
#     with open("secret_passwords.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("Oops! 'secret_passwords.txt' wasn't found. We will create a blank one for you.")