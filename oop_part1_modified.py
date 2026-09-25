# class Robot:
#     def __init__(self,name,model_feature):
#         self.name = name
#         self.model_feature = model_feature
#         print(f"This is {self.name} an automated agent")

#     def feature_highlight(self):
#         print(f"This {self.name} is {self.model_feature}")

# robot_one = Robot('omega','explorer')
# robot_two = Robot('alpha','adventurer')
# print(robot_one.feature_highlight())


class Smartphone:
    def __init__(self, brand, battery):
        # Attributes
        self.brand = brand
        self.battery_level = battery
    
    # Method to check state
    def display_status(self):
        print(f"📱 {self.brand} Status: Battery is at {self.battery_level}%.")
    
    # Method that modifies internal attributes
    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        print(f"🔌 Charging... Added {amount}%.")

# Instantiate the phone
my_phone = Smartphone("FruitPhone", 45)

# # Interact with the attributes via methods
# my_phone.display_status()  # Output: 📱 FruitPhone Status: Battery is at 45%.
# my_phone.charge(20)        # Output: 🔌 Charging... Added 20%.
# my_phone.display_status()  # Output: 📱 FruitPhone Status: Battery is at 65%.

my_phone2 = Smartphone("Apple",100)
my_phone2.charge(20)
my_phone2.display_status()